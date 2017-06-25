#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('----------迭代实现斐波那契数列----------')
print('''
兔子在出生两个月之后就拥有繁殖能力，此后\n
这对兔子每个月都能产下一对小兔子，假设所\n
有兔子都不会死去，一年之后可以繁殖多少只\n
兔子呢？\n''')
def fab(n):
    
    n1 = 1
    n2 = 1
    n3 = 1
    
    if n < 1:
        print('输入有误！')
        return -1
    
    if n <= 2:
        return(1)
        
    while n > 2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
        
    return n3
        
result = fab(int(input('请输入月数：')))
if result != -1:
    print('总共有%d对小兔子诞生！'%result)
        
