import tkinter as tk
import os
import re

def puncreateuser():
    listbox.insert(tk.END, "to create a new person, just write the name in the user: add the desired amount then, press add")

def addpun():
    user = userinput.get()
    amount = useramount.get()
    with open(user + '.txt','w') as file:
        file.write(amount)




root = tk.Tk()
root.title("Pun Token System: Administrator Console")

listbox = tk.Listbox(root, height=40, width=140)
listbox.grid(row=0, column=0, columnspan=3, pady=10)

userinput = tk.Entry(root, width=50)
userinput.grid(row=1, column=0)

useramount = tk.Entry(root, width=50)
useramount.grid(row=1, column=1)

button = tk.Button(text="Add", command=addpun)
button.grid(row=1, column=2)

button2 = tk.Button(text="New guy", command=puncreateuser)
button2.grid(row=1, column=3)

listbox.insert(tk.END, "Welcome to the Pun Token Administrator console. V 0.1 Compiled 30th of December 2023. Add the user or put the user in on the left, and the amount is on the right")


root.mainloop()
