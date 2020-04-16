# Python面向对象三大特性

类提供了一种组合数据和功能的方法，创建一个新类意味着创建了一个新的对象类型，从而允许创建一个该类型的实例。

* Python是面向对象的语言，支持面向对象编程的三大特性：封装、继承、多态

接下来详细介绍三种特性：

最简单的类定义如下：

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

创建的类对象支持**属性引用**和**实例化**，下面的例子给出了相应的调用

```python
class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello World'
if __name__=='__main__':
    a = MyClass()
    print(a.i)
    print(a.f())
    print(a.__doc__)  #将返回所属类的文档字符串
```

实例化操作会创建一个空对象，许多类喜欢创建带有特定初始状态的自定义实例，可以定义一个名为<font color=blue>\_\_init\_\_()</font>的特殊方法：

```python
def __init__(self):
    self.data = []
```

当一个类定义了<font color=blue>\_\_init\_\_()</font>方法时，类的实例操作会自动为新创建的类实例调用<font color=blue>\_\_init\_\_()</font>，下面的例子定义了一个复数：

```python
class Complex(object):
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart

if __name__=='__main__':
    c = Complex(3.0,-4.5)
    print(c.r)
    print(c.i)
```

* 实例对象是属性引用：数据属性和方法
* 方法对象
* 实例变量用于每个实例的唯一数据，而类变量用于类的所有实例共享的属性和方法

```python
class Dog:
    kind='canine'    #class variable shared by all instances
    def __init__(self,name):
        self.name = name   #instance variable unique to each instance
if __name__=='__main__':
    d = Dog('Fido')
    e = Dog('Buddy')
    print(d.kind,e.kind)
    print(d.name,e.name)
```

## 1 继承

派生类的定义语法：

```python
class DerivedCClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

名称BaseClassName必须定义于包含派生类定义的作用域中，也允许其他任意表达式替代基类名称所在的位置。当构造类对象时，基类会被记住，此信息将被用来解析属性引用：如果请求的属性在类中找不到，搜索将转往基类中进行查找。如果基类本身也派生自其他某个类，则此规则将被递归地应用。

派生类可能会重载其基类的方法，因为方法在调用同一对象的其他方法时没有特殊权限，调用同一基类中定义的另一个方法的基类方法最终可能会调用覆盖它的派生类的方法。

下面是单继承的一个简单例子：

```python
class Person(object):
    # Constructor
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

# Inherited or Sub class
class Employee(Person):
    def isEmployee(self):
        return True
if __name__=='__main__':
    # -------继承测试--------------------------
    emp1 = Person("Geek1")
    print(emp1.getName(),emp1.isEmployee())

    emp2 = Employee("Greek2")
    print(emp2.getName(), emp2.isEmployee())

```

Python有两个内置函数可被用于继承机制：

- 使用<font color=blue>isinstance()</font>来检查一个实例的类型：`isinstance(obj,int)`仅会在`obj.__class__`为<font color=blue>int</font>或某个派生自<font color=blue>int</font>的类时为`True`
- 使用<font color=blue>issubclass()</font>来检查类的继承关系：`issubclass(bool,int)`为`True`，因为<font color=blue>bool</font>是<font color=blue>int</font>的子类，但是`issubclass(float,int)`为`False`，因为<font color=blue>float</font>不是<font color=blue>int</font>的子类。

<font color=red size=5>1-多继承</font>

Python也支持多继承，带有多个基类的类定义语句如下：

```python
class DerivedClassName(Base1,Base2,Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

对于多数应用来说，在最简单的情况下，你可以认为搜索从父类所继承属性的操作是深度优先、从左至右的，当层次结构中存在重叠时不会在同一个类中搜索两次。 因此，如果某一属性在 `DerivedClassName` 中未找到，则会到 `Base1` 中搜索它，然后（递归地）到 `Base1` 的基类中搜索，如果在那里未找到，再到 `Base2` 中搜索，依此类推。

下面为一个多继承的例子：

```python
# Python example to show working of multiple 
# inheritance 
class Base1(object): 
	def __init__(self): 
		self.str1 = "Geek1"
		print("Base1") 

class Base2(object): 
	def __init__(self): 
		self.str2 = "Geek2"		
		print("Base2") 

class Derived(Base1, Base2): 
	def __init__(self): 
		
		# Calling constructors of Base1 
		# and Base2 classes 
		Base1.__init__(self) 
		Base2.__init__(self) 
		print("Derived") 
		
	def printStrs(self): 
		print(self.str1, self.str2) 
		

ob = Derived() 
ob.printStrs() 
# Output
>Base1
>Base2
>Derived
>('Geek1','Geek2')

```

<font color=red size=5>2-私有变量</font>





<font color=red size=5>3-迭代器</font>

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

这种访问风格清晰、简洁又方便，迭代器的使用非常普遍使得Python成为一个统一的整体，而迭代器的幕后机制，就是给类添加迭代器行为，定义一个 [`__iter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 方法来返回一个带有 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法的对象。 如果类已定义了 `__next__()`，则 [`__iter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 可以简单地返回 `self`:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
if __name__=='__main__':
    #----------迭代器测试---------------
    rev = Reverse('spam')
    iter(rev)
    for char in rev:
        print(char)
```

<font color=red size=5>4-生成器</font>

[Generator](https://docs.python.org/zh-cn/3/glossary.html#term-generator) 是一个用于创建迭代器的简单而强大的工具。 它们的写法类似标准的函数，但当它们要返回数据时会使用 [`yield`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#yield) 语句。 每次对生成器调用 [`next()`](https://docs.python.org/zh-cn/3/library/functions.html#next) 时，它会从上次离开位置恢复执行（它会记住上次执行语句时的所有数据值）。 显示如何非常容易地创建生成器的示例如下:

```python
#----------生成器测试------------------------
def reverse(data):
	for index in range(len(data) - 1, -1, -1):
		yield data[index]
for char in reverse("glof"):
	print(char)
```

可以用生成器来完成的操作同样可以用前一节所描述的基于类的迭代器来完成。 但生成器的写法更为紧凑，因为它会自动创建 [`__iter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 和 [`__next__()`](https://docs.python.org/zh-cn/3/reference/expressions.html#generator.__next__) 方法。

另一个关键特性在于局部变量和执行状态会在每次调用之间自动保存。 这使得该函数相比使用 `self.index` 和 `self.data` 这种实例变量的方式更易编写且更为清晰。

**生成器表达式**

```python
x = sum(i*i for i in range(10))
print(x)

xvec = [10,20,30]
yvec = [7,5,3]
print(zip(xvec,yvec))
value = sum(x*y for x,y in zip(xvec,yvec))
print(value)

data = 'golf'
print(list(data[i] for i in range(len(data)-1,-1,-1)))
```





























