# 독립변수가 두 개인 함수의 그래프 그리기
from sympy import *
from sympy.plotting import plot3d

x, y = symbols('x y')
f = 2*x + 3*y
plot3d(f)