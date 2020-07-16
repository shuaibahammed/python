#importing tkinter
from tkinter import *

#accesing tkinter to window
window = Tk()

#giving window display design
window.geometry("100x150")
window.title("Calculator")
window.configure(bg="blue")

# creating button
button1 = Button(text="0", bg="black", fg="yellow", height=2,width=2)
button2 = Button(text="1", bg="black", fg="yellow" , height=2,width=2)
button3 = Button(text="2", bg="black", fg="yellow", height=2,width=2)
button4 = Button(text="3", bg="black", fg="yellow", height=2,width=2)
button5 = Button(text="4", bg="black", fg="yellow", height=2,width=2)
button6 = Button(text="5", bg="black", fg="yellow", height=2,width=2)
button7 = Button(text="6", bg="black", fg="yellow", height=2,width=2)
button8 = Button(text="7", bg="black", fg="yellow", height=2,width=2)
button9 = Button(text="8", bg="black", fg="yellow", height=2,width=2)
button10 = Button(text="9", bg="black", fg="yellow", height=2,width=2)
button11 = Button(text="+", bg="black", fg="yellow", height=2,width=2)
button12= Button(text="-", bg="black", fg="yellow", height=2,width=2)
button13= Button(text="*", bg="black", fg="yellow", height=2,width=2)
button14= Button(text="/", bg="black", fg="yellow", height=2,width=2)
button15= Button(text="=", bg="black", fg="yellow", height=2,width=2)
button16= Button(text=".", bg="black", fg="yellow", height=2,width=2)
button17= Button(text="c", bg="black", fg="yellow", height=2,width=2)


#alignment of buttons

button1.grid(row=4,column=2)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=3,column=3)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=2,column=3)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button10.grid(row=1,column=3)
button11.grid(row=3,column=4)
button12.grid(row=2,column=4)
button13.grid(row=1,column=4)
button14.grid(row=4,column=4)
button15.grid(row=5,column=3)
button16.grid(row=4,column=3)
button17.grid(row=4,column=1)


window.mainloop()



