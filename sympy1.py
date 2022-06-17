import sympy
import math


x = sympy.symbols('x')
y = sympy.symbols('y')


c = sympy.integrate(sympy.sin(x**2), (x))
print(c)
