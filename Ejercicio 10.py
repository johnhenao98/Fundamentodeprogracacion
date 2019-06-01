#%% Ejercicio 10: Convolución unidimensional entre dos polinomios.

from scipy.ndimage import interpolation as nt
from matplotlib import pyplot as plt
import numpy as np

P = lambda x: 2*(x**3) + 3*(x**2) + 6*x + 7
h = lambda x: x + 2

x = np.linspace(-1,1)
y = h(x)

plt.figure(1)
plt.plot(x, P(x), label = 'P(x)')
plt.plot(x, h(x), label = 'h(x)')
plt.title('Funciones P(x) y h(x)')
plt.xlabel('x')
plt.legend()
plt.show()

n = len(x)

z = np.zeros(2*n-1)

for i in range(1,2*n):
    z[i-1] = np.multiply(P(x), nt.shift(h(-x),-n+i)).sum()

plt.figure(2)
plt.plot(z)
plt.title('Resultado convolución entre P(x) y h(x)')
plt.xlabel('x')
plt.ylabel('z(x)')
plt.legend()
plt.show()

# Observación: error en la escala de tiempo del resultado (corregir).

