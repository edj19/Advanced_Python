import tkinter as tk


app = tk.Tk()
app.title('Tkinter Frame Learning')
app.geometry('400x300')

tk.Label(app,text='On the window').pack()

#-----创建一个Frame-----------
frm = tk.Frame(app)
frm.pack()

#-----在刚才Frame上继续创建小的Frame,大容器套小容器------
frm_1 = tk.Frame(frm)
frm_2 = tk.Frame(frm)

#-------放置相对位置-----------------
frm_1.pack(side='left')
frm_2.pack(side='right')

#--------在相应的容器上添加控件---------------
tk.Label(frm_1,text='on the frame 1').pack()
tk.Label(frm_1,text='on the frame 1 second').pack()
tk.Label(frm_2,text='on the frame 2').pack()


app.mainloop()