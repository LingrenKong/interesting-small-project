# _*_coding:utf-8_*_
"""
Author: Lingren Kong
Created Time: 2020/3/23 11:29
运用dsolve为主，符号方式解可解的常微分方程
"""

from sympy.abc import x
from sympy import Function, dsolve, Eq, Derivative
# sin, cos, exp
f = Function('f')
q = Eq(Derivative(f(x),x),3*x**2)
print(dsolve(q))

