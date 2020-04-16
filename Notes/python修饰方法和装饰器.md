# Python进阶

实际开发中，为了完成较为复杂的任务往往需要多个函数配合，当一个函数中收到了数据为了让其他的函数中能够直接使用，很多人想到了使用全局变量来实现传递的功能，这虽然很方便，但是也会出现一个问题，例如：并发程序会出现对同一个全局变量操作的问题。

## 1.重点基础知识

**多继承以及MRO顺序**

1. 单独调用父类的方法

```python
class Parent(object):
    def __init__(self,name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')

class Son1(Parent):
    def __init__(self, name,age):
        # super().__init__(name)
        print('Son1的init开始被调用')
        self.age = age
        Parent.__init__(self,name)
        print('Son1的init结束被调用')

class Son2(Parent):
    def __init__(self, name,gender):
        # super().__init__(name)
        print('Son2的init开始被调用')
        self.gender = gender
        Parent.__init__(self,name)
        print('Son2的init结束被调用')

class Grandson(Son1,Son2):
    def __init__(self, name, age,gender):
        # super().__init__(name, age)
        print('Grandson的init开始被调用')
        Son1.__init__(self,name,age) #单独调用父类的初始化方法
        Son2.__init__(self,name,gender)
        print('Grandson的init结束被调用')

if __name__=="__main__":
    gs = Grandson('grandson',12,'男')
    print('姓名：',gs.name)
    print('年龄：',gs.age)
    print('性别：',gs.gender)

    print("*********多继承使用类名.__init__发生的状态******\n")
```

2. 多继承中super调用其所父类的被重写的方法

```python
class Parent(object):
    def __init__(self,name,*args,**kwargs): #为避免多继承报错，使用不定参数，接受参数
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')

class Son1(Parent):
    def __init__(self, name,age, *args,**kwargs):  #为避免多继承报错，使用不定参数，接受参数 
        # super().__init__(name)
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name, *args,**kwargs)  #为避免多继承报错，使用不定参数，接受参数 
        print('Son1的init结束被调用')

class Son2(Parent):
    def __init__(self, name,gender, *args,**kwargs):
        # super().__init__(name)
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name, *args,**kwargs)
        print('Son2的init结束被调用')

class Grandson(Son1,Son2):
    def __init__(self, name, age,gender):
        # super().__init__(name, age)
        # 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍
        #而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
        #super(Grandson,self).__init__(name,age,gender)
        print('Grandson的init开始被调用')
        super().__init__(name,age,gender)
        print('Grandson的init结束被调用')
print("*********多继承使用super().__init__发生的状态******\n")
print(Grandson.__mro__)
if __name__=="__main__":
    gs = Grandson('grandson',12,'男')
    print('姓名：',gs.name)
    print('年龄：',gs.age)
    print('性别：',gs.gender)

    print("*********多继承使用类名.__init__发生的状态******\n")
```

运行结果：

```
*********多继承使用super().__init__发生的状态******

(<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
Grandson的init开始被调用
Son1的init开始被调用
Son2的init开始被调用
parent的init开始被调用
parent的init结束被调用
Son2的init结束被调用
Son1的init结束被调用
Grandson的init结束被调用
姓名： grandson
年龄： 12
性别： 男
*********多继承使用类名.__init__发生的状态******
```

`*args`以元组的形式保存参数，`**kwargs`以字典的形式传递关键字参数

```python
def test2(a,b,*args,**kwargs):
    print("-----test two-------")
    print(a)
    print(b)
    print(args)
    print(kwargs)

def test(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    test2(a,b,args,kwargs)

test(11,22,33,44,55,66,name="laowang",age=25)
```

运行结果：

```
11
22
(33, 44, 55, 66)
{'name': 'laowang', 'age': 25}
-----test two-------
11
22
((33, 44, 55, 66), {'name': 'laowang', 'age': 25})
{}
```

```python
def test2(a,b,*args,**kwargs):
    print("-----test two-------")
    print(a)
    print(b)
    print(args)
    print(kwargs)

def test(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    test2(a,b,*args,**kwargs)

test(11,22,33,44,55,66,name="laowang",age=25)
```

运行结果：

```
11
22
(33, 44, 55, 66)
{'name': 'laowang', 'age': 25}
-----test two-------
11
22
(33, 44, 55, 66)
{'name': 'laowang', 'age': 25}
```

3. 单继承中super
   * `super()__init__`相当于类名.\_\_init\_\_，在单继承上用法基本无差别
   * 但在多继承上有区别，super方法能保证每个父类的方法执行一次，而使用类名的方法会导致方法被执行多次，具体看前面的例子。
   * 多继承时，使用super方法，对父类的传参数，应该是由于python中的super的算法导致的原因，必须把参数全部传递，否则会报错。
   * 单继承时，使用super方法，则不能全部传递，只能传父类方法所需的参数，否则会报错。
   * 多继承时，相对于使用类名.\_\_init\_\_方法，要把每个父类全部写一遍，而使用super方法，只需写一句话使执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因。

面试题：

以下的代码的输出将是什么？说出答案并解释

```python
class Parent(object):
    x=1

class Child1(Parent):
    pass

class Child2(Parent):
    pass
print(Child1.__mro__)
print(Parent.x,Child1.x,Child2.x)
Child1.x = 2
print(Parent.x,Child1.x,Child2.x)
Parent.x = 3
print(Parent.x,Child1.x,Child2.x)

```

结果为：

```
(<class '__main__.Child1'>, <class '__main__.Parent'>, <class 'object'>)
1 1 1
1 2 1
3 2 3
```

### 1.1再论静态方法和类方法

**1.类属性、实例属性**

它们在定义和使用中有所区别，其最本质的区别是内存中保存的位置不同。

* 实例属性属于对象
* 类属性属于类

```python
class Province(object):
    #类属性
    country='中国'

    def __init__(self,name):
        #实例属性
        self.name = name

# 创建一个实例对象
obj = Province('山东省')
# 直接访问实例属性
print(obj.name)
# 直接访问类属性
Province.country
```

由以上代码可知【实例属性需要通过对象来访问】【类属性通过类访问】，在使用上可以看出实例属性和类属性的归属是不同的。

1.`__new__`---->创建对象，通俗点说：有个内存空间

2.`__init__`---->对刚刚申请的空间进行初始化

* 类属性在内存中只保存一份
* 实例属性在每个对象中都要保存一份

**2.实例方法、静态方法和类方法**

方法包括：实例方法、静态方法和类方法，三种方法在内存中都归属于类，区别在于调用方式不同。

* 实例方法：由对象调用：至少一个self参数；执行实例方法时，自动将调用该方法的对象赋值给self；
* 类方法：由类调用，至少一个cls参数；执行类方法时，自动调用该方法的类赋值给cls；
* 静态方法：由类调用，无默认参数；

```python
class Foo(object):
    def __init__(self,name):
        self.name = name

    def ord_func(self):
        """ 定义实例方法，至少有一个self参数"""
        print(self.name)
        print('实例方法')

    @classmethod
    def class_func(cls):
        """定义类方法，至少有一个cls参数"""
        print('类方法')

    @staticmethod
    def static_func():
        """定义静态方法，无默认参数"""
        print('静态方法')

f = Foo("中国")
#调用实例方法
f.ord_func()

# 调用类方法
Foo.class_func()

# 调用静态方法

Foo.static_func()

```

运行结果：

```
中国
实例方法
类方法
静态方法
```

**对比**

* 相同点：对于所有的方法而言，均属于类，所以在内存中只存在一份
* 不同点：方法调用者不同、调用方法时自动传入的参数不同

### 1.2 property属性

**1.什么是property属性**

一种用起来像是使用的实例属性一样的特殊属性，可以对应于某个方法

```python
class Foo:
    def func(self):
        pass

    # 定义property属性
    @property
    def prop(self):
        pass
class Good:

    @property
    def size(self):
        return 100

#--------------调用-------------
foo_obj = Foo()
foo_obj.func()  # 调用实例方法
foo_obj.prop    #调用property属性

g = Good()
ret = g.size
print(ret)
```

**property属性的定义和调用要注意以下几点：**

* 定义时，在实例方法的基础上添加`@property`装饰器，并且仅有一个self参数；
* 调用时无需括号

**2.简单的实例**

> 对于京东商城中显示电脑主机的列表页面，每次请求不可能把数据库中的所有内容都显示到页面上，而是通过分页局部显示，所有在向数据库中请求数据时就要显示的指定获取从第m条到第n条的所有数据 这个分页的功能包括：
>
> * 根据用户请求的当前页和总数据条数计算出m和n
> * 根据m和n去数据库中请求数据

```python
class Page:
    def __init__(self,current_page):
        # 用户当前请求的页码（第一页、第二页）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page-1)*self.per_items
        return val

    @property
    def end(self):
        val = self.current_page*self.per_items
        return val

#--------调用------------------------
p = Page(1)
p.start
p.end
print(p.start)
print(p.end)


```

**从上述可见**

* Python的property属性的功能是：property属性内部进行的一系列的逻辑计算，最终将计算结果返回。

**3.property属性的两种方式**

* 装饰器 即：在方法上应用装饰器；
* 类属性 即：在类中定义值为property对象的类属性

**3.1 装饰器方式**

在类的实例方法上应用@property装饰器

Python中的类由`经典类`和`新式类`，`新式类`的属性比`经典类`的属性丰富。（如果类继承object，就是新式类）

**经典类，具有一种@property装饰器**

```python
class Goods:
    @property
    def price(self):
        return "laowang"

#-------调用----------------
obj = Goods()
result = obj.price  #自动执行 @property修饰的price方法，并获取方法的返回值
print(result)

```

**新式类，具有三种@property装饰器**

```python
class Goods:
    """
    python3默认继承object类
    只有python3中才有@xx.setter @xx.deleter
    """
    
    @property
    def price(self):
        print('@property')


    @price.setter
    def price(self,value):
        print('@price.setter')

    @price.deleter
    def price(self):
        print('@price.deleter')

#-------调用----------------
obj = Goods()
obj.price  #自动执行 @property修饰的price方法，并获取方法的返回值
obj.price = 123
print(obj.price)
del obj.price


```

**注意**

* 经典类中的属性只有一种访问方式，其对应被@property修饰的方法
* 新式类中的属性有三种访问方式，并分别对应了三个被@property、@方法名.setter、@方法名.deleter

**实例**

```python
class Goods:
    """
    python3默认继承object类
    只有python3中才有@xx.setter @xx.deleter
    """
    def __init__(self):
        self.val = val
        self.original_price = 100
        self.discount = 0.8
    
    @property
    def price(self):
        new_price  = self.original_price*self.discount
        return new_price


    @price.setter
    def price(self,value):   
        self.original_price=value

    @price.deleter
    def price(self):
        del self.original_price

#-------调用----------------
obj = Goods()
obj.price  #获取商品价格
print(obj.price)
obj.price = 200  #修改商品价格
print(obj.price)
del obj.price   #删除商品原价
```































## 2.Python修饰符

**classmethod修饰符**

**classmethod**修饰符对应的函数不需要实例化，不需要self参数，但第一个参数需要是表示自身类的cls参数，可以调用类的属性、类的方法、实例化对象等。

```python
class A(object):
    bar=1
    # def __init__(self,value,name):
    #     self.value = value
    #     self.name = name
    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print("func2")
        print(cls.bar)
        cls().func1()   #调用foo方法
        # print(cls.value)
        # print(cls.name)
if __name__ =='__main__':
    A().func2()      #不需要实例化
```

```python
from datetime import date
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year-year)

    # A static method to check if a Person is adult or not
    @staticmethod
    def isAdult(age):
        return age>18

if __name__ =='__main__':
    person1 = Person('mayank',21)
    person2 = Person.fromBirthYear('mayank',1996)
    print(person1.age)
    print(person2.age)
    print(Person.isAdult(22))
```

































































































































