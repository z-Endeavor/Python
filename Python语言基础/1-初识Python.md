# 初识Python


### Python简介

#### Python历史

 1. 1989年圣诞节：Guido von Rossum开始写Python语言的编译器。
 2. 1991年2月：第一个Python编译器（同时也是解释器）诞生，它是用C语言实现的（后面），可以调用C语言的库函数。在最早的版本中，Python已经提供了对“类”，“函数”，“异常处理”等构造块的支持，还有对列表、字典等核心数据类型，同时支持以模块为基础来构造应用程序。
 3. 1994年1月：Python 1.0正式发布。
 4. 2000年10月16日：Python 2.0发布，增加了完整的垃圾回收，提供了对Unicode的支持。与此同时，Python的整个开发过程更加透明，社区对开发进度的影响逐渐扩大，生态圈开始慢慢形成。
 5. 2008年12月3日：Python 3.0发布，它并不完全兼容之前的Python代码，不过因为目前还有不少公司在项目和运维中使用Python 2.x版本，所以Python 3.x的很多新特性后来也被移植到Python 2.6/2.7版本中。

#### Python的优缺点

Python的优点很多，简单的可以总结为以下几点。

 1. 简单明了，学习曲线低，比很多编程语言都容易上手。
 2. 开放源代码，拥有强大的社区和生态圈，尤其是在数据分析和机器学习领域。
 3. 解释型语言，天生具有平台可移植性，代码可以工作于不同的操作系统。
 4. 对两种主流的编程范式（面向对象编程和函数式编程）都提供了支持。
 5. 代码规范程度高，可读性强，适合有代码洁癖和强迫症的人群。

Python的缺点主要集中在以下几点。

 1. 执行效率稍低，对执行效率要求高的部分可以由其他语言（如：C、C++）编写。
 2. 代码无法加密，但是现在很多公司都不销售卖软件而是销售服务，这个问题会被弱化。
 3. 在开发时可以选择的框架太多（如Web框架就有100多个），有选择的地方就有错误。

#### Python的应用领域

目前Python在Web应用后端开发、云基础设施建设、DevOps、网络数据采集（爬虫）、自动化测试、数据分析、机器学习等领域都有着广泛的应用。


### 安装Python解释器

想要开始Python编程，首先得在自己使用的计算机上安装Python解释器环境。官方的Python解释器是用C语言实现的，也是使用最为广泛的Python解释器，通常称之为CPython。除此之外，Python解释器还有Java语言实现的Jython、C#语言实现的IronPython以及PyPy、Brython、Pyston等版本。
Python可应用于多平台包括 Linux 和 Mac OS X。你可以通过终端窗口输入 "python" 命令来查看本地是否已经安装Python以及Python的安装版本。

#### Windows环境

可以在[Python官方网站](https://www.python.org/)下载到Python的[Windows安装程序](https://www.python.org/downloads/windows/)（exe文件）。安装过程最好勾选“Add Python 3.x to PATH”（将Python 3.x添加到PATH环境变量）并选择自定义安装，安装完成会看到“Setup was successful”的提示。

> 新手可以参考该[Python教程](https://zhuanlan.zhihu.com/p/111168324?from_voters_page=true)，比较详细完整。

#### Linux环境/MacOS环境

> 自己暂时没用到其他环境。


### 运行Python

#### 确认Python版本

可以Windows的命令行提示符中键入下面的命令。

    python --version

退出Python环境，ctrl+Z，接着回车即退出。

#### 编写Python源代码

可以用代码编辑器（Sublime、Visual Studio Code等高级文本编辑工具）编写Python源代码并用py作为后缀名保存该文件。

    print('hello, world!')

#### 运行程序
切换到源代码所在的目录并执行下面的命令，看看屏幕上是否输出了"hello, world!"。

    python hello.py

#### 代码中的注释

注释是编程语言的一个重要组成部分，用于在源代码中解释代码的作用从而增强程序的可读性和可维护性，当然也可以将源代码中不需要参与运行的代码段通过注释来去掉，这一点在调试程序的时候经常用到。注释在随源代码进入预处理器或编译时会被移除，不会在目标代码中保留也不会影响程序的执行结果。

 1. 单行注释 - 以#和空格开头的部分
 2. 多行注释 - 三个引号开头，三个引号结尾

注释示例如下：

	"""
	第一个Python程序 - hello, world!
	Author: zkc
	"""
	print('Hello, World!')
	# print("This is single line comment")


### 练习

 1. 在Python交互式环境中输入下面的代码并查看结果，请尝试将看到的内容翻译成中文。
 
代码如下：

    import this

> 输入上面的代码，在Python的交互式环境中可以看到Tim Peter撰写的 “ Zen of Python”（Python之禅），里面讲述的道理不仅仅适用于Python，也适用于其他编程语言。

> Beautiful is better than ugly.  Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!

> 优美比丑陋好。清晰比晦涩好。简单比复杂好。复杂比错综复杂好。 扁平比嵌套好。稀疏比密集好。可读性很重要。 特殊情况也不应该违反这些规则。但现实往往并不那么完美。异常不应该被静默处理。 除非你希望如此。 遇到模棱两可的地方，不要胡乱猜测。 肯定有一种通常也是唯一一种最佳的解决方案。虽然这种方案并不是显而易见的，因为你不是Dutch 。现在开始做比不做好。不做比盲目去做好。如果一个实现方案难于理解，它就不是一个好的方案。如果一个实现方案易于理解，它很有可能是一个好的方案。命名空间非常有用，我们应当多加利用。

 
 2. 学习使用turtle在屏幕上绘制一个矩形。

> turtle是Python内置的一个非常有趣的模块，特别适合对计算机程序设计进行初体验。

代码如下：

    import turtle
    turtle.pensize(4)
	turtle.pencolor('red')

	turtle.forward(100)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(100)

	turtle.mainloop()

 3. 画个国旗
 4. 画个小猪佩奇
 
> 在代码目录中提供了画国旗和小猪佩奇的代码。可以大概参考代码思路流程。
