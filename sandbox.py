# from tkinter import *
import pandas
from datetime import datetime
# # -------------------------------CONSTANTS & Global Var-------------------------------#
# FONT_NAME = "Arial"
# DEFAULT_LIST_HEIGHT = 20
# buddy_dict = [
#     {"name": "example name", "tz_offset": 5},
#     {"name": "Buddy 1", "tz_offset": -5},
#     {"name": "Buddy 2", "tz_offset": 0},
# ]
#
#
#
#
# # -------------------------------TIME ZONE OFFSET-------------------------------#
# #  contributed by JameaPlays
# def select_tz(selection):
#     """Assigns the time offset in hours to the new_tz_offset variable based on dropdown selection"""
#     global new_buddy_tz
#     selection = variable.get()
#     # Gets the name of the timezone from the dropdown selection
#     tz_selected = selection[0:3]
#     for tz in tz_dict:
#         if tz_selected == tz["Name"]:
#             # Gets the time offset from GMT based on the dropdown selection
#             new_tz_offset = tz["Offset from GMT"]
#
#
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# def add_buddy_to_list():
#     global tz_dict, buddy_dict
#     name = buddy_name_entry.get()
#     tz = variable.get()
#     buddy_dict["name"] = name
#     # TODO: 1. pull the offset number from the tz_dict using the variable given from the dropdown
#     #buddy_dict["tz_offset"] =
#
#
# # -------------------------------SCREEN SETUP-------------------------------#
# # main window
# root = Tk()
# root.title("TimeZone Buddy App")
# root.config(width=500, height=300, bg="black")
#
# # Add image file
# bg = PhotoImage(file="cool_python_pic2.png")
# # Create Canvas
# canvas1 = Canvas(root, width=500, height=300, background="black")
# canvas1.grid(column=1, row=1)
# # Display image
# canvas1.create_image(250, 150, image=bg)
#
# canvas1.create_text(250, 30, text="Welcome", fill="white", font=("Arial", 20, "bold"))
#
# # create a frame for the buddy label and listbox
# frame1 = Frame(background="white", width=100, height=290, bg="black")
# canvas1.create_window(10, 10, window=frame1, anchor='nw')
#
# buddy_label = Label(frame1, text="Buddy List", bg="black", fg="white")
# buddy_label.grid(column=0, row=0)
#
# # Listbox
# listbox = Listbox(frame1, width=15, height=16, bg="black", fg="white")
# buddy_list = ["Buddy 1", "Buddy 2"]
# for item in buddy_list:
#     listbox.insert(buddy_list.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.grid(column=0, row=1, rowspan=3)
#
# # create a frame for the add_buddy widgets
# frame2 = Frame(background="black", width=375, height=30)
# canvas1.create_window(120, 270, window=frame2, anchor='nw')
#
# add_buddy = Button(frame2, text="Add", command=add_buddy_to_list)
# add_buddy.grid(column=2, row=0)
#
# # Dropdown list - contributed by JameaPlays
# tz_data = pandas.read_csv("time_zones.csv")
# tz_dict = tz_data.to_dict(orient="records")
# new_buddy_tz = 0
# # Generates a list of strings for the dropdown menu
# tz_dropdown_list = [f"{tz['Name']} ({tz['Relative to GMT']})" for tz in tz_dict]
#
# variable = StringVar(value="Time Zones")
# tz_dropdown = OptionMenu(frame2, variable, *tz_dropdown_list, command=select_tz)
# tz_dropdown.grid(column=1, row=0, sticky="EW")
#
#
# buddy_name_entry = Entry(frame2, width=28)
# buddy_name_entry.grid(column=0, row=0, sticky="EW")
# buddy_name_entry.insert(0, "Buddy Name")
#
#
#
#
#
# root.mainloop()


now = datetime.now()
# string formatted time
current_time = now.strftime("%H:%M")
# convert the current time of user to an int
ct_hour = int(current_time[:2])
# not converting the minute to an int because the time zone differences only deal in hours
ct_minute = current_time[3:]
print("Current Time =", current_time)
print(type(current_time))
print(ct_hour)
print(ct_minute)

buddy_file = pandas.read_csv("buddy_data.csv")
buddy_dict = buddy_file.to_dict(orient="records")
print(buddy_dict)

ct_hour += buddy_dict[0]["tz_offset"]

print("Current Time =", current_time)

def update_time():
