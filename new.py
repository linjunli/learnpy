# 自定义求绝对值
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 求阶层
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(100))

# 汉诺塔
step = []
def move(n, a='A', b='B', c='C'):
    if n == 1:
        step.append(a+"===>>>"+c)
        return print(a,'===>>>', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
# N = input('step num:')
# if not isinstance(N, (int,float)):
#     raise TypeError('input type only int or float')
# move(int(N))
move(5)
print("need",len(step),step)

# python切片功能slice
L = ['A', 'B', 'C', 'D', 'E']
print('abcdefg'[:3])
print(L[1:3])
print(L[-2:-1])

# 特殊迭代
d = {'a': 1,'b': 2, 'c': 3}
for key in d:
    print('key = ',key)

for value in d.values():
    print('value = ',value)

for key,value in d.items():
    print('key = ',key,' value = ',value)

for x,y in [(1,1), (2,4), (3,8), (4,16)]:
    print(x,y)

# 列表生成式
listRange = [x * x for x in range(1,11)]
print(listRange)
listPai = [m + n for m in 'ABC' for n in 'XYZ']
print(listPai)
isStr = isinstance('xyz', str)
print(isStr)

# 生成器generator
# 列表生成器list
Lis = [x * x for x in range(10)]
print(Lis)
# generator
genera = (x * x for x in range(10))
print(genera)
for n in genera:
    print(n)
# map对list每个元素做相同运算
def f(x):
    return x * x
r = map(f, list(range(10)))
print(list(r))

# 斐波那契数列
# 1，1，2，3，5，8，13
def fibo(max):
    n, a, b = 0, 1, 1
    while n < max:
        print(b)
        # 将print(b)改为 yield b fibo()将变成generator
        t = (a, a + b)
        b = t[0]
        a = t[1]
        #等价 a, b = b, a + b
        n = n + 1
    return 'done'
fibo(10)

# 杨辉三角 generator
# 每次next输出下一行
# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
def Yh(n):
    while expression:
        pass

# reduce()把一个函数作用在一个序列[x1,x2,x3]上
# 这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累计计算
# reduce(f, [x1,x2,x3]) = f(f(f(x1), x2), x3) 
from functools import reduce
def add(x, y):
    return x + y
re = reduce(add, [1, 2, 3, 4, 5])
print(re)

# filter()函数用于过滤序列，接收一个函数和一个序列
# 把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n % 2
def not_empty(s):
    return s and s.strip()
# 去掉偶数
fil = filter(is_odd, list(range(10)))
print(list(fil))
# 去掉空字符
strFil = filter(not_empty, ['a', '', 'b', None, ' '])
print(list(strFil))
# 找出素数,埃式筛法
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3,  5,  7,  9,  11, 13,  15, 17,19, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 7,11,13,17,19, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7,11,13,17,19, ...
# # 不断筛下去，就可以得到所有的素数。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x:x % n>0
def primes():
    yield 2
    it = _odd_iter() #初始化序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it) #构造新的序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# sorted()函数是用来排序的函数
sor = sorted([36, 5, -12, 9, -21])
print(sor)
sorByAbs = sorted([36, 5, -12, 9, -21], key=my_abs)
print(sorByAbs)
# 反向排序，第三个参数reverse=True
sorByAbsRe = sorted([36, 5, -12, 9, -21], key=my_abs, reverse=True)
print(sorByAbsRe)
sortByLower = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(sortByLower)
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score)
print(L3)

# 函数闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3()) # 得到9 9 9
# 再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3()) # 得到1 4 9

# 匿名函数
# lambda x: x * x
no_name = list(map(lambda x: x * x, list(range(1,10))))
print(no_name)

# 装饰器
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
import time
def log(func):
    def wrapper(*args, **kw):
        print('call %s():'% func.__name__)
        return func(*args, **kw)
    return wrapper
# 使用python自带的functools
import functools

def logNew(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()'% func.__name__)
        return func(*args, **kw)
    return wrapper
#@log #使用log,func__name__为wrapper
@logNew # 使用logNew,func.__name__为调用函数
def now():
    return time.time()
f = now
print(f())
print(f.__name__)




# 关于输出当前时间http://www.cnblogs.com/kerwinC/p/5760811.html
currentTime = time.time() #输出unix时间戳
print(currentTime)
formatTime = time.localtime(time.time()) #格式化时间
print(formatTime)
realTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(realTime)

# 偏函数Partial function (functools自带)
# int(arg1, base = 10)
print(int('12345')) # 输入为字符串默认按十进制转换
print(int('12345', base = 8)) # base设为8，将8进制转换为十进制
print(int('1011010011', base = 2)) # 将二进制转换为十进制
# 一直需要输入base，很麻烦，于是functools.partial诞生
int2 = functools.partial(int, base=2)
print(int2('1010001111010'))
print(int2('1010001111010', base=10))

# 模块module
import hello
hello.test()
print(hello.__author__)

# 作用域
print(hello.greeting('SB'))
print(hello._private_1('sb')) # 尽量不要调用内部函数(_开头约定为内部使用函数)


# 安装第三方模块
# 通过包管理工具pip
# 处理图片的库Pillow
from PIL import Image
im = Image.open('pic.png')
print(im.format, im.size, im.mode)
im.thumbnail((200,100))
im.save('thumb.jpg', 'JPEG')

# 面向对象
# object表示父类，所有类最终都是继承自object
# 特殊方法__init__的第一个参数永远是self
# 类中所有函数第一个参数都是self,表示创建的实例本身
# 定义为self.__name外部实例不可以访问(实际通过lisa._Student__name可以访问),而self.name可以,这就是访问限制
# 特殊说明: __name__是可以在外部访问的,因此成员变量不能是__name__
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s : %s'% (self.__name, self.__score))
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 99)
bart.print_score()
# dir()方法查看属性
print(dir(bart))
print(bart._Student__name)
print(bart.get_grade())
lisa.print_score()
print(lisa.get_grade())

# 继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running')
class Cat(Animal):
    def run(self):
        print('Cat is running')

dog = Dog()
dog.run()
cat = Cat()
cat.run()
# 判断一个变量是否是某个类型可以用isinstance()判断
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))

# 获取对象信息
# 使用type()
# 使用types模块
print(type(dog))
print(type(111))
print(type('lilinjun'))
print(type(None))

import types
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x * x) == types.LambdaType)

# 实例属性和类的属性
class Family(object):
    name = 'Family'
s = Family() #创建实例
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Family.name) # 打印类的name属性
s.name = 'Sb' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Family.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

# 面向对象的高级编程
# 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。
# 在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。
# 我们会讨论多重继承、定制类、元类等概念。

# 给实例添加方法(其它实例不可用)
s = Family()
def set_name(self, name):
    self.name = name
from types import MethodType
s.set_name = MethodType(set_name, s)
s.set_name('sss')
print(s.name)
# 给class绑定方法
Family.set_name = set_name
# 使用__slots__
# 作用: 限制实例的属性(不能限制通过方法添加属性)
# 作用于: 仅对当前类实例起作用，对继承的子类不起作用
# 比如，只允许对Family实例添加name和age属性。
class Family_new(object):
    __slots__ = ('name', 'age')

fa = Family_new()
fa.name = 'sd'
fa.age = 12
# fa.score = 43会报错

# python内置的@property装饰器就是负责把一个方法编程属性调用
class StudentNew(object):
    # 相当于 get
    @property
    def score(self):
        return self._score
    # 相当于 set
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('scode must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

s = StudentNew()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()
# s.score = 666 # error ValueError: score must between 0~100!

# 多重继承(MixIn设计)
class Animal(object):
    pass
class Mammal(object):
    pass
class RunableMixIn(object):
    pass
class FlyableMixIn(object):
    pass
class Bird(Animal):
    pass

class Dog(Mammal, RunableMixIn):
    pass
class Bat(Mammal, FlyableMixIn):
    pass
class Parrot(Bird, FlyableMixIn):
    pass

# __str__与__repr__
# 定制类
class Student(object):
    def __init__(self, name):
        self._name = name
    # __str__定制Student('name')
    def __str__(self):
        return 'Student object (name: %s)'% self._name
    # __repr__定制s = Student('name')
    __repr__ = __str__
print(Student('lilinjun'))

# __iter__
# 一个类想被用于for..in循环,必须实现__iter__方法
# 并且要实现__next__方法
class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1 # 初始化两个计数器a，b
    # 用于迭代
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    # 用于取值get
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

for n in Fib():
    print(n)