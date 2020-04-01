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

class FuncMPL:
  """matplotlib window function"""

  def __init__(self, title):
    ## turn interactive mode on
    plt.ion()

    fig = plt.figure()
    fig.canvas.set_window_title(title)
    self.ax=plt.gca()
    # self.ax.set_color_cycle(['red', 'blue', 'green', 'pink'])
    xx = np.linspace(-1, 1, 100)
    yy = xx**2
    self.plot,=plt.plot(xx, yy, color='red',linestyle='-', linewidth=1.5)
    # Returns a tuple of line objects, thus the comma
    # self.real, = plt.plot(xx, yy, ls='-', lw=2)
    # self.imag, = plt.plot(xx, yy, ls='--', lw=2)
    # self.norm, = plt.plot(xx, yy, ls='-.', lw=4)
    # self.ax.set_ylim(-1.05, 1.05)
    plt.grid(b=True, which='major', color='g', linestyle='--')
    # plt.legend(['real', 'imag', 'norm', ], loc='upper left')
    self.ax.set_title('Radiation Damage Calculation code Systems', fontsize=12)
    plt.tight_layout()

class RadiationDamage:
	#-------构造函数--------
	def __init__(self,app):
		# self.mpl=mpl

		#------控件布局-------
		self.menu = tk.Menu(app)
		app.config(menu=self.menu)
		self.filemenu = tk.Menu(self.menu)
		self.menu.add_cascade(label='File',menu=self.filemenu)
		self.filemenu.add_command(label='New')
		self.filemenu.add_command(label='Open',command=self.inpopen)
		self.filemenu.add_separator()
		self.filemenu.add_command(label='Exit',command=app.quit)

		self.helpmenu = tk.Menu(self.menu)
		self.menu.add_cascade(label='Help',menu=self.helpmenu)
		self.helpmenu.add_command(label='About')

		# self.lab1 = tk.Label(app,text='Hello World!')
		# self.lab1.grid(row=0,column=0)

		self.montecarlo = tk.Frame(app)
		self.montecarlo.grid(row=0,column=0)

		# self.but = tk.Button(self.montecarlo,text='MCNP_inp',command=self.inpopen)
		# self.but.grid(row=0,column=0)
		self.labm = tk.Label(self.montecarlo,text='Monte Carlo Simulation')
		self.labm.grid(row=0,column=0)

		self.inp = tk.Text(self.montecarlo,bg='linen',cursor='arrow')
		self.inp.grid(row=1,column=0)

		self.btg= tk.Button(self.montecarlo,bg='cyan',text='Geometry Structure')
		self.btg.grid(row=2,column=0)

		self.bts = tk.Button(self.montecarlo,bg='tomato',text='Start simulation')
		self.bts.grid(row=3,column=0)

		self.post_calc = ttk.Frame(app,borderwidth=1)
		self.post_calc.grid(row=1,column=0)

		self.labp = tk.Label(self.post_calc,text='Radiation Damage Calculation')
		self.labp.grid(row=0,column=0)

		self.particle = ttk.Combobox(self.post_calc,width=10)
		self.particle['values'] = ('electron','neutron','gamma')
		self.particle.grid(row=1,column=0)
		self.particle.current(0)

		self.energy = ttk.Combobox(self.post_calc,width=10)
		self.energy['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
		self.energy.grid(row=2,column=0)
		self.energy.current(0)

		self.btn = tk.Button(self.post_calc,bg='SkyBlue1',text='Calculation',command=self.dpa_calculation)
		self.btn.grid(row=4,column=0)

		self.btn2 = tk.Button(self.post_calc,bg='coral',text='Plot',command=self.data_plot)
		self.btn2.grid(row=4,column=1)


		#----------计算结果-----------------------
		values = {"PKA Cross Section":"1",
		          "dpa Cross Section":"2",
		          "dpa":"3"}
		for (text,value) in values.items():
			ttk.Radiobutton(self.post_calc,text=text,value=value).grid(row=3,column=(int(value)-1))
		# self.rad1 = ttk.Radiobutton(self.post_calc,text='PKA cross section',variable=v)
		# self.rad1.grid(row=3,column=0)
		# self.rad2 = ttk.Radiobutton(self.post_calc,text='dpa cross section')
		# self.rad2.grid(row=3,column=1)
		# self.rad3 = ttk.Radiobutton(self.post_calc,text='dpa')
		# self.rad3.grid(row=3,column=2)

		
		# pass
    #-----------------------------------
    # 读取蒙特卡罗软件mcnp软件，并显示
    # 1.读取文件
    # 2.运行mcnp程序
    # 3.提取数据并绘制图像
    # 4.将数据转存后续计算
    #------------------------------------
	def inpopen(self):
		var = tk.StringVar()
		filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		try:
		    with open(filename,'r') as f:
			    line = f.readline()
			    while line:
				    var=line
				    self.inp.insert('end',var)
				    print(var)
				    line = f.readline()
		except IOError:
			print("Error:No such file!!")
		else:
			print("Successfully!!")
		print(filename)

	def dpa_calculation(self):
		var1 = tk.StringVar()
		var2 = tk.IntVar()
		var1 = self.particle.get()
		var2 = self.energy.get()
		print("Particle is: %s Energy is:%s MeV" %(var1,var2))


	def data_plot(self):
		self.mpl=FuncMPL("Radiation Damage")
		xx = np.linspace(-2, 2, 100)
		yy = np.exp(xx)
		self.mpl.ax.set_xlim(xx[0],xx[-1])
		self.mpl.ax.set_ylim(yy[0],yy[-1])
		self.mpl.plot.set_data(xx,yy)
		plt.draw()


app = tk.Tk()
# mpl = FuncMPL("Gaussian function plot")
MyGUI = RadiationDamage(app)
app.title('Radiation Damage Calculation code Systems')
app.geometry('800x600')
# app.configure(background='blue')
app.iconbitmap('./25-1.ico')
app.mainloop()