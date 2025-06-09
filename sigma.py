summation = sum(2*i for i in range(1, 6))
print(summation)

# 네 배열의 합계 구하기
x = [1, 4, 6, 2]
n =len(x)

summation1 = sum(10*x[i] for i in range(0, n))
print(summation1)

# 심파이를 이용한 합계 구하기
from sympy import *

i, n = symbols('i n')

# 1부터 n까지 i를 반복하면서 2를 곱하고 더합니다.
summation2 = Sum(2*i, (i, 1, n))

# n을 5로 지정하면 숫자 1에서 5까지 반복합니다.
up_to_5 = summation2.subs(n, 5)
print(up_to_5.doit())

# 심파이로 표현식 간소화하기
from sympy import *

x = symbols('x')
expr = x**2 / x**5
print(expr) # x**-3

# 파이썬에서 로그 함수 사용하기
from math import log

# 2를 거듭제곱해 8이 되는 지수는?
x = log(8, 2)
print(x) # 3.0

