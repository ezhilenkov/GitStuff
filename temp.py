# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

from __future__ import print_function

def f(x, y, op):
    if op == '-':
        return(x - y)
    elif op == '/':
        return(x / y)
    else:
        return('unknown operation')
        
x = int(input('vvedite pervoe chislo '))
a = int(input('введите второе число '))
op = input('выберете операцию "/" или "-": ')

print(f(x, a, op))