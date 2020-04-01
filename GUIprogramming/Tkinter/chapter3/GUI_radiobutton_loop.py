import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI Notes")
# Disable resizeing the GUI by passing in False/False
# win.resizable(False,False)
colors = ["Blue","Gold","Red"]

def click_me():
	btn.configure(text='Hello '+ name.get()+' '+number_chose.get())

def radCall():
	radSel = radVar.get()
	if radSel == 0: win.configure(background=colors[0])
	elif radSel == 1: win.configure(background=colors[1])
	elif radSel == 2: win.configure(background=colors[2])
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
radVar.set(99)

for col in range(3):
	radbtn=tk.Radiobutton(win,text=colors[col],variable=radVar,value=col,command=radCall)
	radbtn.grid(row=3,column=col,sticky=tk.W)


# Start the GUI
win.mainloop()