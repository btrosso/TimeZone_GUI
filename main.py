from tkinter import *
import pandas
# -------------------------------CONSTANTS-------------------------------#
FONT_NAME = "Arial"
DEFAULT_LIST_HEIGHT = 20


# -------------------------------TIME ZONE OFFSET-------------------------------#
#  contributed by JameaPlays
def select_tz(selection):
    """Assigns the time offset in hours to the new_tz_offset variable based on dropdown selection"""
    global new_tz_offset
    selection = variable.get()
    # Gets the name of the timezone from the dropdown selection
    tz_selected = selection[0:3]
    for tz in tz_dict:
        if tz_selected == tz["Name"]:
            # Gets the time offset from GMT based on the dropdown selection
            new_tz_offset = tz["Offset from GMT"]


# -------------------------------SCREEN SETUP-------------------------------#
# main window
window = Tk()
window.title("TimeZone Buddy App")
window.config(width=600, height=300, bg="black")

# canvas
canvas = Canvas(width=500, height=300, bg="black", highlightthickness=0)
img = PhotoImage(file="cool_python_pic2.png")
canvas.create_image(300, 150, image=img)
timer_text = canvas.create_text(150, 170, text="Some Text", fill="white", font=(FONT_NAME, 15, "bold"))
canvas.grid(column=1, row=1)

# Entries
buddy_name_entry = Entry( width=20)
buddy_name_entry.grid(column=1, row=2, sticky="EW")
buddy_name_entry.insert(0, "Buddy Name")

# Buttons
add_button = Button(text="Add Buddy")
add_button.grid(column=3, row=2)

# Dropdown list - contributed by JameaPlays
tz_data = pandas.read_csv("time_zones.csv")
tz_dict = tz_data.to_dict(orient="records")
new_tz_offset = 0
# Generates a list of strings for the dropdown menu
tz_dropdown_list = [f"{tz['Name']} ({tz['Relative to GMT']})" for tz in tz_dict]

variable = StringVar(value="Time Zones")
tz_dropdown = OptionMenu(window, variable, *tz_dropdown_list, command=select_tz)
tz_dropdown.grid(column=2, row=2, sticky="EW")

#Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=)
# buddy_list = []
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

window.mainloop()
