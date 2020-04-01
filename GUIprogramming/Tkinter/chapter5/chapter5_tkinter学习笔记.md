# Data and Classes

本章我们将GUI数据保存到tkinter变量中，然后开始使用面向对象编程(OOP)，用Python编写自己的类，这样可以创建可重用的OOP组件。通过这一章你可以学到下面的知识：

[总的代码github地址](https://github.com/PacktPublishing/Python-GUI-Programming-Cookbook-Third-Edition)。

* 如何使用*StringVar()*
* 如何从一个组件获取数据
* 使用模块级全局变量
* 如何在类中编程来改善GUI
* 书写回调函数
* 创建可复用的GUI组分

## 如何使用*StringVar()*

| strVar = StringVar() | 存储一个字符，默认值为“ ”      |
| -------------------- | ------------------------------ |
| intVar = IntVar()    | 存储一个整数，默认值为0        |
| dbVar = DoubleVar()  | 存储一个浮点数，默认值为0.0    |
| blVar = BooleanVar() | 存储一个布尔值，0-False 1-True |

下面创建一个tkinter变量DoubleVar，并通过+操作符加一个浮点数，相应代码如下：

```python
import tkinter as tk

win = tk.Tk()
doubleData = tk.DoubleVar()
print(doubleData.get())
doubleData.set(2.5)
print(type(doubleData))

add_doubles = 1.258+doubleData.get()
print(add_doubles)
print(type(add_doubles))
```

下面创建tkinter变量StringVar，相应代码如下：

```python
import tkinter as tk

win = tk.Tk()
strData = tk.StringVar()
strData.set('Hello StringVar....')
varData = strData.get()
print(varData)
```

## 如何从一个组件获取数据

```python
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep         # careful - this can freeze the GUI

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")  

tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Tab 1')      # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Tab 2')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# LabelFrame using tab1 as the parent
mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Modify adding a Label using mighty as the parent instead of win
a_label = ttk.Label(mighty, text="Enter a name:")
a_label.grid(column=0, row=0, sticky='W')

# Modified Button Click Function
def click_me(): 
    action.configure(text='Hello ' + name.get() + ' ' + 
                     number_chosen.get())

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')               # align left/West

# Adding a Button
action = ttk.Button(mighty, text="Click Me!", command=click_me)   
action.grid(column=2, row=1)                                

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Spinbox callback 
def _spin():
    value = spin.get()
    print(value)
    scrol.insert(tk.INSERT, value + '\n')
     
# Adding a Spinbox widget
spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=9, command=_spin) # using range
spin.grid(column=0, row=2)

# Using a scrolled Text control    
scrol_w  = 30
scrol_h  =  3
scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scrol.grid(column=0, row=3, sticky='WE', columnspan=3)                    


# Tab Control 2 refactoring  ---------------------------------------------------------
# We are creating a container frame to hold all other widgets -- Tab2
mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=0, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=0, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=0, sticky=tk.W)                     

# GUI Callback function 
def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 

# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())    
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())   


# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold", "Red"]   

# We have also changed the callback function to be zero-based, using the list 
# instead of module-level global variables 
# Radiobutton Callback
def radCall():
    radSel=radVar.get()
    if   radSel == 0: mighty2.configure(text='Blue')
    elif radSel == 1: mighty2.configure(text='Gold')
    elif radSel == 2: mighty2.configure(text='Red')

# create three Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar
radVar.set(99)                                 
 
# Now we are creating all three Radiobutton widgets within one loop
for col in range(3):                             
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, 
                            value=col, command=radCall)          
    curRad.grid(column=col, row=1, sticky=tk.W)             # row=6


# Add a Progressbar to Tab 2
progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2) 

# update progressbar in callback loop
def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i   # increment progressbar
        progress_bar.update()       # have to call update() in loop
    progress_bar["value"] = 0       # reset/clear progressbar  

def start_progressbar():
    progress_bar.start()
    
def stop_progressbar():
    progress_bar.stop()
 
def progressbar_stop_after(wait_ms=1000):    
    win.after(wait_ms, progress_bar.stop)
    
     
# Create a container to hold buttons
buttons_frame = ttk.LabelFrame(mighty2, text=' ProgressBar ')
buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)        

# Add Buttons for Progressbar commands
ttk.Button(buttons_frame, text=" Run Progressbar   ", command=run_progressbar).grid(column=0, row=0, sticky='W')  
ttk.Button(buttons_frame, text=" Start Progressbar  ", command=start_progressbar).grid(column=0, row=1, sticky='W')  
ttk.Button(buttons_frame, text=" Stop immediately ", command=stop_progressbar).grid(column=0, row=2, sticky='W')  
ttk.Button(buttons_frame, text=" Stop after second ", command=progressbar_stop_after).grid(column=0, row=3, sticky='W')  
 
for child in buttons_frame.winfo_children():  
    child.grid_configure(padx=2, pady=2) 
 
for child in mighty2.winfo_children():  
    child.grid_configure(padx=8, pady=2) 

    
# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit() 
    
# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Display a Message Box
def _msgBox():
    msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2019.')  
    
# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)   # display messagebox when clicked
menu_bar.add_cascade(label="Help", menu=help_menu)

# Change the main windows icon
# win.iconbitmap('pyc.ico')

name_entered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()
```

![1582908819508](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1582908819508.png)

















