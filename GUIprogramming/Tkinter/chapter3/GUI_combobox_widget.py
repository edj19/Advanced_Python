import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI Notes")
# Disable resizeing the GUI by passing in False/False
# win.resizable(False,False)

def click_me():
	btn.configure(text='Hello '+ name.get()+' '+number_chose.get())

label1=ttk.Label(win,text="Enter a name:").grid(row=0,column=0)
label2=ttk.Label(win,text="Choose a number:").grid(row=0,column=1)
# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win,width=12,textvariable=name)
name_entered.grid(row=1,column=0)

number = tk.StringVar()
number_chose = ttk.Combobox(win,width=12,textvariable=number)
number_chose['values'] = (1,2,4,42,56,100)
number_chose.grid(row=1,column=1)
number_chose.current(0)
# name_entered.focus()

btn = ttk.Button(win,text="Click me!",command=click_me)
btn.grid(row=1,column=2)

# Start the GUI
win.mainloop()