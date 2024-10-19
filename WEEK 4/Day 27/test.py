import tkinter
from tkinter import *
# #Window
window = Tk()
window.title("Tkinter")
window.minsize(width=400, height=200)

# #Label
label =Label(text="i am a label", font=("Arial", 24))
label.grid(column=0,row=0)

def got_clicked():
    text = input.get()
    label.config(text=text)


# # Button
button = Button(text="Click me", command=got_clicked)
button.grid(column=1,row=1)

nbutton = Button(text="New Button", command=got_clicked)
nbutton.grid(column=2, row=0)

# #Entry
input = Entry(width=10)
input.grid(column=3,row=2)
input.get()








window.mainloop()
