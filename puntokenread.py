import tkinter as tk
import os
import re

def readuser():
    try:
        userread = userinput.get()
        with open(userread + ".txt", 'r') as file:
            amount = file.read()
    except FileNotFoundError:
        error = "We cannot find the user:" + userread + ". Check the name, spelling or try again later"
        listbox.insert(tk.END, "     ")
        listbox.insert(tk.END, error)
        listbox.insert(tk.END, "     ")
    except Exception as e:
        error = "An Error Occurred, if this continues, post an issue in Github on the Issues page"
        listbox.insert(tk.END, "     ")
        listbox.insert(tk.END, error)
        listbox.insert(tk.END, "     ")
    finally:
        print("Successful Prompt with 0 known errors")
        listbox.insert(tk.END, "     ")
        listbox.insert(tk.END, userread + "s' pun tokens: " + amount)
        listbox.insert(tk.END, "     ")

root = tk.Tk()
root.title("Pun Token System: Administrator Console")

listbox = tk.Listbox(root, height=40, width=140)
listbox.grid(row=0, column=0, columnspan=3, pady=10)

userinput = tk.Entry(root, width=50)
userinput.grid(row=1, column=0)

button = tk.Button(text="Look", command=readuser)
button.grid(row=1, column=2)


listbox.insert(tk.END, "Welcome to the Pun Token Reader. V 0.1 Compiled 30th of December 2023. Put the user in the input box below (Case sensitive) and it will read out the pun tokens")


root.mainloop()
