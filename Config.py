#!/usr/bin/env python
# coding: utf-8
# PySBM - Python Small Business Management. Configuration Module
# v1.0
# 28/01/2019
# Marcos Pérez Martín

# Configuration Module of the program.
# Módulo de configuración del programa.

import os # para usar el cls y limpiar la consola

# EM
# si modo_visualizacion = 1, modo consola
modo_visualizacion = 1

# EM
# si modo_diccionarios = 1, diccionarios .dat reales
# si modo_diccionarios = 0, diccionarios ficticios hardcoded
modo_diccionarios = 1

# PM
# If config_by_input == 0, the values used will be the included in the code
# If config_by_input == 1, the program will ask the user to introduce the values
config_by_input = 1

listadiccfiltrada = []
listadiccfiltradatotal = []

# EM, PySBM,
def print_titulo1(texto, altura):
    # 66 asteriscos
    # 58 caracteres por línea máximo
    # máximo 2 líneas
    # texto es el texto a escribir
    # altura es el numero de lineas en blanco entre texto y bordes

    os.system('cls')
    if len(texto) > 58:
        texto_dividido = texto.split(" ")
        if (len(texto_dividido)) % 2 == 0:
            division = int(len(texto_dividido)/2)
            texto_linea_1 = texto_dividido[:division]
            texto_linea_2 = texto_dividido[division:]
        else:
            division = int((len(texto_dividido)+1)/2)
            texto_linea_1 = texto_dividido[:division]
            texto_1 = " ".join(texto_linea_1)
            longitud_linea_1 = len(texto_1)
            if longitud_linea_1 % 2 == 1:
                texto_1 = texto_1 + " "

            texto_linea_2 = texto_dividido[division:]
            texto_2 = " ".join(texto_linea_2)
            longitud_linea_2 = len(texto_2)
            if longitud_linea_2 % 2 == 1:
                texto_2 = texto_2 + " "

        espacios_linea_1 = int((64-longitud_linea_1)/2)
        espacios_linea_2 = int((64-longitud_linea_2)/2)

    else:
        if len(texto) % 2 == 1:
            texto = texto + " "
        espacios = int((64-len(texto))/2)

    print("*" * 66)
    for x in range(altura):
        print("*" + " " * 64 + "*")
    if len(texto) <= 58:
        print("*" + " " * espacios + texto + " " * espacios + "*")
    else:
        print("*" + " " * espacios_linea_1 + texto_1 + " " * espacios_linea_1 + "*")
        print("*" + " " * 64 + "*")
        print("*" + " " * espacios_linea_2 + texto_2 + " " * espacios_linea_2 + "*")
    for x in range(altura):
        print("*" + " " * 64 + "*")
    print("*" * 66)
    print("\n")

# EM, PySBM,
def print_titulo2(texto):
    # longitud total: 66 caracteres
    os.system('cls')
    if len(texto) % 2 == 1:
        texto = texto + " "
    espacios = int((66-len(texto))/2)
    print("\n")
    print(" " * espacios + texto + " " * espacios + "\n")
    print("*" * 66)
    print("\n")
