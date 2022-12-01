# копирование переменнной

import random

a = [1, 2, 3]

def foo(a):
    b = a.copy()
    random.shuffle(a)
    return b
    
print(foo(a))
foo(a)
print(a)