# importing tkinter
from tkinter import *

# accesing tkinter to window
window = Tk()

# giving window display design
window.geometry("100x150")
window.title("Calculator")
window.configure(bg="blue")

# assign a class variable,we create an instance of this class
text = StringVar()
# we declare a variable as globally
exp = ""


# function to display in screen
def click(num):
    global exp
    exp = exp + str(num)
    text.set(exp)


# function for the equal button
def equal():
    global exp
    total = str(eval(exp))
    text.set(total)
    exp = ""


# function for clear
def clear():
    global exp
    exp = ""
    text.set("")


# function for multiplication
def multiply():
    global exp
    multiplication = str(eval(exp))
    text.set(multiplication)
    exp=""

# function for division
def div():
    global exp
    division = str(eval(exp))
    text.set(division)
    exp=""

# function for subtration
def sub():
    global exp
    subtration = str(eval(exp))
    text.set(subtration)
    exp=""

# function for addition
def add():
    global exp
    addition = str(eval(exp))
    text.set(addition)
    exp=""

hello

# creating button
button1 = Button(text="0", bg="black", fg="yellow", height=2, width=2,command=lambda)
button2 = Button(text="1", bg="black", fg="yellow", height=2, width=2,command=lambda)
button3 = Button(text="2", bg="black", fg="yellow", height=2, width=2,command=lambda)
button4 = Button(text="3", bg="black", fg="yellow", height=2, width=2,command=lambda)
button5 = Button(text="4", bg="black", fg="yellow", height=2, width=2,command=lambda)
button6 = Button(text="5", bg="black", fg="yellow", height=2, width=2,command=lambda)
button7 = Button(text="6", bg="black", fg="yellow", height=2, width=2,command=lambda)
button8 = Button(text="7", bg="black", fg="yellow", height=2, width=2,command=lambda)
button9 = Button(text="8", bg="black", fg="yellow", height=2, width=2,command=lambda)
button10 = Button(text="9", bg="black", fg="yellow", height=2, width=2,command=lambda)
button11 = Button(text="+", bg="black", fg="yellow", height=2, width=2,command=lambda)
button12 = Button(text="-", bg="black", fg="yellow", height=2, width=2,command=lambda)
button13 = Button(text="*", bg="black", fg="yellow", height=2, width=2,command=lambda)
button14 = Button(text="/", bg="black", fg="yellow", height=2, width=2,command=lambda)
button15 = Button(text="=", bg="black", fg="yellow", height=2, width=2,command=lambda)
button16 = Button(text=".", bg="black", fg="yellow", height=2, width=2,command=lambda)
button17 = Button(text="c", bg="black", fg="yellow", height=2, width=2,command=lambda)

# alignment of buttons

button1.grid(row=4, column=2)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=3, column=3)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=2, column=3)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button10.grid(row=1, column=3)
button11.grid(row=3, column=4)
button12.grid(row=2, column=4)
button13.grid(row=1, column=4)
button14.grid(row=4, column=4)
button15.grid(row=5, column=3)
button16.grid(row=4, column=3)
button17.grid(row=4, column=1)

window.mainloop()
