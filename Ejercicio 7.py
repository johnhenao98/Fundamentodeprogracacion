# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:49:56 2019

@author: John
"""

#%% Ejercicio 7:
#   Dada la siguiente lista de strings cuente cuántas veces se repite la 
#   palabra “Python” en toda la lista.

lista = ["We are learning Python", "Functional programming in Python", 
         "What are this Python functions for?", "Do we really need Python?", 
         "Python rulez!"]

n = sum(list(map(lambda w: "Python" in w, lista)))
print(f"La palabra 'Python' aparece {n} veces en la lista.")

