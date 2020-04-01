import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.label = tk.Label(self.frame,text="How to open a new window")
        self.label.grid(row=0,column=0)
        self.button1 = tk.Button(self.frame, text = 'Please clicke me! New Window',bg='cyan',
                                  width = 30, command = self.new_window)
        self.button1.grid(row=1,column=0)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.lna = tk.Label(self.frame,text="Happy,you have opend a new window!")
        self.lna.grid(row=0,column=0)
        self.quitButton = tk.Button(self.frame, text = 'Quit',bg='tomato', width = 25, command = self.close_windows)
        self.quitButton.grid(row=1,column=0)
     
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.title("Open a new window!")
    root.geometry('400x300') 
    root.mainloop()

if __name__ == '__main__':
    main()