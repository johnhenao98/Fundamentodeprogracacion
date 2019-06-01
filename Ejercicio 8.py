# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:50:09 2019

@author: John
"""

#%% Ejercicio 8:
#   ¿Cuál es la suma de los primeros 50 números positivos cuyo cuadrado es
#   divisible por 5?.

n = sum(list(filter(lambda x: (x**2)%5 == 0, range(1,1000)))[:50])
print(f"La suma de los primeros 50 números positivos es {n}.")