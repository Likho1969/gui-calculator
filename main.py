
from tkinter import *

root = Tk()
root.geometry("450x300")
root.title("add 2 numbers")

def add():
    num1 = int(first_number.get())
    num2 = int(second_number.get())
    add = num1 + num2
    return answer.insert(add, add)

def reset():
    first_number.delete(0, END)
    second_number.delete(0, END)

def exit():
    root.destroy()

first_label = Label(root, text="Enter your first number", bd=4)
first_number = Entry(root)

second_label = Label(root, text="Enter your second number", bd=4)
second_number = Entry(root)

third_label = Label(root, text="Your answer", bd=5)
answer = Entry(root)

num1 = Entry(root)
num2 = Entry(root)

button1 = Button(root, text="ADD", command=add, bd=4, padx=3)
button2 = Button(root, text="Reset", command=reset, bd=4, padx=2)
button3 = Button(root, text="Exit", command=exit, bd=4, padx=3)

first_label.place(x=0, y=0)
second_label.place(x=0, y=25)
third_label.place(x=0, y=50)
first_number.place(x=250, y=0)
second_number.place(x=250, y=25)
answer.place(x=250, y=50)
button1.place(x=125, y=75)
button2.place(x=175, y=75)
button3.place(x=255, y=75)

root.mainloop()
