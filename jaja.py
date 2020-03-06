from tkinter import *
import random
s = []
with open ("text.txt") as file:
    s = [row.strip() for row in file]
def clicked():
    lbl.configure(text = random.choice(s))
window = Tk()
window.title("Generator:P")
window.geometry('450x100')
lbl = Label(window, text = "YOUR WISH HERE", font=("Arial Bold", 50),fg = "pink")
btn = Button(window, text="GENERATE",bg = "pink",fg = "green",command = clicked)
btn.grid(column=0, row=1)
lbl.grid(column = 0,row = 0)
window.mainloop()