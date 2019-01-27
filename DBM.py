#!/usr/bin/env python
# coding: utf-8
# PySBM - Python Small Business Management. DataBase Management Module
# v1.0
# 27/01/2019
# Marcos Pérez Martín

# DataBase Management Module of the program.
# Módulo de base de datos de clientes.

import Config
import csv # Para trabajar con la base de datos, que tiene extensión .csv
from Config import print_titulo1 # Para pintar los títulos en los menús
from tabulate import tabulate # Para pintar las tablas de resultados



def leer_bbdd(filtro = "", primeravez = 1):
    # Con el siguiente código cargamos la base de datos a la variable bbdd
    count = 0
    with open('database.csv', encoding="utf8") as csvfile:
        entrada = csv.DictReader(csvfile)
        listadicc = list(entrada)  # Obtener lista de diccionarios

        if filtro == "":
            print("\n")
            print(tabulate(listadicc, headers='keys', tablefmt='fancy_grid'))
            print('\nNúmero de registros:', len(listadicc),"\n")  # Obtener número de registros. Hay que restarle 1 de los nombres de las columnas

        else:
            if primeravez == 1:
                Config.listadiccfiltrada = []
                for key, value in filtro.items():
                    if not value == []:
                        if key == "Día":
                            for reg in listadicc:
                                if reg["Dia1"] == value:
                                    Config.listadiccfiltrada.append(reg)
                                if reg["Dia2"] == value:
                                    Config.listadiccfiltrada.append(reg)
                                if reg["Dia3"] == value:
                                    Config.listadiccfiltrada.append(reg)
                        elif key == "Hora":
                            for reg in listadicc:
                                if reg["Hora1"] == value:
                                    Config.listadiccfiltrada.append(reg)
                                if reg["Hora2"] == value:
                                    Config.listadiccfiltrada.append(reg)
                                if reg["Hora3"] == value:
                                    Config.listadiccfiltrada.append(reg)
                        else:
                            for reg in listadicc:
                                if reg[key] == value:
                                    Config.listadiccfiltrada.append(reg)
                print("\n")
                print(tabulate(Config.listadiccfiltrada, headers='keys', tablefmt='fancy_grid'))
                print('\nNúmero de registros:', len(Config.listadiccfiltrada),"\n")  # Obtener número de registros.
            else:
                Config.listadiccfiltradatotal = []
                for key, value in filtro.items():
                    if not value == []:
                        if key == "Día":
                            for reg in listadicc:
                                if reg["Dia1"] == value:
                                    Config.listadiccfiltradatotal.append(reg)
                                if reg["Dia2"] == value:
                                    Config.listadiccfiltradatotal.append(reg)
                                if reg["Dia3"] == value:
                                    Config.listadiccfiltradatotal.append(reg)
                        elif key == "Hora":
                            for reg in listadicc:
                                if reg["Hora1"] == value:
                                    Config.listadiccfiltradatotal.append(reg)
                                if reg["Hora2"] == value:
                                    Config.listadiccfiltradatotal.append(reg)
                                if reg["Hora3"] == value:
                                    Config.listadiccfiltradatotal.append(reg)
                        else:
                            for reg in Config.listadiccfiltrada:
                                if reg[key] == value:
                                    Config.listadiccfiltradatotal.append(reg)
                print("\n")
                print(tabulate(Config.listadiccfiltradatotal, headers='keys', tablefmt='fancy_grid'))
                print('\nNúmero de registros:', len(Config.listadiccfiltradatotal),"\n")  # Obtener número de registros.

def menu_dbm():

    while 1:
        primeravez = 1

        print_titulo1("GESTIÓN DE BASE DE DATOS DE CLIENTES", 1)

        # Pedimos el modo en el que vamos a entrar
        # Primero mostramos un menú con las opciones disponibles

        print("Introduce el modo (1-3) en el que quieres entrar y presiona Enter:\n")
        print("\t1: Consultar datos")
        print("\t2: Modificar datos")
        print("\t3: Salir\n")

        # Recogemos la entrada del usuario
        # Si da error al castear a int es que el dato introducido no es un número, así que lo pedimos de nuevo hasta que sea correcto
        while 1:
           try:
               modo_principal = int(input("Modo: "))
           except ValueError:
               print ("Debes escribir un número")
           else:
               break

        print("\n")

        # Entramos al modo CONSULTAR DATOS
        if modo_principal == 1:

            while 1:
                print_titulo1("MODO CONSULTAR DATOS", 1)

                # Menú para preguntar si se quiere ver la base de datos o filtrar
                print("Introduce el modo (1-2) en el que quieres entrar y presiona Enter:\n")
                print("\t1: Ver base de datos completa")
                print("\t2: Buscar en la base de datos\n")

                while 1:
                    try:
                        modo_consultar_datos = int(input("Modo: "))
                    except ValueError:
                        print ("Debes escribir un número")
                    else:
                        break

                # Modo BASE DE DATOS COMPLETA
                if modo_consultar_datos == 1:
                    print("Modo seleccionado: Ver base de datos completa")
                    leer_bbdd()
                    input("Pulsa Enter para volver")

                # Modo BUSCAR EN BASE DE DATOS
                elif modo_consultar_datos == 2:

                    filtro_total = {'ID': [], 'Nombre': [], 'Apellido 1': [], 'Apellido 2': [], 'F. Nacim': [], 'Telefono': [], 'Email': [], 'Terapia': [], 'Terapeuta': [], 'Dias': [], 'Día': [], 'Hora': [], 'Tarifa': [], 'F. ini': [], 'F. fin': []}

                    while 1:
                        filtro = {'ID': [], 'Nombre': [], 'Apellido 1': [], 'Apellido 2': [], 'F. Nacim': [], 'Telefono': [], 'Email': [], 'Terapia': [], 'Terapeuta': [], 'Dias': [], 'Día': [], 'Hora': [], 'Tarifa': [], 'F. ini': [], 'F. fin': []}

                        print("Modo seleccionado: Buscar en la base de datos")

                        print("Introduce el modo (1-15) de búsqueda y presiona Enter:\n")
                        print("\t1: ID")
                        print("\t2: Nombre")
                        print("\t3: Primer Apellido")
                        print("\t4: Segundo Apellido")
                        print("\t5: Fecha de nacimiento")
                        print("\t6: Teléfono")
                        print("\t7: Email")
                        print("\t8: Terapia")
                        print("\t9: Terapeuta")
                        print("\t10: Número de días")
                        print("\t11: Día")
                        print("\t12: Hora")
                        print("\t13: Tarifa")
                        print("\t14: Fecha de inicio")
                        print("\t15: Fecha de fin\n")

                        while 1:
                            try:
                                modo_consultar_datos_busq = int(input("Modo: "))
                            except ValueError:
                                print ("Debes escribir un número")
                            else:
                                break

                        if modo_consultar_datos_busq == 1:
                            print("Introduce la ID a buscar")
                            param = "ID"

                        elif modo_consultar_datos_busq == 2:
                            print("Introduce el nombre a buscar")
                            param = "Nombre"

                        elif modo_consultar_datos_busq == 3:
                            print("Introduce el primer apellido a buscar")
                            param = "Apellido 1"

                        elif modo_consultar_datos_busq == 4:
                            print("Introduce el segundo apellido a buscar")
                            param = "Apellido 2"

                        elif modo_consultar_datos_busq == 5:
                            print("Introduce la fecha de nacimiento a buscar (Ej: 01/01/2019)")
                            param = "F. Nacim"

                        elif modo_consultar_datos_busq == 6:
                            print("Introduce el teléfono a buscar")
                            param = "Telefono"

                        elif modo_consultar_datos_busq == 7:
                            print("Introduce el email a buscar")
                            param = "Email"

                        elif modo_consultar_datos_busq == 8:
                            print("Introduce la terapia a buscar (Ej: L)")
                            param = "Terapia"

                        elif modo_consultar_datos_busq == 9:
                            print("Introduce el terapeuta a buscar (Ej: LLA)")
                            param = "Terapeuta"

                        elif modo_consultar_datos_busq == 10:
                            print("Introduce el número de días a buscar")
                            param = "Dias"

                        elif modo_consultar_datos_busq == 11:
                            print("Introduce el día a buscar (Ej: M)")
                            param = "Día"

                        elif modo_consultar_datos_busq == 12:
                            print("Introduce la hora de inicio a buscar")
                            param = "Hora"

                        elif modo_consultar_datos_busq == 14:
                            print("Introduce la tarifa a buscar")
                            param = "Tarifa"

                        elif modo_consultar_datos_busq == 13:
                            print("Introduce la fecha de inicio a buscar (Ej: 01/01/2019)")
                            param = "F. ini"

                        elif modo_consultar_datos_busq == 15:
                            print("Introduce la fecha de fin a buscar (Ej: 01/01/2019)")
                            param = "F. fin"

                        else:
                            print("Error al seleccionar el modo")

                        filtro[param] = input("\nDato: ")

                        print("\nFiltros aplicados:")

                        if primeravez == 0:
                            for key, value in filtro_total.items():
                                if not value == []:
                                    print(key + ": " + value)
                        for key, value in filtro.items():
                            if not value == []:
                                print(key + ": " + value)

                        leer_bbdd(filtro, primeravez)

                        print("\n¿Quieres añadir más filtros?")
                        print("Introduce el modo (1-2) y presiona Enter:\n")
                        print("\t1: Sí")
                        print("\t2: No\n")

                        while 1:
                            try:
                                modo_consultar_datos_busq_filtro = int(input("Modo: "))
                            except ValueError:
                                print ("Debes escribir un número")
                            else:
                                break

                        # Añadimos más datos al filtro
                        if modo_consultar_datos_busq_filtro == 1:
                            filtro_total = filtro
                            primeravez = 0
                            continue

                        # No añadimos más datos al filtro
                        elif modo_consultar_datos_busq_filtro == 2:
                            Config.listadiccfiltrada = []
                            Config.listadiccfiltradatotal = []
                            break
                        else:
                            print("Error al seleccionar el modo")
                else:
                    print("Error al seleccionar el modo")

        # Entramos al modo MODIFICAR DATOS
        elif modo_principal == 2:

            while 1:
                print_titulo1("MODO MODIFICAR DATOS", 1)

                # Menú para preguntar si se quiere modificar un registro existente o añadir uno nuevo
                print("Introduce el modo (1-2) en el que quieres entrar y presiona Enter:\n")
                print("\t1: Añadir un nuevo registro")
                print("\t2: Modificar un registro existente\n")

                while 1:
                    try:
                        modo_modificar_datos = int(input("Modo: "))
                    except ValueError:
                        print ("Debes escribir un número")
                    else:
                        break

                # Modo AÑADIR UN NUEVO REGISTRO
                if modo_modificar_datos == 1:
                    print("Modo seleccionado: Añadir un nuevo registro")
                    input("Pulsa Enter para volver")

                # Modo MODIFICAR UN REGISTRO EXISTENTE
                elif modo_modificar_datos == 2:
                    print("Modo seleccionado: Modificar un registro existente")
                    input("Pulsa Enter para volver")

                else:
                    print("Error al seleccionar el modo")
