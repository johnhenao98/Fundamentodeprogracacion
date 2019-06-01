# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:49:44 2019

@author: John
"""

#%% Ejercicio 5:
#   Dado un string que contiene números enteros separados por espacio,
#   determine los números de la lista que son números “palíndromos”.

import numpy as np

numbers = "9 7 8 6 9"

nmbs = np.array(list(map(int, numbers.split(" "))))
idx = np.where(nmbs == nmbs[::-1])
n = list(set(nmbs[idx]))

print(f"En la lísta, los números {n} son palíndromos.")

#a = list(map(int, numbers.split(" ")))
#b = a[::-1]
#
##n = list(filter(lambda x: x == b, a))
##n = list(enumerate(map(lambda x, y: x == y, a, b)))
#n = dict(enumerate(map(lambda x, y: x == y, a, b)))

