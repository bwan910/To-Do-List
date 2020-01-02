from tkinter import *
import datetime
from functions import play_music, stop_music

# Create an empty list
tasks = []

# For testing purposes use a default list
tasks = ["Call mom", "Buy a guitar"]


def update_listbox():
    # Clear the current list
    clear_listbox()
    # Populate the listbox
    for task in tasks:
        lst_box.insert("end", task)


def clear_listbox():
    lst_box.delete(0, "end")


def clear_inputbox():
    ipt_Task.delete(0, "end")


def add_task():
    # Get the task to add
    task = ipt_Task.get()
    clear_inputbox()
    # Make sure the task is not empty
    if task != "":
        # Append to the list
        tasks.append(task)
        # Update the listbox
        update_listbox()
    else:
        #lbl_display["text"] = "Please enter a task."
        ipt_Task.delete(0, "end")


def del_one():
    # Get the text of the currently selected item
    task = lst_box.get("active")
    # Confirm it is in the list
    if task in tasks:
        tasks.remove(task)
    # Update the listbox
    update_listbox()


root = Tk()
# To set the size of frame
root.geometry('1000x1000')
root.title("MY TO-DO LIST")

# Button to play music
btn_play = Button(root, text='Play Music', bg="Yellow", command=play_music)
btn_play.grid(pady = 50, padx = 50)
btn_play.place(x=600, y=400)

lbl_music = Label(root, text='Press the buttons for musics', font=('Arial', 12))
lbl_music.place(x=630, y=350)

# Button to stop music
btn_stop = Button(root, text='Stop Music', bg="Yellow", command=stop_music)
btn_stop.place(x=800, y=400)


# to display the calendar title
lbl_calHead = Label(root, text='Display the current date and time', font=('Arial', 12))
lbl_calHead.place(x=610, y=120)

# to display the calendar
date = datetime.datetime.now()
lbl_cal = Label(root, text=date, font=('Arial', 12, 'bold'), bg='cyan')
lbl_cal.place(width=250, x=600, y=150)

# To create the filemenu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=root.quit)

# This is the title
lbl_Title = Label(root, text='TO-DO-LIST', font=('Arial', 20, 'bold'))
lbl_Title.pack()

# This is the two buttons part
btn_add = Button(root, text='Add Task', bg="Yellow", command=add_task)
btn_add.place(width=100, x=20, y=100)
btn_del = Button(root, text="Delete Task", bg="Red", command=del_one)
btn_del.place(width=100, x=20, y=150)

# This is the Entry box
lbl_Tdo = Label(root, text="Enter task:")
lbl_Tdo.place(x=180, y=100)
ipt_Task = Entry(root)
ipt_Task.place(width=200, height=30, x=250, y=100)

# This is the Listbox
lst_box = Listbox(root)
lst_box.place(width=300, height=300, x=200, y=200)

root.mainloop()
