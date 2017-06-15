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

