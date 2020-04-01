import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title('Tkinter ttk learning')

a_label=ttk.Label(win,text="A Label").grid(column=0,row=0)
# Button Click Event Function
def click_me():
	action.configure(text="I have been clicked!")
	a_label.configure(fg='red')
	a_label.configure(text='A Red label')

action = ttk.Button(win,text="Clicke me",command=click_me)
action.grid(row=0,column=1)

win.mainloop() 