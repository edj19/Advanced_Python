# Importing tkinter module 
import tkinter as tk

# creating Tk window 
master = tk.Tk() 

# cretaing a Fra, e which can expand according 
# to the size of the window 
pane = tk.Frame(master) 
pane.pack(fill = tk.BOTH, expand = True) 

# button widgets which can also expand and fill 
# in the parent widget entirely 
b1 = tk.Button(pane, text = "Click me !", 
			background = "red", fg = "white") 
b1.pack(side = tk.TOP, expand = True, fill = tk.BOTH) 

b2 = tk.Button(pane, text = "Click me too", 
			background = "blue", fg = "white") 
b2.pack(side = tk.TOP, expand = True, fill = tk.BOTH) 

b3 = tk.Button(pane, text = "I'm also button", 
			background = "green", fg = "white") 
b3.pack(side = tk.TOP, expand = True, fill = tk.BOTH) 

tk.mainloop() 


