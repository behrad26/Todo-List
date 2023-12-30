# Package import:
from tkinter import *
import functions
import datetime
import webbrowser
from tkinter.messagebox import showinfo

# Functions:
# <Filling Listboxes <<-------------------------------------------------------------------------->> Filling Listboxes> #
def fill_boxes():
    todo_list.delete(0, "end")
    completed_list.delete(0, "end")
    for item in functions.numeric_generator_iter(functions.read("todo_list.txt"), 1, " -- "):
        if "".join(item.split("-")[1:]).replace(" ", "") != "":
            todo_list.insert("end", item)
    for item in functions.numeric_generator_iter(functions.read("comp_list.txt"), 1, " -- "):
        if "".join(item.split("-")[1:]).replace(" ", "") != "":
            completed_list.insert("end", item)

# <Listbox Selection <<-------------------------------------------------------------------------->> Listbox Selection> #
def listselect(event):
    global last_selected_item
    try:
        selected_item_index = int(str(todo_list.curselection())[1:-2])
        list_items = functions.read("todo_list.txt")
        last_selected_item = {"listbox":"todo", "address":"todo_list.txt", "index":selected_item_index, "item":list_items[selected_item_index]}
    except:
        try:
            selected_item_index = int(str(completed_list.curselection())[1:-2])
            list_items = functions.read("comp_list.txt")
            last_selected_item = {"listbox": "completed", "address":"comp_list.txt", "index": selected_item_index, "item": list_items[selected_item_index]}
        except:
            pass
    item_value = list_items[selected_item_index]
    task_field.delete(0, "end")
    task_field.insert(0, item_value)


# <Item Adding <<-------------------------------------------------------------------------------------->> Item Adding> #
def add():
    functions.add("todo_list.txt", task_field.get())
    fill_boxes()

# <Item Removing <<---------------------------------------------------------------------------------->> Item Removing> #
def remove():
    functions.remove(last_selected_item["address"], last_selected_item["index"] + 1)
    fill_boxes()

# <Item Editing <<------------------------------------------------------------------------------------>> Item Editing> #
def edit():
    functions.edit(last_selected_item["address"], last_selected_item["index"] + 1, task_field.get())
    fill_boxes()

# <Item Completing <<------------------------------------------------------------------------------>> Item Completing> #
def complete():
    if last_selected_item["listbox"] == "todo":
        functions.add("comp_list.txt", functions.complete(last_selected_item["address"], last_selected_item["index"] + 1))
        showinfo("CONGRATULATIONS", f"you completed the task number {last_selected_item['index'] + 1}:\n{last_selected_item['item']}")
        fill_boxes()

def calendar():
    # Functions:
    # Solar calendar
    def solar():
        root1.destroy()
        webbrowser.open_new_tab("https://www.time.ir/")

    # Gregorian calendar
    def gregorian():
        root1.destroy()
        webbrowser.open_new_tab("https://www.timeanddate.com/calendar/")

    # Window definition
    root1 = Tk()
    root1.title("Behrad Todo - Choose Calendar")
    root1.geometry("400x140")
    root1.iconbitmap("55281.ico")
    root1.resizable(False, False)
    root1["bg"] = "#202020"

    # Elements definition:
    # <Labels <<------------------------------------------------------------------------------------------------>> Labels> #
    cal_choose_label = Label(root1, text="Choose the type of calendar:", bg="#202020", fg="#fffff2", font=("Bold", 20))
    # <Buttons <<---------------------------------------------------------------------------------------------->> Buttons> #
    solar_button = Button(root1, text="Solar", bg="#2f2f2f", fg="#ffffff", command=solar, bd=3, font=("Tahoma", 15))
    gregorian_button = Button(root1, text="Gregorian", bg="#2f2f2f", fg="#ffffff", command=gregorian, width=10, bd=3, font=("Tahoma", 15))

    # Placements:
    # <Labels <<------------------------------------------------------------------------------------------------>> Labels> #
    cal_choose_label.place(x=20, y=20)
    # <Buttons <<---------------------------------------------------------------------------------------------->> Buttons> #
    solar_button.place(x=65, y=80, width=122)
    gregorian_button.place(x=200, y=80, width=122)


    # Starting window mainloop
    root1.mainloop()

# Date checking:
today = str(datetime.date.today()).split("-")
today.reverse()
today = "/".join([today[1], today[0], today[2]])
with open("owner_name.txt", "r") as file:
    owner = file.read()
with open("last_date.txt", "r") as file:
    last_date = file.read()
if functions.date_check(today, last_date):
    with open("todolist.txt", "w") as file:
        file.write("")
    with open("comp_list.txt", "w") as file:
        file.write("")
    with open("last_date.txt", "w") as file:
        file.write(today)

# Window definition:
root = Tk()
root.title("Behrad Todo")
root.geometry("1085x540")
root.resizable(False, False)
root["bg"] = "#202020"
# Elements definition:
# <Labels <<------------------------------------------------------------------------------------------------>> Labels> #
name_label = Label(root, text=owner, bg="#202020", fg="#fffff2", font=("Bold", 20))
god_label = Label(root, text="------------------------------------------- In The Name Of GOD -------------------------------------------", bg="#202020", fg="#fffff2", font=("Bold", 20))
date_label = Label(root, text=today, bg="#202020", fg="#fffff2", font=("Bold", 20))
todo_label = Label(root, text="Tasks you have TODO:", bg="#202020", fg="#f00000", font=("Bold", 20))
completed_label = Label(root, text="Tasks you've COMPLETED:", bg="#202020", fg="#00ff00", font=("Bold", 20))
# <Listboxes <<------------------------------------------------------------------------------------------>> Listboxes> #
todo_list = Listbox(root, bg="#2f2f2f", fg="#ffffff", selectbackground="#006494", selectforeground="azure", selectmode="single", bd=4, font=("Tahoma", 15))
completed_list = Listbox(root, bg="#2f2f2f", fg="#ffffff", selectbackground="#00ff00", selectforeground="azure",selectmode="single", bd=4, font=("Tahoma", 15))
# <Scrollbars <<---------------------------------------------------------------------------------------->> Scrollbars> #
todo_y_scrollbar = Scrollbar(root, orient = "vertical", command=todo_list.yview)
todo_x_scrollbar = Scrollbar(root, orient = "horizontal", command=todo_list.xview)
completed_y_scrollbar = Scrollbar(root, orient = "vertical", command=completed_list.yview)
completed_x_scrollbar = Scrollbar(root, orient = "horizontal", command=completed_list.xview)
# <Entries <<---------------------------------------------------------------------------------------------->> Entries> #
task_field = Entry(root, bg="#2f2f2f", fg="#ffffff", width=70, bd=4, font=("Arial", 20))
# <Buttons <<---------------------------------------------------------------------------------------------->> Buttons> #
add_button = Button(root, text="Add", bg="#2f2f2f", fg="#ffffff", command=add, bd=3, font=("Tahoma", 15))
remove_button = Button(root, text="Remove", bg="#2f2f2f", fg="#ffffff", command=remove, width=10, bd=3, font=("Tahoma", 15))
edit_button = Button(root, text="Edit", bg="#2f2f2f", fg="#ffffff", command=edit, width=10, bd=3, font=("Tahoma", 15))
complete_button = Button(root, text="Complete", bg="#2f2f2f", fg="#ffffff", command=complete, width=10, bd=3, font=("Tahoma", 15))
refresh_button = Button(root, text="Refresh", bg="#2f2f2f", fg="#ffffff", command=fill_boxes, width=10, bd=3, font=("Tahoma", 15))
clear_button = Button(root, text="Clear", bg="#2f2f2f", fg="#ffffff", command=lambda: task_field.delete(0, "end"), width=10, bd=3, font=("Tahoma", 15))
cal_button = Button(root, text="Calendar", bg="#2f2f2f", fg="#ffffff", command=calendar, width=10, bd=3, font=("Tahoma", 15))
exit_button = Button(root, text="Exit", bg="#2f2f2f", fg="#ffffff", command=root.destroy, width=10, bd=3, font=("Tahoma", 15))


# Configurations:
# <Listboxes <<------------------------------------------------------------------------------------------>> Listboxes> #
todo_list.config(yscrollcommand=todo_y_scrollbar.set, xscrollcommand=todo_x_scrollbar.set)
completed_list.config(yscrollcommand=completed_y_scrollbar.set, xscrollcommand=completed_x_scrollbar.set)

# Placements:
# <Labels <<------------------------------------------------------------------------------------------------>> Labels> #
name_label.place(x=12, y=35)
god_label.place(x=13, y=5)
date_label.place(x=930, y=35)
todo_label.place(x=10, y=70)
completed_label.place(x=725, y=70)
# <Listboxes <<------------------------------------------------------------------------------------------>> Listboxes> #
todo_list.place(x=15, y=115, width=505, height=285)
completed_list.place(x=565, y=115, width=505, height=285)
# <Scrollbars <<---------------------------------------------------------------------------------------->> Scrollbars> #
todo_y_scrollbar.place(x=520, y=115, height=302)
todo_x_scrollbar.place(x=15, y=400, width=505)
completed_y_scrollbar.place(x=548, y=115, height=302)
completed_x_scrollbar.place(x=565, y=400, width=505)
# <Entries <<---------------------------------------------------------------------------------------------->> Entries> #
task_field.place(x=12, y=425)
# <Buttons <<---------------------------------------------------------------------------------------------->> Buttons> #
add_button.place(x=12, y=487, width=122)
remove_button.place(x=146, y=487, width=122)
edit_button.place(x=281, y=487, width=122)
complete_button.place(x=415, y=487, width=122)
refresh_button.place(x=549, y=487, width=122)
clear_button.place(x=683, y=487, width=122)
cal_button.place(x=818, y=487, width=122)
exit_button.place(x=952, y=487, width=122)

# Filling the window with content:
fill_boxes()
completed_list.bind("<<ListboxSelect>>", listselect)
todo_list.bind("<<ListboxSelect>>", listselect)

# Starting window mainloop
root.mainloop()
