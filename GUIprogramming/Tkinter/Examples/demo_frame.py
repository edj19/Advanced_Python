__author__ = "Dejun E"
__license__ = "GPL"

import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib
import matplotlib.pylab as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
matplotlib.use('TkAgg')
class Materials:
	def __init__(self,master):
		self.btn = tk.Button(master,text="Clicked to choose..")
		self.btn.grid(row=0,column=0)
		pass

class Geometry:
	def __init__(self,master):
		self.btn = tk.Button(master,text="Geometry Visulation..")
		self.btn.grid(row=0,column=0)
		pass


class DemoFrame:
	def __init__(self,app):
		#-----------控件布局---------------
		self.btn = tk.Button(app,text='Start simulation')
		self.btn.pack()
		self.lab1 = tk.Label(app,text='Frame one')
		self.lab1.pack()
		self.fram1 = tk.Frame(app)
		self.fram1.pack(anchor=tk.W)
		self.materials = Materials(self.fram1)
		self.lab2 = tk.Label(app,text='Frame two')
		self.lab2.pack()
		self.fram2 = tk.Frame(app)
		self.fram2.pack(anchor=tk.W)
		self.geometry = Geometry(self.fram2)
	pass

app = tk.Tk()
# mpl = FuncMPL("Gaussian function plot")
MyGUI = DemoFrame(app)
app.title('Demo Tkinter System')
app.geometry('800x600')
# app.configure(background='blue')
# app.iconbitmap('./25-1.ico')
app.mainloop()