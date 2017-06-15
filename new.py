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