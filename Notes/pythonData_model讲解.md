# Python Data model的学习笔记

参考教程-Python进阶版：

[Python3.8中文教程](https://docs.python.org/zh-cn/3/)

* [Python语言参考](https://docs.python.org/zh-cn/3/reference/index.html)

[Python3.8英文教程](https://docs.python.org/3/reference/index.html)



## 1 对象-值-类型

对象是Python中对数据的抽象，每个对象都有各自的编号、类型和值。一个对象被创建后，它的*编号*就绝不会改变，可以理解为该对象在内存中的地址。'**is**'运算符可以比较两个对象的编号是否相同；**id()**函数能返回一个代表其编号的整型数。



实例方法

实例方法结合类、类实例和任何可调用对象（通常为用户定义函数）

特殊的只读类型：`__self__ `为类实例对象本身，`__func__`为函数对象；`__doc__`为方法的文档；`__name__`为方法名称；`__module__`为方法所属模块的名称，没有则为None.

## 2 特殊方法名称

一个类可以通过定义具有特殊名称的方法来实现特殊语法所引发的特定操作（例如算数运算或下标与切片）。这是Python实现*操作符重载*的方式，允许每个类自行定义基于操作符的特定行为。例如，如果一个类定义了名为<font color=blue>`__getitem__()`</font>的方法，并且`x`为该类的一个实例，则`x[i]`基本就等同于`type(x).__getitem__(x,i)`，除非有说明例外的情况，在没有定义适当的方法的情况下尝试执行一种操作将引发一个异常（通常为<font color=blue>AttributeError</font>或<font color=blue>TypeError</font>）。

### 2.1 基本定制

object.\_\_**new**\_\_(cls[,...])

调用以创建一个*cls*类的新实例，<font color=blue>\_\_new\_\_（）</font>是一个静态方法



object.\_\_**init**\_\_(self[,...])



object.\_\_**del**\_\_(self)



<font color=red size=5>1-改变对象实例的打印或显示输出，更加具有可读性</font>

object.\_\_**repr**\_\_(self)

该方法返回一个实例的代码表示形式，通常用来重新构造这个实例由于<font color=blue>repr()</font>内置函数调用以输出一个对象的“官方”字符串表示

object.\_\_**str**\_\_(self)

通过<font color=blue>str(object)</font>以及内置函数<font color=blue>format()</font>和<font color=blue>print()</font>调用以生成一个对象的“非正式”或格式良好的字符串表示，返回值必须为一个<font color=blue>字符串</font>对象。

注：自定义`__repr__`和`__str__()`通常是很好的习惯，可以简化调试和实例输出

```python
class Pair(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r},{0.y!r})'.format(self)
        # return 'Pair(%f %f)'%(self.x,self.y)
    def __str__(self):
        return '({0.x!s},{0.y!s})'.format(self)

if __name__ =='__main__':
    p = Pair(3,4)
    print(p)
    #>>>(3,4)
```

<font color=red size=5>2-自定义字符串的格式化</font>

object.\_\_**format**\_\_(self,format_spec)

通过**format()**函数和字符串方法使得一个对象能支持自定义的格式化

为了自定义字符串的格式化，需要在类上面定义`__format__()`方法，该方法给Python的字符串格式化功能提供了一个钩子，这里需要着重强调的是格式化代码的解析工作完全由类自己决定。代码如下：

```python
class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self,code):
        if code=='':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

if __name__ =='__main__':
    d = Date(2012,12,25)
    print('The date is {:mdy}'.format(d,'mdy'))
    #>>>The date is 12/25.=/2012
```

**富比较方法**

object.\_\_**lt**\_\_(self,other)             x<y

object.\_\_**le**\_\_(self,other)           x<=y

object.\_\_**eq**\_\_(self,other)          x==y

object.\_\_**ne**\_\_(self,other)          x!=y

object.\_\_**gt**\_\_(self,other)           x>y

object.\_\_**ge**\_\_(self,other)          x>=y



object.\_\_**hash**\_\_(self)

通过内置函数<font color=blue>hash()</font>调用对哈希集的成员进行操作，属于哈希集的类型包括<font color=blue>set</font>、<font color=blue>frozenset</font>以及<font color=blue>dict</font>。<font color=blue>\_\_hash\_\_()</font>应该返回一个整数，对象比较结果相同所需的唯一特征属性是其具有相同的哈希值，建议把参与比较的对象全部组件的哈希值混在一起，即将它们打包为一个元组并对该元组做哈希运算。

object.\_\_**bool**\_\_(self)

### 2.2自定义属性访问

可以定义下列方法来自定义对类实例属性访问（`x.name`的使用、赋值或删除）的具体含义。

object.\_\_**getattr**\_\_(self,name)

object.\_\_**getattribute**\_\_(self,name)

object.\_\_**setattr**\_\_(self,name)

object.\_\_**delattr**\_\_(self,name)

object.\_\_**dir**\_\_(self,name)

#### 2.2.1 自定义模块属性访问



#### 2.2.2 实现描述器

一般地一个描述器是一个包含“绑定行为”的对象，对其属性的存取被描述器协议中定义的方法覆盖，这些方法有：<font color=blue>\_\_get\_\_()</font>，<font color=blue>\_\_set\_\_()</font>和<font color=blue>\_\_delete\_\_()</font>。如果某个对象中定义了这些方法中的任意一个，那么这个对象就可以被称为一个描述器。

属性访问的默认行为是从一个对象的字典中获取、设置或删除属性。例如，`a.x`的查找顺序会从`a.__dict__['x‘]`开始，然后是`type(a).__dict__['x']`，接下来依次查找`type(a)`的基类，不包括元类。如果找到的值是定义了某个描述器方法的对象，则Python可能会重载默认行为并转而发起调用描述器方法。这具体发生在优先级链的哪个环节则要根据所定义的描述器方法及其被调用的方式来决定。

描述器是一个强大而通用的协议，它们是特征属性、方法静态方法、类方法和<font color=blue>super()</font>背后的实现机制，描述器简化了底层的C代码并为Python的日常程序提供了一组灵活的新工具。



```python
#---------------描述器--------------------------
class RevealAccess(object):
    def __init__(self,initval=None,name='var'):
        self.val = initval
        self.name = name

    def __get__(self,obj,objtype):
        print('Retrieving',self.name)
        return self.val
    def __set__(self,obj,val):
        print('Updating',self.name)
        self.val = val
class MyClass(object):
    x = RevealAccess(10,'variable x')
    y = 5


if __name__ =='__main__':
    m = MyClass()
    print(m.x)
    m.x = 20
    print(m.x)

```



























