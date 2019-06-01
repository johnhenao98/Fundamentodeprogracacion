# -*- coding: utf-8 -*-

# EJERCICIO PRÁCTICO 2: Librería Optimize
# Minimizar: f = -(2*x1*x2 + 2*x1 - x1^2 - 2*x2^2)
# Restricciones:
# 1) x1^3 - x2 = 0
# 2) x2 - (x1 - 1)^4 - 2 >= 0
# Límites x1: 0.5 <= x1 <= 1.5
# Límites x2: 1.5 <= x2 <= 2.5
# Semilla inicial: (0, 2.5)

#%% LIBRERÍAS
from scipy.optimize import minimize as mini

#%% PARÁMETROS DE ENTRADA
limitesX0 = (0.5, 1.5)
limitesX1 = (1.5, 2.5)
semilla = [0, 2.5]

#%% FUNCIONES
def f(x):
    funcion = 2*x[0]*x[1] + 2*x[0] - x[0]**2 - 2*(x[1]**2)
    return (-funcion)

def restriccion1(x):
    return (x[0]**3 - x[1])

def restriccion2(x):
    return (x[1] - (x[0] - 1)**4 - 2)

#%% PROGRAMA
# Configuraciones para ejecutar algoritmo de optimización
restricciones = [{'type': 'eq', 'fun': restriccion1},
                 {'type': 'ineq', 'fun': restriccion2}]
limites = (limitesX0, limitesX1)

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
print('Función evaluada en solución: {:.4f}'.format(solucion.fun))
