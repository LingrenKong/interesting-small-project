# _*_coding:utf-8_*_
"""
Author: Lingren Kong
Created Time: 2020/4/18 10:24
"""

from sympy import *

def G(nlist,r):
    """
    母函数法求有限可重复组合数问题
    :param nlist: 可重复集合的n1~nk数值
    :param r: 所求取出数r
    :return:
    """
    f = 1
    x = symbols('x')
    for n in nlist:
        t = 1
        for i in range(1,n+1):
            t = t + x**i
        f = f*t
    f = Poly(f)
    print('生成函数为：',f)
    print(f'从重复集合{[x for x in nlist]}取出{r}个的方法数为：',f.as_dict()[(r,)])
    return f.as_dict()[(r,)]

if __name__ == '__main__':
    G([2,2,3],2)