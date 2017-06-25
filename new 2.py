#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('----------递归实现斐波那契数列----------')
print('''
兔子在出生两个月之后就拥有繁殖能力，此后\n
这对兔子每个月都能产下一对小兔子，假设所\n
有兔子都不会死去，一年之后可以繁殖多少只\n
兔子呢？\n''')
def fab(n):

    if n < 1:
        print('输入有误')
        return -1
        
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)
        
result = fab(int(input('请输入月数：')))
if result != -1:
    print('总共有%d对小兔崽子诞生！'%result)
