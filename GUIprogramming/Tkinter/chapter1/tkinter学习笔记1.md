这是学习tkinter的笔记，由于是笔记一般以代码展示为主，毕竟我们每个人都希望尽快解决问题，而不是看我扯闲话，废话不多说，开始**tkinter**的学习之路。

# 1 tkinter初见

Tkinter模块是Python的标准Tk GUI工具包的接口，下面为第一个**tkinter**的Hello World界面显示：

![1580121310665](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1580121310665.png)

具体的代码如下：

```python
import tkinter as tk


app = tk.Tk()
app.title("Tkinter Learning Notes")
app.geometry('800x600')

label =tk.Label(app,text='Hello World')
label.pack()

app.mainloop()
```

我们可以在**控件类型**处定义控件布局，以此达到我们的条件。

![1580121457525](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1580121457525.png)

# 2 tkinter常见控件

| 控件         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| Button       | 按钮控件；在程序中显示按钮                                   |
| Canvas       | 画布控件；显示图形元素如线条或文本                           |
| Checkbutton  | 多选框控件；用于在程序中提供多项选择框                       |
| Entry        | 输入控件；用于显示简单的文本内容                             |
| Frame        | 框架控件；在屏幕上显示一个矩形区域，多用来作为容器           |
| Label        | 标签控件；可以显示文本和位图                                 |
| Listbox      | 列表框控件；在Listbox窗口小部件是用来显示一个字符列表给用户  |
| Menubutton   | 菜单按钮控件，用于显示菜单项                                 |
| Menu         | 菜单控件；显示菜单栏，下拉菜单和弹出菜单                     |
| Message      | 消息控件；用来显示多行文本，与label比较类似                  |
| Radiobutton  | 单选按钮控件；显示一个单选的按钮状态                         |
| Scale        | 范围控件；显示一个数值刻度，为输出限定范围的数字区间         |
| Scrollbar    | 滚动条控件，当内容超过可视化区域时使用，如列表框             |
| Text         | 文本控件；用于显示多行文本                                   |
| Toplevel     | 容器控件；用来提供一个单独的对话框，和Frame比较类似          |
| Spinbox      | 输入控件；与Entry类似，但是可以指定输入范围值                |
| PanedWindow  | PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件 |
| LabelFrame   | labelframe是一个简单的容器控件，常用与复杂的窗口布局         |
| tkMessageBox | 用于显示你应用程序的消息框                                   |



## 2.1 tkinter控件几何

tkinter控件几何位置的管理方法：包、网格、位置

| 几何方法 | 描述 |
| -------- | ---- |
| pack()   | 放置 |
| grid()   | 网格 |
| place()  | 位置 |

## 2.2 控件基本属性

| 属性      | 描述     |
| --------- | -------- |
| Dimension | 控件大小 |
| Color     | 控件颜色 |
| Font      | 控件字体 |
| Anchor    | 锚点     |
| Relief    | 控件样式 |
| Bitmap    | 位图     |
| Cursor    | 光标     |



# 3 基本实例

对于Tkinter的其他控件和方法，读者可以根据自己的需求自行进行修改补充，方法都是类似的，这里重点介绍几个重要[我认为的...]的控件实例，其他都是类似的。

## 实例一：Label,Button,Entry

代码如下：

```python
import tkinter as tk
from tkinter import filedialog  #打开文件并显示内容

app = tk.Tk()
app.title("Tkinter Learning Notes")
app.geometry('400x300')

#-----标签----------
lb1 = tk.Label(app,text='I am Label')
lb1.grid(column=0,row=0)

#-----按钮----------
# btn = tk.Button(app,text="Click me",bg='orange',fg='red',command=clicked)
btn = tk.Button(app,text="Click me",command=clicked)
btn.grid(column=1,row=0)

#-------输入控件-----------------
txt = tk.Entry(app,width=10)
txt.grid(column=0,row=1)

#--------打开某一文件并读取内容-----------
btn_file = tk.Button(app,text="Structure file",command=fileread)
btn_file.grid(column=2,row=0)


app.mainloop()

```

最终的效果图如下：

![1580126767237](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1580126767237.png)

## 实例二：几何位置pack(),grid(),place()

* pack()方法：利用**fill**,**expand**和**side**参数控制几何

具体代码如下：

```python
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

```

将很多部件一个一个放在上方(tk.TOP)，并占据整个框架(tk.BOTH)，相关参考资料可见：[pack() method](https://www.tutorialspoint.com/python/tk_pack.htm)

最终效果如下图所示：

![1580127327904](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1580127327904.png)

* grid()方法：将控件放置在二维表中，通过行(**row**)和列(**column**)来控制

具体实现代码如下：

```python
# import tkinter module 
import tkinter as tk

# creating main tkinter window/toplevel 
master = tk.Tk()
master.title("Tkinter Learning Notes") 

# this wil create a label widget 
l1 = tk.Label(master, text = "First:") 
l2 = tk.Label(master, text = "Second:") 

# grid method to arrange labels in respective 
# rows and columns as specified 
l1.grid(row = 0, column = 0, sticky = tk.W, pady = 2) 
l2.grid(row = 1, column = 0, sticky = tk.W, pady = 2) 

# entry widgets, used to take entry from user 
e1 = tk.Entry(master) 
e2 = tk.Entry(master) 

# this will arrange entry widgets 
e1.grid(row = 0, column = 1, pady = 2) 
e2.grid(row = 1, column = 1, pady = 2) 

# infinite loop which can be terminated by keyboard 
# or mouse interrupt 
master.mainloop() 

```

对于grid()的其他方法，可以参考如下链接：[grid() method](https://web.archive.org/web/20190521203213/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/grid.html)

实现的效果如下所示：

![1580134574347](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1580134574347.png)

* place()方法：通过设定位置和窗口大小(绝对值或相对值实现)

```python
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
```

对于place()方法的具体参数介绍可参考如下：[place method()](https://www.tutorialspoint.com/python/tk_place.htm)

具体效果图如下：

![1580137731834](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1580137731834.png)

## 实例三：Frame控件

由于我们需要在自己的界面上设计不同的区域来完成不同的工作，我认为Frame是非常有必要学习的。具体代码如下：

```python
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
```

对于Frame的相关参数的设定可参考如下链接：[Frame() class](https://web.archive.org/web/20190528185415/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/frame.html)

具体实现效果如下：

![1580135824299](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1580135824299.png)

























