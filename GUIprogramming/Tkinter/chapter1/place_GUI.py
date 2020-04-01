# Importing tkinter module 
import tkinter as tk
# creating Tk window 
master = tk.Tk() 

# setting geometry of tk window 
master.geometry("200x200") 

# button widget 
b1 = tk.Button(master, text = "Click me !") 
b1.place(relx = 1, x =-2, y = 2, anchor ='ne') 

# label widget 
l = tk.Label(master, text = "I'm a Label") 
l.place(anchor = 'nw') 

# button widget 
b2 = tk.Button(master, text = "GFG") 
b2.place(relx = 0.5, rely = 0.5, anchor = 'center') 

# infinite loop which is required to 
# run tkinter program infinitely 
# until an interrupt occurs 
master.mainloop() 
