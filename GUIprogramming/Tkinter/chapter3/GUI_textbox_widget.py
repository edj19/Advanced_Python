import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI Notes")
# Disable resizeing the GUI by passing in False/False
# win.resizable(False,False)

def click_me():
	btn.configure(text='Hello '+ name.get())

ttk.Label(win,text="Enter a name:").grid(row=0,column=0)
# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win,width=12,textvariable=name)
name_entered.grid(row=1,column=0)
# name_entered.focus()

btn = ttk.Button(win,text="Click me!",command=click_me)
btn.grid(row=1,column=1)

# Start the GUI
win.mainloop()