# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:08:09 2019

@author: John
"""

#%% Ejercicio 11: Filtrado (detección de bordes) de la imagen Lenna.png 
#                utilizando el kernel sobel y convolución en dos dimensiones.

import numpy as np
import pylab as pl

path = 'C:\\Users\\Administrador\\Pictures\\Lenna.png'

src = pl.imread(path)

pl.figure(1)
pl.imshow(src, cmap = pl.cm.gray)

src = np.matrix(src[:,:,2],'float')

pl.figure(2)
pl.imshow(src, cmap = pl.cm.gray)

m = np.size(src, axis = 0)
n = np.size(src, axis = 1)

KernelH = np.matrix([[-1,-2,-1],[0,0,0],[1,2,1]],'float')
KernelV = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]],'float')

stackColumns = np.ones((n,1))
src = np.hstack((stackColumns, src, stackColumns))
stackRows = np.ones((1,m + 2))
src = np.vstack((stackRows, src, stackRows))

dstH = np.ones_like(src)
dstV = np.ones_like(src)

for i in range(1,m):
    for j in range(1,n):
        dstH[i,j] = np.multiply(src[i-1:i+2,j-1:j+2],KernelH).sum()

for i in range(1,m):
    for j in range(1,n):
        dstV[i,j] = np.multiply(src[i-1:i+2,j-1:j+2],KernelV).sum()

dst = np.sqrt(np.power(dstH[1:m+1,1:n+1],2) + np.power(dstV[1:m+1,1:n+1],2))

pl.figure(3)
pl.imshow(dst, cmap = pl.cm.gray)

# Observación: se debe colocar la ruta de la imagen "Lena.png" en "path".

