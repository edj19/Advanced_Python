import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI Notes")
# Disable resizeing the GUI by passing in False/False
# win.resizable(False,False)
COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

def click_me():
	btn.configure(text='Hello '+ name.get()+' '+number_chose.get())

def radCall():
	radSel = radVar.get()
	if radSel == 1: win.configure(background=COLOR1)
	elif radSel == 2: win.configure(background=COLOR2)
	elif radSel == 3: win.configure(background=COLOR3)
	pass

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

# Create three checkbuttons
chVarDis = tk.StringVar()
check1 = tk.Checkbutton(win,text="Disabled",variable=chVarDis,state='disabled')
check1.select()
check1.grid(row=2,column=0,sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win,text="UnChecked",variable=chVarUn)
check2.deselect()
check2.grid(row=2,column=1,sticky=tk.W)

chVarEn = tk.IntVar()
check1 = tk.Checkbutton(win,text="Enable",variable=chVarEn)
check1.select()
check1.grid(row=2,column=2,sticky=tk.W)

# Radiobutton
radVar = tk.IntVar()

rad1 = tk.Radiobutton(win,text=COLOR1,variable=radVar,value=1,command=radCall)
rad1.grid(row=3,column=0,sticky=tk.W,columnspan=3)

rad2 = tk.Radiobutton(win,text=COLOR2,variable=radVar,value=2,command=radCall)
rad2.grid(row=3,column=1,sticky=tk.W,columnspan=3)

rad1 = tk.Radiobutton(win,text=COLOR3,variable=radVar,value=3,command=radCall)
rad1.grid(row=3,column=2,sticky=tk.W,columnspan=3)

# Start the GUI
win.mainloop()