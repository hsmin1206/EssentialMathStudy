# 심파이로 선형함수 그래프 그리기
from sympy import *

x = symbols('x')
f = 2 * x + 1
plot(f)

# 심파이로 2차 함수 그래프 그리기
x = symbols('x')
f = x**2 + 1
plot(f)