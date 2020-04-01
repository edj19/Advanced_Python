import tkinter as tk
from tkinter import ttk
from tkinter import Menu

win = tk.Tk()

win.title("Python GUI Notes")
# Disable resizeing the GUI by passing in False/False
# win.resizable(False,False)
colors = ["Blue","Gold","Red"]

def quit():
	win.quit()
	win.destroy()
	exit()

def click_me():
	btn.configure(text='Hello '+ name.get()+' '+number_chose.get())

def radCall():
	radSel = radVar.get()
	if radSel == 0: mighty2.configure(background=colors[0])
	elif radSel == 1: mighty2.configure(background=colors[1])
	elif radSel == 2: mighty2.configure(background=colors[2])
	pass

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1,text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text='Tab 2')
tabControl.pack(expand=1,fill="both")

#LabelFrame using tab1 as the parent
mighty = ttk.Labelframe(tab1,text=' Mighty Python')
mighty.grid(row=0,column=0,padx=8,pady=4)

# Label using mighty as the parent
a_label = ttk.Label(mighty,text="Enter a name:")
a_label.grid(row=0,column=0,sticky='W')

# Add another label
ttk.Label(mighty,text="Choose a number:").grid(row=0,column=1)

# Add some space around each label
for child in mighty.winfo_children():
	child.grid_configure(padx=8)

# Another tab2
mighty2 = ttk.Labelframe(tab2,text='The Snake')
mighty2.grid(row=0,column=0,padx=8,pady=4)
# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)
menu_bar.add_cascade(label="File",menu=file_menu)

# Create another menu and add menu items
help_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About")


label1=ttk.Label(mighty2,text="Enter a name:").grid(row=0,column=0)
label2=ttk.Label(mighty2,text="Choose a number:").grid(row=0,column=1)
# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty2,width=12,textvariable=name)
name_entered.grid(row=1,column=0)

number = tk.StringVar()
number_chose = ttk.Combobox(mighty2,width=12,textvariable=number)
number_chose['values'] = (1,2,4,42,56,100)
number_chose.grid(row=1,column=1)
number_chose.current(0)
# name_entered.focus()

btn = ttk.Button(mighty2,text="Click me!",command=click_me)
btn.grid(row=1,column=2)

# Create three checkbuttons
chVarDis = tk.StringVar()
check1 = tk.Checkbutton(mighty2,text="Disabled",variable=chVarDis,state='disabled')
check1.select()
check1.grid(row=2,column=0,sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2,text="UnChecked",variable=chVarUn)
check2.deselect()
check2.grid(row=2,column=1,sticky=tk.W)

chVarEn = tk.IntVar()
check1 = tk.Checkbutton(mighty2,text="Enable",variable=chVarEn)
check1.select()
check1.grid(row=2,column=2,sticky=tk.W)

# Radiobutton
radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
	radbtn=tk.Radiobutton(mighty2,text=colors[col],variable=radVar,value=col,command=radCall)
	radbtn.grid(row=3,column=col,sticky=tk.W)

# Create a container to hold labels
btn_frame = ttk.Labelframe(mighty2,text='Label in a Frame')
btn_frame.grid(row=4,column=0,padx=20,pady=40)

# Place labels into the container element
ttk.Label(btn_frame,text='Label1').grid(row=0,column=0)
ttk.Label(btn_frame,text='Label2').grid(row=0,column=1)
ttk.Label(btn_frame,text='Label3').grid(row=0,column=2)

for child in btn_frame.winfo_children():
	child.grid_configure(padx=8,pady=4)

# Start the GUI
win.mainloop()