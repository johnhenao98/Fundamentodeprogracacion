# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:34:15 2019

@author: John
"""

#%% Ejercicio 3: Eigenvalor dominante (1er valor propio) de una matriz.

from numpy import linalg as lng
import numpy as np

def maxEigValue(A, x0, tol):
    x = A*x0
    d = np.max(np.abs(x))
    x = np.divide(x, d)
    
    while (lng.norm(x - x0) > tol):
        x0 = x
        x = A*x0
        d = np.max(np.abs(x))
        x = np.divide(x, d)
    
    d = np.round(d, 2)
    x = np.round(x, 2)
    
    return d, x


D = np.matrix([[1,-3,8],[2,-5,9],[3,-6,10]], 'float')

x0 = np.ones((3,1))
tol = 1e-3

d, x, = maxEigValue(D, x0, tol)

X = lng.eig(D)
np.round(np.real(np.max(X[0])),2)

print(f"El valor propio d = {d}, coincide con el calculado por " +
      f"eig(D) = {np.round(np.real(np.max(X[0])),2)}.")

# Observación: en lugar de indicar el número de iteraciones, estas son
#              definidas por el programa de acuerdo a la comparación entre la
#              tolerancia y la aproximación (diferencia) entre el valor
#              calculado para x y el de la iteración anterior.
#              Esto se hace para evitar gastar ciclos innecesariamente cuando
#              se busca un decimal de precisión en el resultado.