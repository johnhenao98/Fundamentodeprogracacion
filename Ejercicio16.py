# -*- coding: utf-8 -*-

# EJERCICIO PRÁCTICO 3: Librería Optimize (LinProg)
# Maximizar: f = x + y
# Restricciones:
# 1) 50x + 24y <= 2400
# 2) 30x + 33y <= 2100
# Límites: x, y <= 0

#%% LIBRERÍAS
import numpy as np
from scipy.optimize import linprog as lp

#%% PARÁMETROS DE ENTRADA
# Coeficientes de Función
cFuncionMin = [1, 1] # 1x + 1y

# Coeficientes de Restricciones
aRestricciones = [[50, 24], [30, 33]] # [50x + 24y], [30x + 33y]
bRestricciones = [2400, 2100]

# Límites
limitesX = (0, None)
limitesY = (0, None)

#%% PROGRAMA
# Configuraciones para ejecutar algoritmo de optimización
cFuncionMax = -np.array(cFuncionMin) # Maximización en lugar de minimización
limites = (limitesX, limitesY) 

# Ejecución de optimización
solucion = lp(cFuncionMax, A_ub = aRestricciones, b_ub = bRestricciones, bounds = limites)
funcionReal = - solucion.fun # Ocurrió una maximización en lugar de una minimización

#%% IMPRESIÓN DE RESULTADOS
print()
print('Resultado de ejecución:')
print(solucion)
print()

print('Solución:')
print('X = {:.4f}'.format(solucion.x[0]))
print('Y = {:.4f}'.format(solucion.x[1]))
print('Función evaluada en solución: {:.4f}'.format(funcionReal))
