import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI Notes")
# Disable resizeing the GUI by passing in False/False
# win.resizable(False,False)

# Button Click Event Function
def click_me():
	btn.configure(text="** I have been Clicked!**")
	label.configure(foreground='red')
	label.configure(text='A Red Label')
# Adding a Label
label = ttk.Label(win,text="A test Label")
label.grid(row=0,column=0)
# Adding a Button
btn = ttk.Button(win,text="Click me!",command=click_me)
btn.grid(row=0,column=1)


# Start the GUI
win.mainloop()