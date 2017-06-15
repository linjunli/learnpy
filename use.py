def _not_divisible(n):
    return lambda x:x % n>0
print(_not_divisible(5))