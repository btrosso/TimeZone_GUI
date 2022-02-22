from tkinter import *
import pandas
# -------------------------------CONSTANTS-------------------------------#
FONT_NAME = "Arial"


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

# entries
buddy_name_entry = Entry( width=25)
buddy_name_entry.grid(column=1, row=2)
buddy_name_entry.insert(0, "Buddy Name")


# time_zone_data = pandas.read_csv("time_zones.csv")
# # print(time_zone_data)
# OPTIONS = [time_zone_data.Name for index, row in time_zone_data.iteritems()]
# print(OPTIONS)
# # for (index, row) in df_student.iteritems():
# #     if row.students == "Nina":
# #         print(row.scores)
#
# variable = StringVar(window)
# # default value
# variable.set(OPTIONS[0])
#
# time_menu = OptionMenu(window, variable, *OPTIONS)
# time_menu.grid(column=0, row=2)

# buttons
add_button = Button(text="Add Buddy")
add_button.grid(column=2, row=2)

window.mainloop()