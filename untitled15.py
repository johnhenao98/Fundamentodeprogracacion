# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:12:15 2019

@author: John
"""

#%% Ejercicio 3: resuelva con "linprog":
#                max f(x, y) = x + y
#                sujeto a:
#
#                Restricciones:     50 * x + 24 * y <= 2400
#                                   30 * x + 33 * y <= 2100
#                Rango:             x, y >= 0

from scipy.optimize import linprog

# la función "linprog" siempre miniza la función objetivo.
# Para maximizarla, se hace max(f(x)) == -min(-f(x)).

c = [-1, -1]
A = [[50, 24], [30, 33]]
b = [2400, 2100]
bnds = (0, None)

sltn = linprog(c, A, b, bounds = bnds, method = 'simplex')

print(f"El valor máximo de la función es f(x) = {(-1)*sltn.fun}.\n" +
      f"El argumento que la maximiza es: x = {sltn.x}")

