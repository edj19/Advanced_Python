import tkinter as tk

def frame(root,side):
	w = tk.Frame(root)
	w.pack(side=side,fill=tk.BOTH,expand=True)
	return w

def button(root,side,text,command=None):
	w = tk.Button(root,text=text,command = command)
	w.pack(side=side,fill=tk.BOTH,expand=True)
	return w

class Calculator(tk.Frame):
	def __init__(self):
		tk.Frame.__init__(self)
		self.pack(fill=tk.BOTH,expand=True)
		self.master.title('Simple Calculator')

		display = tk.StringVar()
		tk.Entry(self,relief=tk.SUNKEN,
			     textvariable=display).pack(side=tk.TOP,fill=tk.BOTH,expand=True)
		for key in ("123","456","789","-0."):
			keyF = frame(self,tk.TOP)
			for char in key:
				button(keyF,tk.LEFT,char,
					lambda w=display,s=' %s'%char:w.set(w.get()+s))
		opsF = frame(self,tk.TOP)
		for char in "+-*/=":
			if char == '=':
				btn = button(opsF,tk.LEFT,char)
				btn.bind('<ButtonRelease-1>',
					lambda e,s=self,w=display:s.calc(w),'+')
			else:
				btn = button(opsF,tk.LEFT,char,
					  lambda w=display,c=char:w.set(w.get()+' '+c+' '))
		clearF = frame(self,tk.BOTTOM)
		button(clearF,tk.LEFT,'Clr',lambda w=display:w.set(''))

	def calc(self,display):
		try:
			string = eval(display.get())
			display.set(string)
		except ValueError:
			display.set("ERROR")

if __name__ == '__main__':
	Calculator().mainloop()