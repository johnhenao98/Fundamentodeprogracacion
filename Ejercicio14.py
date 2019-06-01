# -*- coding: utf-8 -*-

# EJERCICIO PRÁCTICO 1: Librería Optimize
# Minimizar: f = x1 * x4 * (x1 + x2 + x3) + x3
# Restricciones:
# 1) x1*x2*x3*x4 >= 25
# 2) (x1^2) + (x2^2) + (x3^2) + (x4^2) = 40
# Límites: 1 <= xi <= 5
# Semilla inicial: (1, 5, 5, 1)

#%% LIBRERÍAS
from scipy.optimize import minimize as mini
import numpy as np

#%% PARÁMETROS DE ENTRADA
limiteInferior = 1
limiteSuperior = 5
semilla = [1, 5, 5, 1]

#%% FUNCIONES
def f(x):
    funcion = x[0]* x[3] * (x[0] + x[1] + x[2]) + x[2]
    return (funcion)

def restriccion1(x):
    return (np.prod(x)- 25)

def restriccion2(x):
    return (np.sum(np.square(x)) - 40)

#%% PROGRAMA
# Configuraciones para ejecutar algoritmo de optimización
restricciones = [{'type': 'ineq', 'fun': restriccion1},
                 {'type': 'eq', 'fun': restriccion2}]
limites = [(limiteInferior, limiteSuperior) for x in range(4)]

# Ejecución de optimización
solucion = mini(f, semilla, method='SLSQP', bounds = limites, constraints = restricciones)

#%% IMPRESIÓN DE RESULTADOS
print()
print('Resultado de ejecución:')
print(solucion)
print()

print('Solución:')
print('X1 = {:.4f}'.format(solucion.x[0]))
print('X2 = {:.4f}'.format(solucion.x[1]))
print('X3 = {:.4f}'.format(solucion.x[2]))
print('X4 = {:.4f}'.format(solucion.x[3]))
print('Función evaluada en solución: {:.4f}'.format(solucion.fun))
