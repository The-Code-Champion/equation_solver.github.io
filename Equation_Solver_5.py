import numpy as np
from numpy import linspace,append
import sympy as sp
from sympy import Eq, symbols, simplify
from sympy.solvers import solve

try:
    Var_num = int(input('Enter the number of Variables: '))
    Eq_num = int(input('Enter the number of Equations: '))
    Constant_num = int(input('Enter number of constants: '))
except ValueError:
    print('Error Occured, Try again')
    exit()

Eq_range = range(Eq_num)
Var_range = range(Var_num)
Constant_range = range(Constant_num)

Eqs = []
Variables = []
Consts = []
Consts_Vals = []

if Var_num <= Eq_num:
    for number in Var_range:
        Var = []
        Var = input(f'Enter the Variable {number+1}: ')
        Variables.append(Var)
    for number in Eq_range:
        Eq_Split = []
        Eq_input = simplify(input(f'Enter Equation {number+1}: '))
        Eq_Split = [Eq_input,0]
        #print(Eq_Split)
        eq = Eq(Eq_Split[0],Eq_Split[1])
        Eqs.append(eq)
    #print(f'Eqs are {Eqs}, Variables are {Variables}')
    
    for num in Constant_range:
        Const = input('Input constant: ')
        Consts.append(Const)
        Const_Val = input('Enter the value of that constant: ')
        Consts_Vals.append(Const_Val)
    
    substitution_map = {}
    Variables2 = symbols(Variables)

    for num in Constant_range:
        substituted_vals = {Consts[num]: Consts_Vals[num]}
        substitution_map.update(substituted_vals)
    
    substituted_eqs = [eq.subs(substitution_map) for eq in Eqs]

    output = solve(substituted_eqs,Variables2,dict=True)

    outputValues = {}

    for number in Eq_range:
        outVal = {Variables[number]: float(output[0][Variables2[number].evalf()])}
        outputValues.update(outVal)

    print(outputValues)
elif Var_num > Eq_num:
    print('Too many unknowns for the number of equations.')
#elif Var_num < Eq_num:
#    print('simplify the number of equations and try again.')
else:
    print('You broke the code')









'''
x+y-z-4
x-2*y+3*z+6
2*x+3*y+z-7

###############
Ax
Dx
Ay
AB
AC
BC
BD
BE
CE
DE
Ax+Dx-F
Ay+2*G
-G*d1+F*d2-Dx*(d2+d3)
Ax+AC*(d1/sqrt(d1^2+d2^2))
Ay-AB-AC*(d2/sqrt(d1^2+d2^2))
-F-BC-AC*(d1/sqrt(d1^2+d2^2))
-CE+AC*(d2/sqrt(d1^2+d2^2))
Dx+DE
G+BD
BC+BE*(d1/sqrt(d1^2+d3^2))
d1
4.49
d2
5.26
d3
5.81
F
73.4
G
65.8
'''

