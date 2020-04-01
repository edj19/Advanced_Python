import tkinter as tk
from PIL import ImageTk,Image


class App(tk.Frame):
	def __init__(self,parent=None):
		super().__init__(parent)
		self.pack()
		self.frm1 = tk.Frame(self)
		self.frm1.grid(row=0,column=0)
		self.lab1 = tk.Label(self.frm1,text='标签一')
		self.lab1.grid(row=0,column=0)

		self.frm2 = tk.Frame(self)
		self.frm2.grid(row=1,column=0)

		self.setUI()

	def setUI(self):
		pass

if __name__ == '__main__':
	root = tk.Tk()
	MyGui = App(root)
	root.mainloop()