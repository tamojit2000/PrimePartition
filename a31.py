from sympy import symbols,Eq,solve

y=symbols('x')
a=Eq(x+3)
s=solve(a)
print(s)
