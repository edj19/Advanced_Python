![1585529700578](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1585529700578.png)

# Python项目包管理

​        此篇记录如何打包一个简单的Python项目，展示如何添加必要的文件和结构来创建软件包，以及如何上传到Python软件包索引。路过记得点赞呀，整理不易，且行且珍惜！

## 1 准备工作

首先注册PyPl账号和TestPyPI账户,对于前期项目管理、修改和查看可通过TestPyPI来管理，最后项目完整版的发布就可以上传到PyPI来实现，相应的网站注册如下：

* [TestPyPI](https://test.pypi.org/)
* [PyPI](https://pypi.org/)

接着在Pycharm下新建项目，项目包含的结构如下：

![1585552975183](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1585552975183.png)

**setup.py**文件是setuptools的构建脚本，它告诉项目的名称、版本和你代码文件的信息，对于其中setup()的一些参数或者声明信息，随着深入后面再做讲解，对于刚开始入门的复制下面内容并做相应的修改就行，里面的内容也是非常清晰明了的：

```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```

对于上传的Python包**LICENSE**是非常重要的，对于license具体的选择可参考相应的网站，对于刚开始学习的下面的MIT协议内容复制粘贴就好：

```
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

相应的**README.md**文件是利用markdown语法写的对自己项目的介绍，以便别人可以更好的理解你的项目：

```
# Example Package Test

This is a simple example package.
Have fun for coding!
```

对于example.py文件就写一个画图的测试函数作为测试，相应的代码如下：

```python
import numpy as np
import matplotlib.pylab as plt

def plot_figure(n):
    x = [i for i in range(n)]
    y = np.sqrt(x)
    plt.plot(x,y,'bo--')
    plt.show()
```

经过上面的操作就编写完成了，接下来就开始构建项目了！

## 2.开始构建项目

安装必要的python包：setuptools wheel twine

```python
python3 -m pip install --user --upgrade setuptools wheel
python3 -m pip install --user --upgrade twine
```

在项目目录下中启动cmd命令行，对项目进行打包处理：

```python
python3 setup.py sdist bdist_wheel
```

![1585532445162](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1585532445162.png)

通过运行上述命令后再次查看目录情况，打包已经完成，相应的目录结构如下图所示：

![1585553221686](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1585553221686.png)

## 3 上传项目

在前期构建测试阶段先上传TestPyPI上进行测试，cmd下运行下面语句：

```python
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

![1585532827799](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1585532827799.png)

![1585532992483](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1585532992483.png)

相应的可登陆自己的TestPyPI进行项目查看，如图所示，接下来就可以安装example_test包来测试了。

对于前期软件包的测试，建议用虚拟环境Virtualenv下开展，相应的步骤如下，首先安装必要的包：

```shell
pip install virtualenv
```

然后安装下面的步骤启动虚拟环境（Windows版)

```shell
mkdir virtualprojects
cd virtualprojects
virtualenv testenv   #初始化化虚拟环境
cd testenv/Scripts
activate             #启动虚拟环境
```

然后在该虚拟环境下安装我们上传到TestPyPI的example_test包：

```powershell
pip install -i https://test.pypi.org/simple/ example-test
```

接下来就是启动python环境导入包进行测试：

```
python
>>> import exampe_test  #okay
>>> from example_test.example import *    #okay
>>plt.figure(10)
```

运行后就可以做出$\sqrt(x)$的函数图像了，成功了！

当你打算发布自己的Python项目到PyPI时就可以直接运行下面的命令：

```
python3 -m twine upload dist/*
```

然后像安装numpy一样在自己电脑上安装包就可以了，好了终于讲完了，记得路过点赞呀，整理不易，且行且珍惜！





