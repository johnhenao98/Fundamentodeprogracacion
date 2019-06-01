# -*- coding: utf-8 -*-

# EJERCICIO PRÁCTICO 4: Librería Optimize
# Problema de maximización del retorno de venta (ingreso, utilidad):

# Maximizar ingreso: Sumatoria (p(t) * x(t))
# p(t): Precio del producto en el intervalo de tiempo 't'
# x(t): Cantidad de producto vendido (demanda) en el intervalo de tiempo 't'

# Restricciones:
# 1) El total de productos vendidos no puede superar el inventario total (s0):
# Sumatoria (x(t)) <= s0
# 2) x(t) >= 0 (cantidad de productos no negativa)
# 3) x(t) <= A / B (valor según modelo para que precios no sean negativos)

# Modelo: Precio en función del tiempo y la demanda
# p(x, t) = (A - B * x(t)) * (D / (D + t))

# A,B y D son parámetros que resultan de la caracterización del comportamiento
# del ingreso como producto del precio por la demanda, a lo largo del tiempo.
# Puede darles el valor que considere conveniente.

#%% LIBRERÍAS
from scipy.optimize import minimize as mini
import numpy as np

#%% CONFIGURACIÓN
# Limitar número de decimales en impresión de arreglos
np.set_printoptions(precision = 2, suppress = True)

#%% PARÁMETROS DE ENTRADA
tiempoTotal = 10 # Total Horas
factorEscala = 10000 # Factor para que el resultado sea de orden 1, facilitando convergencia
A = 5000 # Precio máximo
B = 100 # Rebaja en precio según demanda
D = 20 # Término para disminución del precio a medida que avanza el tiempo
s0 = 200 # Inventario total

#%% FUNCIONES

# Implementación de modelo de precios en función del tiempo y la demanda
def precios(x):
    # Variables globales a utilizar en modelo
    global A, B, D, arregloTiempo
    
    # Inicializar arreglo precios
    listaPrecios = []
    
    # Ciclo para calcular precio en cada intervalo de tiempo
    for (indice, tiempo) in enumerate(arregloTiempo):
        precio = (A - B * x[indice]) * (D / (D + tiempo))
        # Agregar precio en arreglo sólo si no es negativo
        if (precio >= 0): listaPrecios.append(precio)
        else: listaPrecios.append(0)
    
    # Retornar lista de precios como arreglo NumPy
    return (np.array(listaPrecios))

# Función a optimizar: Ingreso
def ingreso(x):
    producto = np.dot(precios(x), x) # Ingresos: Precio * Demanda
    return (- producto / factorEscala) # Maximizar en lugar de minimizar

# Restricciones
def restriccionInventario(x):
    global s0
    return (s0 - np.sum(x))


#%% PROGRAMA

# Inicializaciones
# Arreglo de tiempo
arregloTiempo = np.arange(1, tiempoTotal + 1) # N° Hora

# Arreglo Semilla de demanda (Aleatorio: Entre 0 y promedio)
promedioDemanda = (s0 // tiempoTotal)
x0 = np.random.rand(tiempoTotal) * promedioDemanda
xPromedio = np.full(tiempoTotal, promedioDemanda)

# Configuraciones para ejecutar algoritmo de optimización
# Restricciones
restricciones = [{'type': 'ineq', 'fun': restriccionInventario}]
# Límites
limiteInferior = 0
limiteSuperior = A / B
limites = [(limiteInferior, limiteSuperior) for i in range(tiempoTotal)]

# Ejecución de optimización
soluciones = mini(ingreso, x0, method='SLSQP', bounds = limites, constraints = restricciones)
ingresoTotal = - ingreso(soluciones.x) * factorEscala

#%% IMPRESIÓN DE RESULTADOS

# Arreglo de tiempo (N° Hora)
print()
print('Arreglo de Tiempo:')
print(arregloTiempo)
print()

# Arreglo semilla de demanda:
print('Arreglo Semilla de Demanda:')
print(x0)
print('Suma Arreglo Semilla Demanda: {:.2f}'.format(np.sum(x0)))
print()

# Resumen solución
# Arreglo de demanda de Productos por hora
print('Demanda Promedio de Productos (por Hora): ')
print(xPromedio)
print('Demanda Óptima de Productos por Hora: ')
print(soluciones.x)
print()

# Arreglo de precio de productos por hora
print('Precio Estimado de Productos por Hora (para Demanda Óptima):')
print(precios(soluciones.x))
print()

# Ingreso total
print('Ingreso total: ${:.2f}'.format(ingresoTotal))
