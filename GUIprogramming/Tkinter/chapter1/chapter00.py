import tkinter as tk


app = tk.Tk()
app.title("Tkinter Learning Notes")
app.geometry('800x600')

label =tk.Label(app,text='Hello World')
label.pack()

app.mainloop()