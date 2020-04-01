license__ = "GPL"

import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,scrolledtext
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

class Materails:
	def __init__(self,master):
		self.master = master
		self.lmc = tk.Label(master,text='This is test multi class')
		self.lmc.grid(row=0,column=0)
		self.bmc = tk.Button(master,text='Please click me!!',bg='blue')
		self.bmc.grid(row=1,column=0)
		
	pass

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
		self.tabControl = ttk.Notebook(app)

		self.montecarlo = ttk.Frame(self.tabControl)
		self.tabControl.add(self.montecarlo,text='Transport Calculations')

		self.radiation = ttk.Frame(self.tabControl)
		self.tabControl.add(self.radiation,text='Radiation Damage')

		self.tabControl.pack(expand=1,fill="both")


		# self.but = tk.Button(self.montecarlo,text='MCNP_inp',command=self.inpopen)
		# self.but.grid(row=0,column=0)
		self.labm = tk.Label(self.montecarlo,text='Monte Carlo Simulation',font=("Helvetica",28),
			                 fg='blue')
		self.labm.pack()

		# self.inp = tk.Text(self.montecarlo,bg='linen',cursor='arrow')
		# self.inp.grid(row=1,column=0)
		self.geo = tk.Frame(self.montecarlo)
		self.geo.pack(anchor=tk.W)

		self.lgeo = tk.Label(self.geo,text='Geometry Structure',font=("Helvetica",18),
			                 fg='deepskyblue')
		self.lgeo.grid(row=0,column=0,sticky=tk.W)

		self.btg= tk.Button(self.geo,bg='deepskyblue',text='Geometry Structure')
		self.btg.grid(row=1,column=0,sticky=tk.W)


		self.lmat = tk.Label(self.geo,text='Materials',font=("Helvetica",18),
			                 fg='deepskyblue')
		self.lmat.grid(row=3,column=0,sticky=tk.W)

		self.bmc= tk.Button(self.geo,bg='deepskyblue',text='Geometry Structure')
		self.bmc.grid(row=1,column=0,sticky=tk.W)

		self.scotext = scrolledtext.ScrolledText(self.geo,height=10)
		for i in range(5):
			self.scotext.insert(tk.END,"This is line number "+str(i)+'\n')
		self.scotext.grid(row=4,column=0)


		self.lsour = tk.Label(self.geo,text='Source Definition',font=("Helvetica",18),
			                 fg='deepskyblue')
		self.lsour.grid(row=6,column=0,sticky=tk.W)

		self.lmessage = tk.Label(self.geo,text='Tallys Information Visualization',font=("Helvetica",18),
			                 fg='deepskyblue')
		self.lmessage.grid(row=7,column=0,sticky=tk.W)

		self.bts = tk.Button(self.geo,bg='deepskyblue',text='Start simulation')
		self.bts.grid(row=8,column=0,sticky=tk.W)

		self.mas = tk.Frame(self.montecarlo)
		self.mas.pack(anchor=tk.W)

		self.add_material()

		# self.post_calc = ttk.Frame(app,borderwidth=1)
		# self.post_calc.grid(row=1,column=0)

		self.labp = tk.Label(self.radiation,text='Radiation Damage Calculation',font=("Helvetica",28),
			                 fg='blue')
		self.labp.grid(row=0,column=0)

		self.particle = ttk.Combobox(self.radiation,width=10)
		self.particle['values'] = ('electron','neutron','gamma')
		self.particle.grid(row=1,column=0)
		self.particle.current(0)

		self.energy = ttk.Combobox(self.radiation,width=10)
		self.energy['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
		self.energy.grid(row=2,column=0)
		self.energy.current(0)

		self.btn = tk.Button(self.radiation,bg='SkyBlue1',text='Calculation',command=self.dpa_calculation)
		self.btn.grid(row=4,column=0)

		self.btn2 = tk.Button(self.radiation,bg='coral',text='Plot',command=self.data_plot)
		self.btn2.grid(row=4,column=1)


		#----------计算结果-----------------------
		values = {"PKA Cross Section":"1",
		          "dpa Cross Section":"2",
		          "dpa":"3"}
		for (text,value) in values.items():
			ttk.Radiobutton(self.radiation,text=text,value=value).grid(row=3,column=(int(value)-1))
		# self.rad1 = ttk.Radiobutton(self.post_calc,text='PKA cross section',variable=v)
		# self.rad1.grid(row=3,column=0)
		# self.rad2 = ttk.Radiobutton(self.post_calc,text='dpa cross section')
		# self.rad2.grid(row=3,column=1)
		# self.rad3 = ttk.Radiobutton(self.post_calc,text='dpa')
		# self.rad3.grid(row=3,column=2)

		
		# pass
	#--------------------------------------------

	#--------------------------------------------
	def add_material(self):
		mat = Materails(self.mas)
		pass
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