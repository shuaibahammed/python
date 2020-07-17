# importing tkinter
from tkinter import *

# accesing tkinter to window
window = Tk()

# giving window display appearance
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

# creating a entry box for showing operations
me_text = Entry(window, font=("Arial", 28, 'bold'), textvar=text, width=14, bd=8, bg="powder blue")

# creating button
button1 = Button(window,text="0", bg="black", fg="yellow", height=2, width=2)
button2 = Button(window,text="1", bg="black", fg="yellow", height=2, width=2)
button3 = Button(window,text="2", bg="black", fg="yellow", height=2, width=2)
button4 = Button(window,text="3", bg="black", fg="yellow", height=2, width=2)
button5 = Button(window,text="4", bg="black", fg="yellow", height=2, width=2)
button6 = Button(window,text="5", bg="black", fg="yellow", height=2, width=2)
button7 = Button(window,text="6", bg="black", fg="yellow", height=2, width=2)
button8 = Button(window,text="7", bg="black", fg="yellow", height=2, width=2)
button9 = Button(window,text="8", bg="black", fg="yellow", height=2, width=2)
button10 = Button(window,text="9", bg="black", fg="yellow", height=2, width=2)
button11 = Button(window,text="+", bg="black", fg="yellow", height=2, width=2)
button12 = Button(window,text="-", bg="black", fg="yellow", height=2, width=2)
button13 = Button(window,text="*", bg="black", fg="yellow", height=2, width=2)
button14 = Button(window,text="/", bg="black", fg="yellow", height=2, width=2)
button15 = Button(window,text="=", bg="black", fg="yellow", height=2, width=2)
button16 = Button(window,text=".", bg="black", fg="yellow", height=2, width=2)
button17 = Button(window,text="c", bg="black", fg="yellow", height=2, width=2)

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
