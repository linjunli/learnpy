//自定义求绝对值
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

//求阶层
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(100))

//汉诺塔
step = []
def move(n, a='A', b='B', c='C'):
    if n == 1:
        step.append(a+"===>>>"+c)
        return print(a,'===>>>', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
N = int(input('step num:'))
move(N)
print("need",len(step),step)

//python切片功能slice
L = ['A', 'B', 'C', 'D', 'E']
print(L[1:3])
print(L[-2:-1])