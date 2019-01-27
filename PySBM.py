#!/usr/bin/env python
# coding: utf-8
# PySBM - Python Small Business Management. Main program
# v1.0
# 18/01/2019
# Marcos Pérez Martín

# Main Module of the program.
# Módulo principal del programa.

import Config # Para tener todas las variables de configuracion
import os # para usar el cls y limpiar la consola


from Config import print_titulo1, print_titulo2 # Para pintar los títulos en los menús
from EM import menu_em # Para gestionar el módulo de EM
from DBM import menu_dbm # Para gestionar el módulo de DBM

while 1:
    print_titulo1("PySMB", 1)

    # Pedimos el modo en el que vamos a entrar
    # Primero mostramos un menú con las opciones disponibles

    print("Introduce el modo (1-5) en el que quieres entrar y presiona Enter:\n")
    print("\t1: Base de datos de clientes")
    print("\t2: Pagos de clientes")
    print("\t3: Pagos a colaboradores")
    print("\t4: Informes y reportes")
    print("\t5: Horarios")
    print("\t6: Copias de seguridad")
    print("\t7: Configuración")
    print("\t8: Salir\n")

    # Recogemos la entrada del usuario
    # Si da error al castear a int es que el dato introducido no es un número, así que lo pedimos de nuevo hasta que sea correcto

    while 1:
       try:
           modo = int(input("Modo: "))
       except ValueError:
           print ("Debes escribir un número")
       else:
           break

    print("\n")

    # Entramos al modo BASE DE DATOS DE CLIENTES
    if modo == 1:
        menu_dbm()

    # Entramos al modo PAGOS DE CLIENTES (EM)
    elif modo == 2:
        menu_em()

    # Entramos al modo PAGOS A COLABORADORES
    elif modo == 3:
        print("3")

    # Entramos al modo INFORMES Y REPORTES
    elif modo == 4:
        print("4")

    # Entramos al modo HORARIOS
    elif modo == 5:
        print("5")

    # Entramos al modo COPIAS DE SEGURIDAD
    elif modo == 6:
        print("6")

    # Entramos al modo CONFIGURACIÓN
    elif modo == 7:
        print("7")

    # Entramos al modo SALIR
    elif modo == 8:
        input("Pulsa Enter para cerrar el programa")
        os.system('cls')
        break

    # Error al seleccionar modo
    else:
        print("Error al seleccionar el modo")
