# -*- coding: utf-8 -*-

# EJERCICIO 1: Programación por Procedimientos
# Diseñe una función que recibe como parámetro de entrada un string
# que sólo contiene letras, tanto mayúsuculas como minúsculas (sin espacios),
# mezcladas indistintamente. Su función debe invertir el orden de los caracteres,
# y además, los que estén en minúscula, debe convertirlos en mayúscula, y viceversa.
# Acompañe la función de una interfaz de usuario por consola.

# Constantes
minusculas = 'abcdefghijklmnñopqrstuvwxyz'
mayusculas = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# FUNCIONES

# Función que convierte texto según enunciado del ejercicio
def convertir(textoEntrada):
    # Inicializar texto a retornar
    textoSalida = ''
    # Recorrer texto original
    for letra in textoEntrada:
        # Convertir letra de minúscula a mayúscula
        if (letra in minusculas): 
            posicion = minusculas.index(letra)
            letra = mayusculas[posicion]
        # Convertir letra de minúscula a mayúscula
        elif (letra in mayusculas): 
            posicion = mayusculas.index(letra)
            letra = minusculas[posicion]
        # Agregar cada letra a la izquerda para invertir orden
        textoSalida = letra + textoSalida
    # Retornar texto de salida
    return textoSalida

# Función para pedir texto de entrada por consola
def pedirTexto():
    print()
    texto = input('Ingrese el texto a convertir: ')
    return texto

# Función para mostrar el texto convertido
def mostrar(textoEntrada, textoSalida):
    print()
    print('El resultado de convertir el texto: "{0}" es:'.format(textoEntrada))
    print(textoSalida)

# PROGRAMA
textoInicial = pedirTexto()
textoConvertido = convertir(textoInicial)
mostrar(textoInicial, textoConvertido)
    