from tkinter import *
import pandas
from datetime import datetime, timedelta

# -------------------------------CONSTANTS & Global Var-------------------------------#
FONT_NAME = "Arial"
DEFAULT_LIST_HEIGHT = 20
timer = None


# -------------------------------Read from buddy database-------------------------------#
buddy_file = pandas.read_csv("buddy_data.csv")
buddy_dict = buddy_file.to_dict(orient="records")


# -------------------------------TIME ZONE OFFSET-------------------------------#
#  contributed by JameaPlays
def select_tz(selection):
    """Assigns the time offset in hours to the new_tz_offset variable based on dropdown selection"""
    global new_buddy_tz
    selection = variable.get()
    # Gets the name of the timezone from the dropdown selection
    tz_selected = selection[0:3]
    for tz in tz_dict:
        if tz_selected == tz["Name"]:
            # Gets the time offset from GMT based on the dropdown selection
            new_buddy_tz = tz["Offset from GMT"]


# -----------------------------------TIME-------------------------------------#
def get_time():
    """
    Function to get the current time on the user's machine and continually update it.
    This is probably inelegant, but it works for now.
    :return: configures the text in the ct label
    """
    global timer

    timer = root.after(1000, get_time)
    now = datetime.now()
    cur_time = now.strftime('%I:%M %p')
    ct.config(text=f"{cur_time}")


def get_buddy_time(event):
    """Updates the buddy_time_text with the chosen buddy's local time based on their timezone"""
    global timer, buddy_dict
    buddy_selection = listbox.get(listbox.curselection())
    buddy_offset = 0
    for buddy in buddy_dict:
        if buddy["name"] == buddy_selection:
            buddy_offset += buddy["tz_offset"]
    buddy_time = datetime.utcnow() + timedelta(hours=buddy_offset)
    canvas1.itemconfig(buddy_time_text, text=f"{buddy_time.strftime('%I:%M %p')}")


# -----------------------------------FUNCTIONS-------------------------------------#
def listbox_used(event):
    """
    This is just driver code and will most likely be altered or removed.
    """
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


def add_buddy_to_list():
    """
    This function will grab the name and timezone from the corresponding widgets.
    It will add a new entry into the buddy_dict with the name and float offset value corresponding
        the time zone.
    """
    global new_buddy_tz, buddy_dict
    name = buddy_name_entry.get()
    new_buddy = {"name": name, "tz_offset": new_buddy_tz}
    buddy_dict.append(new_buddy)
    buddy_df = pandas.DataFrame(buddy_dict)
    buddy_df.to_csv("buddy_data.csv", index=False)
    listbox.insert(END, name)
    buddy_name_entry.delete(0, END)
    buddy_name_entry.insert(0, "Buddy Name")


def remove_buddy_from_list():
    """
    Removes a buddy from the list_box and calls refresh_listbox to update the contents of the list box.
    """
    global buddy_dict, buddy_names
    buddy_selection = listbox.get(listbox.curselection())
    for i in buddy_dict:
        if i["name"] == buddy_selection:
            buddy_dict.remove(i)
            df_buddy_dict = pandas.DataFrame(buddy_dict)
            df_buddy_dict.to_csv("buddy_data.csv")
    refresh_listbox()


def refresh_listbox():
    """
    Will clear the list box and reload the contents from the updated buddy_dict after removing a buddy.
    """
    global buddy_names
    listbox.delete(0, END)
    buddy_names = [buddy["name"] for buddy in buddy_dict]
    for bud in buddy_names:
        listbox.insert(buddy_names.index(bud), bud)


# -------------------------------SCREEN SETUP-------------------------------#
# main window
root = Tk()
root.title("TimeZone Buddy App")
root.config(width=500, height=300, bg="black")

# Add image file
bg = PhotoImage(file="cool_python_pic2.png")
# Create Canvas
canvas1 = Canvas(root, width=500, height=300, background="black")
canvas1.grid(column=1, row=1)
# Display image
canvas1.create_image(250, 150, image=bg)

# Text for selected buddy's local timezone
buddy_time_text = canvas1.create_text(250, 30, text="00:00", fill="white", font=("Arial", 20, "bold"))

# create a frame for the buddy label and listbox
frame1 = Frame(background="white", width=100, height=290, bg="black")
canvas1.create_window(10, 10, window=frame1, anchor='nw')

buddy_label = Label(frame1, text="Buddy List", bg="black", fg="white")
buddy_label.grid(column=0, row=0)

# Listbox
listbox = Listbox(frame1, width=15, height=16, bg="black", fg="white")
buddy_names = [buddy["name"] for buddy in buddy_dict]
for item in buddy_names:
    listbox.insert(buddy_names.index(item), item)
listbox.bind("<<ListboxSelect>>", get_buddy_time)
listbox.grid(column=0, row=1, rowspan=3)

# create a frame for the add_buddy  and remove_buddy widgets
frame2 = Frame(background="black", width=375, height=30)
canvas1.create_window(120, 270, window=frame2, anchor='nw')

add_buddy = Button(frame2, text="Add", command=add_buddy_to_list)
add_buddy.grid(column=2, row=0)

remove_buddy = Button(frame2, text="Remove", command=remove_buddy_from_list)
remove_buddy.grid(column=3, row=0)

buddy_name_entry = Entry(frame2, width=25)
buddy_name_entry.grid(column=0, row=0, sticky="EW")
buddy_name_entry.insert(0, "Buddy Name")

# frame for user current time
frame3 = Frame(background="black", width=80, height=50)
canvas1.create_window(420, 10, window=frame3, anchor='nw')
user_ct_label = Label(frame3, text="User Time", bg="black", fg="white")
user_ct_label.grid(column=0, row=0)
ct = Label(frame3, text="00:00", bg="black", fg="white", font=("Arial", 10, "bold"))
ct.grid(column=0, row=1)

# Dropdown list - contributed by JameaPlays
tz_data = pandas.read_csv("time_zones_2.csv")
tz_dict = tz_data.to_dict(orient="records")
new_buddy_tz = 0
# Generates a list of strings for the dropdown menu
tz_dropdown_list = [f"{tz['Name']} ({tz['Relative to GMT']})" for tz in tz_dict]

variable = StringVar(value="Time Zones")
tz_dropdown = OptionMenu(frame2, variable, *tz_dropdown_list, command=select_tz)
tz_dropdown.config(highlightthickness=0, width=15, font=("Arial", 8, "bold"))
tz_dropdown.grid(column=1, row=0, sticky="EW")


get_time()
root.mainloop()
