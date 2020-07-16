from tkinter import *

window = Tk()
window.geometry("400x400")


def hello():
    print("clicked")


# creating button
button = Button(text="ok", width=30, height=30, bg="blue", fg="yellow", command=hello)

# display title
label = Label(window, text="welcome", height=30)

# calling button
button.pack()
label.pack()

window.mainloop()
