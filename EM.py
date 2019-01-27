#!/usr/bin/env python
# coding: utf-8
# PySBM - Python Small Business Management. Earning Management Module
# v1.3
# 28/01/2019
# Marcos Pérez Martín

# Earning Management Module of the program.
# Módulo de pagos de clientes.

import Config # Para tener todas las variables de configuracion
import time # para obtener fecha
import os # para usar el cls y limpiar la consola
import pickle # para guardar y cargar los diccionarios .dat

from Config import print_titulo1 # Para pintar los títulos en los menús


if Config.modo_diccionarios == 1:
    print("Modo diccionarios .dat reales")

    def cargar_datos_tarifas():
        try:
            with open("diccionario_tarifas.dat", "rb") as f:
                return pickle.load(f)
        except (OSError, IOError) as e:
            return dict()

    def cargar_datos_pagos():
        try:
            with open("diccionario_pagos.dat", "rb") as g:
                return pickle.load(g)
        except (OSError, IOError) as h:
            return dict()

    def guardar_datos_tarifas(dic):
        with open("diccionario_tarifas.dat", "wb") as f:
            pickle.dump(dic, f)

    def guardar_datos_pagos(dic):
        with open("diccionario_pagos.dat", "wb") as g:
            pickle.dump(dic, g)

    diccionario_tarifas = cargar_datos_tarifas()
    diccionario_pagos = cargar_datos_pagos()

elif Config.modo_diccionarios == 0:
    print("Modo diccionarios ficticios")
    # Para poder trabajar con Jupyter creo que tengo que "emular" los diccionarios así, pero
    # HAY QUE IMPLEMENTAR LA PARTE DE LOS .dat
    # diccionario de pacientes y tarifas.
    diccionario_tarifas = {"Nombre1": 90, "Nombre2": 50, "Nombre3": 90, "Nombre4": 50, "Nombre5": 90, "Nombre6": 50}

    # diccionario con diccionarios dentro para los pagos de cada mes. NESTED DICTIONARY
    diccionario_pagos = {"201901": {"Nombre2": [44, "Otro", "01/01/2019"], "Nombre3": [14, "Efectivo", "06/01/2019"]},
                         "201812": {},
                         "201811": {"Nombre1": [90, "Efectivo", "01/11/2018"], "Nombre2": [50, "Tarjeta", "05/11/2018"],
                                    "Nombre3": [90, "Otro", "10/11/2018"], "Nombre4": [50, "Efectivo", "15/11/2018"],
                                    "Nombre5": [90, "Tarjeta", "20/11/2018"], "Nombre6": [50, "Otro", "30/11/2018"]},
                         "201902": {},
                         "201903": {"Nombre1": [90, "Efectivo", "01/03/2019"]}}


def menu_em():

    while 1:

       print_titulo1("GESTIÓN DE PAGOS DE CLIENTES", 1)


       # Pedimos el modo en el que vamos a entrar
       # Primero mostramos un menú con las opciones disponibles

       print("Introduce el modo (1-5) en el que quieres entrar y presiona Enter:\n")
       print("\t1: Nuevo pago")
       print("\t2: Consultar datos")
       print("\t3: Modificar datos")
       print("\t4: Generar informe")
       print("\t5: Generar nuevo mes")
       print("\t6: Salir\n")

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

       # Entramos al modo NUEVO PAGO
       if modo_principal == 1:

           while 1:
               print_titulo1("MODO NUEVO PAGO - NOMBRE", 1)

               # Pido nombre del paciente y compruebo si existe en el diccionario de tarifas
               print("Introduce el nombre del paciente\n")
               nuevo_pago_nombre = input("Nombre: ")

               if nuevo_pago_nombre in diccionario_tarifas:
                   print("\nPaciente encontrado")
                   nuevo_pago_tarifa = diccionario_tarifas.get(nuevo_pago_nombre)
                   break
               else:
                   input("\nPaciente no encontrado. Pulsa Enter para volver")

           while 1:
               print_titulo1("MODO NUEVO PAGO - TARIFA", 1)

               # Confirmo la cantidad pagada del diccionario de tarifas
               print("El paciente", nuevo_pago_nombre, "tiene asignada una tarifa de", nuevo_pago_tarifa, "€.")
               print("¿Se corresponde esta cifra con el pago?\n")
               print("\t1: Sí, el paciente paga", nuevo_pago_tarifa, "€")
               print("\t2: No, el paciente paga otra cantidad\n")
               while 1:
                   try:
                       modo_nuevo_pago_tarifa = int(input("Selecciona una opción: "))
                   except ValueError:
                       print ("\nDebes escribir un número\n")
                   else:
                       break

               # La tarifa se corresponde con la del diccionario
               if modo_nuevo_pago_tarifa == 1:
                   input("\nCantidad pagada: " + nuevo_pago_tarifa + "€. Pulsa Enter para continuar")
                   break

               # La tarifa no se corresponde con la del diccionario
               elif modo_nuevo_pago_tarifa == 2:
                   print("\nIntroduce la cantidad pagada\n")
                   while 1:
                       try:
                           nuevo_pago_tarifa = int(input())
                       except ValueError:
                           print("\nDebes escribir un número\n")
                       else:
                           break
                   input("\nCantidad pagada: " + str(nuevo_pago_tarifa) + "€. Pulsa Enter para continuar")
                   break


               # Error al seleccionar tarifa
               else:
                   input("\nError al seleccionar la tarifa. Pulsa Enter para volver")


           while 1:
               print_titulo1("MODO NUEVO PAGO - FORMA DE PAGO", 1)

               # Pregunto método de pago
               print("Introduce la forma de pago\n")
               print("\t1: Efectivo")
               print("\t2: Tarjeta")
               print("\t3: Otro\n")

               while 1:
                   try:
                       modo_nuevo_pago_metodo = int(input("Selecciona una opción: "))
                   except ValueError:
                       print ("\nDebes escribir un número\n")
                   else:
                       break

               # Pago en efectivo
               if modo_nuevo_pago_metodo == 1:
                   input("\nPago en efectivo. Pulsa Enter para continuar")
                   nuevo_pago_metodo = "Efectivo"
                   break

               # Pago con tarjeta
               elif modo_nuevo_pago_metodo == 2:
                   input("\nPago con tarjeta. Pulsa Enter para continuar")
                   nuevo_pago_metodo = "Tarjeta"
                   break

               # Otro método de pago
               elif modo_nuevo_pago_metodo == 3:
                   input("\nPago con otra forma de pago. Pulsa Enter para continuar")
                   nuevo_pago_metodo = "Otro"
                   break

               # Error al seleccionar forma de pago
               else:
                   input("\nError al seleccionar la forma de pago. Pulsa Enter para volver")

           while 1:
               print_titulo1("MODO NUEVO PAGO - FECHA", 1)

               # Pregunto si se ha realizado el pago hoy y si no pido fecha
               print("¿Usar la fecha de hoy para el pago?\n")
               print("\t1: Sí, usar", time.strftime("%d/%m/%Y"))
               print("\t2: No, elegir otra fecha\n")

               while 1:
                   try:
                       modo_nuevo_pago_fecha = int(input("Selecciona una opción: "))
                   except ValueError:
                       print ("\nDebes escribir un número\n")
                   else:
                       break

               # Fecha de hoy
               if modo_nuevo_pago_fecha == 1:
                   input("\nFecha escogida: " + time.strftime("%d/%m/%Y") + ". Pulsa Enter para continuar")
                   nuevo_pago_fecha = time.strftime("%d/%m/%Y")
                   nuevo_pago_fecha_anio = time.strftime("%Y")
                   nuevo_pago_fecha_mes = time.strftime("%m")
                   break

               # Otra fecha
               elif modo_nuevo_pago_fecha == 2:
                   print("\nIntroduce el día del pago (2 cifras)\n")
                   while 1:
                       try:
                           nuevo_pago_fecha_dia_tmp = input("Día: ").zfill(2)
                           if nuevo_pago_fecha_dia_tmp.isdigit() and int(nuevo_pago_fecha_dia_tmp) > 0 and int(nuevo_pago_fecha_dia_tmp) <=31:
                               nuevo_pago_fecha_dia = nuevo_pago_fecha_dia_tmp
                           else:
                               raise ValueError
                       except ValueError:
                           print ("\nDebes escribir un número entre 1 y 31\n")
                       else:
                           break

                   print("\nIntroduce el mes del pago (2 cifras)\n")
                   while 1:
                       try:
                           nuevo_pago_fecha_mes_tmp = input("Mes: ").zfill(2)
                           if nuevo_pago_fecha_mes_tmp.isdigit() and int(nuevo_pago_fecha_mes_tmp) > 0 and int(nuevo_pago_fecha_mes_tmp) <=12:
                               nuevo_pago_fecha_mes = nuevo_pago_fecha_mes_tmp
                           else:
                               raise ValueError
                       except ValueError:
                           print ("\nDebes escribir un número entre 1 y 12\n")
                       else:
                           break

                   print("\nIntroduce el año del pago (4 cifras)\n")
                   while 1:
                       try:
                           nuevo_pago_fecha_anio_tmp = input("Año: ").zfill(4)
                           if nuevo_pago_fecha_anio_tmp.isdigit() and int(nuevo_pago_fecha_anio_tmp) > 0 and int(nuevo_pago_fecha_anio_tmp) <=9999:
                               nuevo_pago_fecha_anio = nuevo_pago_fecha_anio_tmp
                           else:
                               raise ValueError
                       except ValueError:
                           print ("\nDebes escribir un número de cuatro cifras\n")
                       else:
                           break
                   nuevo_pago_fecha = nuevo_pago_fecha_dia + "/" + nuevo_pago_fecha_mes + "/" + nuevo_pago_fecha_anio
                   input("\nFecha escogida: " + nuevo_pago_fecha + ". Pulsa Enter para continuar")
                   break

               # Error al seleccionar fecha
               else:
                   input("Error al seleccionar la fecha. Pulsa Enter para volver")

           while 1:
               print_titulo1("MODO NUEVO PAGO - RESUMEN", 1)
               print("Se va a introducir un nuevo pago con los siguientes datos:\n")

               print("- Nombre: ", nuevo_pago_nombre)
               print("- Cantidad: ", nuevo_pago_tarifa)
               print("- Forma de pago: ", nuevo_pago_metodo)
               print("- Fecha: ", nuevo_pago_fecha)

               print("\n¿Confirmar?\n")
               print("\t1: Sí, introducir pago")
               print("\t2: No, cancelar pago\n")

               while 1:
                   try:
                       modo_nuevo_pago_confirmar = int(input("Selecciona una opción: "))
                   except ValueError:
                       print ("\nDebes escribir un número\n")
                   else:
                       break

               # Confirmar introduccion pago
               if modo_nuevo_pago_confirmar == 1:
                   # AQUI HAY QUE CONFIRMAR QUE EL ARCHIVO DEL MES EXISTE
                   diccionario_pagos[nuevo_pago_fecha_anio+nuevo_pago_fecha_mes][nuevo_pago_nombre] = [nuevo_pago_tarifa, nuevo_pago_metodo, nuevo_pago_fecha]
                   print("\nNuevo pago introducido\n")

                   if Config.modo_diccionarios == 1:
                       print("Guardando datos de tarifas...")
                       guardar_datos_tarifas(diccionario_tarifas)
                       print("Datos de tarifas guardados\n")
                       print("Guardando datos de pagos...")
                       guardar_datos_pagos(diccionario_pagos)
                       print("Datos de pagos guardados\n")

                   input("Operación finalizada. Pulsa Enter para volver al menú principal")
                   break

               # Cancelar introduccion pago
               elif modo_nuevo_pago_confirmar == 2:
                   print("\nNuevo pago cancelado\n")
                   input("Operación finalizada. Pulsa Enter para volver al menú principal")
                   break

               # Error al seleccionar confirmacion
               else:
                   input("\nError al seleccionar confirmación. Pulsa Enter para volver\n")


       # Entramos al modo CONSULTAR DATOS

       elif modo_principal == 2:
           print_titulo1("MODO CONSULTAR DATOS", 1)

           # Menú para preguntar si se quieren consultar tarifas o pagos
           print("Introduce el modo (1-2) en el que quieres entrar y presiona Enter:\n")
           print("\t1: Consultar lista de tarifas")
           print("\t2: Consultar lista de pagos\n")

           while 1:
               try:
                   modo_consultar_datos = int(input("Modo: "))
               except ValueError:
                   print ("Debes escribir un número")
               else:
                   break

           # Modo LISTA DE TARIFAS
           if modo_consultar_datos == 1:
               print_titulo1("MODO CONSULTAR DATOS - LISTA DE TARIFAS", 1)

               # Menú para preguntar si se quiere ver el diccionario completo de nombres y tarifas o filtrar
               print("Introduce el modo (1-2) en el que quieres entrar y presiona Enter:")
               print("\t1: Lista completa de tarifas")
               print("\t2: Buscar en la lista de tarifas")
               while 1:
                   try:
                       modo_lista_tarifas = int(input("Modo: "))
                   except ValueError:
                       print ("Debes escribir un número")
                   else:
                       break

               # Modo LISTA COMPLETA DE TARIFAS
               if modo_lista_tarifas == 1:
                   print("Modo seleccionado: Lista completa de tarifas")
                   print("NOMBRE", "\t\t", "TARIFA")
                   for key, value in diccionario_tarifas.items():
                       print(key, "\t", value)

               # Modo BUSCAR EN LISTA DE TARIFAS
               elif modo_lista_tarifas == 2:
                   print("Modo seleccionado: Buscar en la lista de tarifas")

                   print("Introduce el modo (1-2) de búsqueda y presiona Enter:")
                   print("\t1: Nombre")
                   print("\t2: Tarifa")
                   while 1:
                       try:
                           modo_lista_tarifas_buscar = int(input("Modo: "))
                       except ValueError:
                           print ("Debes escribir un número")
                       else:
                           break

                   # Modo BUSCAR EN LISTA DE TARIFAS POR NOMBRE
                   if modo_lista_tarifas_buscar == 1:
                       print("Introduce el nombre exacto a buscar")
                       busq = input("Nombre: ")

                       if busq in diccionario_tarifas:
                           print("NOMBRE", "\t\t", "TARIFA")
                           print(busq, "\t", diccionario_tarifas.get(busq))
                       else:
                           print("No hay coincidencias")

                   # Modo BUSCAR EN LISTA DE TARIFAS POR TARIFA
                   elif modo_lista_tarifas_buscar == 2:
                       print("Introduce la tarifa a buscar en €/mes. Ej: 90")

                       while 1:
                           try:
                               busq = int(input("Tarifa: "))
                           except ValueError:
                               print ("Debes escribir un número")
                           else:
                               break

                       if busq in diccionario_tarifas.values():
                           print("NOMBRE", "\t\t", "TARIFA")
                           for key, value in diccionario_tarifas.items():
                               if value == busq:
                                   print(key, "\t", value)
                       else:
                           print("No hay coincidencias")

                   # Error al seleccionar modo
                   else:
                       print("Error al seleccionar el modo")

               # Error al seleccionar modo
               else:
                   print("Error al seleccionar el modo")

           # Modo LISTA DE PAGOS
           elif modo_consultar_datos == 2:
               print("Modo seleccionado: Lista de pagos")

               # Menú para preguntar si se quiere ver el diccionario completo de pagos o filtrar
               print("Introduce el modo (1-2) en el que quieres entrar y presiona Enter:")
               print("\t1: Lista completa de pagos")
               print("\t2: Buscar en la lista de pagos")
               while 1:
                   try:
                       modo_lista_pagos = int(input("Modo: "))
                   except ValueError:
                       print ("Debes escribir un número")
                   else:
                       break

               # Modo LISTA COMPLETA DE PAGOS
               if modo_lista_pagos == 1:
                   print("Modo seleccionado: Lista completa de pagos")
                   for fecha, nombre in diccionario_pagos.items():
                       print("\nMes:", fecha[4:6], "/", fecha[:4])
                       if not nombre:
                           print("Lista del mes creada pero sin pagos registrados.")
                       else:
                           print("NOMBRE", "\t\t", "CANTIDAD PAGADA", "\t", "FORMA PAGO", "\t", "FECHA PAGO")
                           for key in nombre:
                               print(key, "\t", nombre[key][0], "\t\t\t", nombre[key][1], "\t\t", nombre[key][2])
                   input("\nOperación finalizada. Pulsa Enter para volver al menú principal")


               # Modo BUSCAR EN LISTA DE PAGOS
               elif modo_lista_pagos == 2:
                   print("Modo seleccionado: Buscar en la lista de pagos")

                   print("Introduce el modo (1-5) de búsqueda y presiona Enter:")
                   print("\t1: Mes")
                   print("\t2: Nombre")
                   print("\t3: Cantidad pagada")
                   print("\t4: Forma de pago")
                   print("\t5: Fecha de pago")


                   while 1:
                       try:
                           modo_lista_pagos_buscar = int(input("Modo: "))
                       except ValueError:
                           print ("Debes escribir un número")
                       else:
                           break

                   # Modo BUSCAR EN LISTA DE PAGOS POR MES
                   if modo_lista_pagos_buscar == 1:
                       print("Introduce el mes a buscar (2 cifras)")
                       while 1:
                           try:
                               lista_pagos_buscar_mes_tmp = input("Mes: ").zfill(2)
                               if lista_pagos_buscar_mes_tmp.isdigit() and int(lista_pagos_buscar_mes_tmp) > 0 and int(lista_pagos_buscar_mes_tmp) <=12:
                                   lista_pagos_buscar_mes = lista_pagos_buscar_mes_tmp
                               else:
                                   raise ValueError
                           except ValueError:
                               print ("Debes escribir un número entre 1 y 12")
                           else:
                               break

                       print("Introduce el año a buscar (4 cifras)")
                       while 1:
                           try:
                               lista_pagos_buscar_anio_tmp = input("Año: ").zfill(4)
                               if lista_pagos_buscar_anio_tmp.isdigit() and int(lista_pagos_buscar_anio_tmp) > 0 and int(lista_pagos_buscar_anio_tmp) <=9999:
                                   lista_pagos_buscar_anio = lista_pagos_buscar_anio_tmp
                               else:
                                   raise ValueError
                           except ValueError:
                               print ("Debes escribir un número de cuatro cifras")
                           else:
                               break

                       if lista_pagos_buscar_anio+lista_pagos_buscar_mes in diccionario_pagos:
                           print("Pagos del mes", lista_pagos_buscar_mes, "del año", lista_pagos_buscar_anio)
                           for fecha, registros in diccionario_pagos.items():
                               if fecha == lista_pagos_buscar_anio+lista_pagos_buscar_mes:
                                   if not registros:
                                       print("Lista del mes creada pero sin pagos registrados.")
                                   else:
                                       print("NOMBRE", "\t\t", "CANTIDAD PAGADA", "\t", "FORMA PAGO", "\t", "FECHA PAGO")
                                       for nombre in registros:
                                           print(nombre, "\t", registros[nombre][0], "\t\t\t", registros[nombre][1], "\t\t", registros[nombre][2])
                       else:
                           print("No hay registros del mes", lista_pagos_buscar_mes, "del año", lista_pagos_buscar_anio,", lista del mes no creada")


                   # Modo BUSCAR EN LISTA DE PAGOS POR NOMBRE
                   if modo_lista_pagos_buscar == 2:

                       # Pido nombre del paciente y compruebo si existe en el diccionario de pagos
                       print("Introduce el nombre del paciente")
                       lista_pagos_buscar_nombre = input("Nombre: ")

                       for fecha, registros in diccionario_pagos.items():
                           print("Pagos del mes", fecha[4:], "del año", fecha[:4])
                           for nombre in registros:
                               if lista_pagos_buscar_nombre in nombre:
                                   print("NOMBRE", "\t\t", "CANTIDAD PAGADA", "\t", "FORMA PAGO", "\t", "FECHA PAGO")
                                   if nombre == lista_pagos_buscar_nombre:
                                       print(nombre, "\t", registros[nombre][0], "\t\t\t", registros[nombre][1], "\t\t", registros[nombre][2])
                           if not lista_pagos_buscar_nombre in registros:
                               print("No hay registros coincidentes con el nombre introducido en", fecha[4:], "/", fecha[:4])


                   # Modo BUSCAR EN LISTA DE PAGOS POR CANTIDAD PAGADA
                   elif modo_lista_pagos_buscar == 3:

                       # Pido cantidad pagada y compruebo si hay coincidencias en el diccionario de pagos
                       print("Introduce la cantidad pagada a buscar en €/mes. Ej: 90")
                       while 1:
                           try:
                               lista_pagos_buscar_cantidad = int(input("Cantidad: "))
                           except ValueError:
                               print ("Debes escribir un número")
                           else:
                               break

                       for fecha, registros in diccionario_pagos.items():
                           lista_pagos_buscar_cantidad_aux = 1 # Bandera que se pone a cero con la primera coincidencia del mes
                           print("Pagos del mes", fecha[4:], "del año", fecha[:4])
                           for nombre in registros:
                               if registros[nombre][0] == lista_pagos_buscar_cantidad:
                                   if lista_pagos_buscar_cantidad_aux == 1:
                                       print("NOMBRE", "\t\t", "CANTIDAD PAGADA", "\t", "FORMA PAGO", "\t", "FECHA PAGO")
                                       lista_pagos_buscar_cantidad_aux = 0
                                   print(nombre, "\t", registros[nombre][0], "\t\t\t", registros[nombre][1], "\t\t", registros[nombre][2])
                           if lista_pagos_buscar_cantidad_aux == 1:
                               print("No hay registros coincidentes con la cantidad introducida en", fecha[4:], "/", fecha[:4])


                   # Modo BUSCAR EN LISTA DE PAGOS POR FORMA DE PAGO
                   elif modo_lista_pagos_buscar == 4:

                       # Pido forma de pago y compruebo si hay coincidencias en el diccionario de pagos
                       print("Introduce la forma de pago (1-3) a buscar y presiona Enter:")
                       print("\t1: Efectivo")
                       print("\t2: Tarjeta")
                       print("\t3: Otro")

                       while 1:
                           try:
                               lista_pagos_buscar_metodo = int(input("Forma de pago: "))
                           except ValueError:
                               print ("Debes escribir un número")
                           else:
                               break

                       # Conversion del numero seleccionado al texto correspondiente
                       if lista_pagos_buscar_metodo == 1:
                           lista_pagos_buscar_metodo = "Efectivo"
                           print("Forma de pago elegida: Efectivo")
                       elif lista_pagos_buscar_metodo == 2:
                           lista_pagos_buscar_metodo = "Tarjeta"
                           print("Forma de pago elegida: Tarjeta")
                       elif lista_pagos_buscar_metodo == 3:
                           lista_pagos_buscar_metodo = "Otro"
                           print("Forma de pago elegida: Otro")
                       else:
                           print("Error al seleccionar la forma de pago")
                           break

                       for fecha, registros in diccionario_pagos.items():
                           lista_pagos_buscar_metodo_aux = 1 # Bandera que se pone a cero con la primera coincidencia del mes
                           print("Pagos del mes", fecha[4:], "del año", fecha[:4])
                           for nombre in registros:
                               if registros[nombre][1] == lista_pagos_buscar_metodo:
                                   if lista_pagos_buscar_metodo_aux == 1:
                                       print("NOMBRE", "\t\t", "CANTIDAD PAGADA", "\t", "FORMA PAGO", "\t", "FECHA PAGO")
                                       lista_pagos_buscar_metodo_aux = 0
                                   print(nombre, "\t", registros[nombre][0], "\t\t\t", registros[nombre][1], "\t\t", registros[nombre][2])
                           if lista_pagos_buscar_metodo_aux == 1:
                               print("No hay registros coincidentes con la forma de pago introducida en", fecha[4:], "/", fecha[:4])


                   # Modo BUSCAR EN LISTA DE PAGOS POR FECHA
                   if modo_lista_pagos_buscar == 5:

                       # Pregunto si se quiere usar la fecha de hoy y si no pido fecha a buscar
                       print("¿Usar la fecha de hoy para la búsqueda?")
                       print("\t1: Sí, usar", time.strftime("%d/%m/%Y"))
                       print("\t2: No, elegir otra fecha")

                       while 1:
                           try:
                               modo_lista_pagos_buscar_fecha = int(input())
                           except ValueError:
                               print ("Debes escribir un número")
                           else:
                               break

                       # Fecha de hoy
                       if modo_lista_pagos_buscar_fecha == 1:
                           print("Fecha escogida:", time.strftime("%d/%m/%Y"))
                           lista_pagos_buscar_fecha = time.strftime("%d/%m/%Y")
                           lista_pagos_buscar_fecha_anio = time.strftime("%Y")
                           lista_pagos_buscar_fecha_mes = time.strftime("%m")
                           lista_pagos_buscar_fecha_dia = time.strftime("%d")

                       # Otra fecha
                       elif modo_lista_pagos_buscar_fecha == 2:
                           print("Introduce la fecha a buscar")
                           print("Introduce el día a buscar (2 cifras)")
                           while 1:
                               try:
                                   lista_pagos_buscar_fecha_dia_tmp = input("Día: ").zfill(2)
                                   if lista_pagos_buscar_fecha_dia_tmp.isdigit() and int(lista_pagos_buscar_fecha_dia_tmp) > 0 and int(lista_pagos_buscar_fecha_dia_tmp) <=31:
                                       lista_pagos_buscar_fecha_dia = lista_pagos_buscar_fecha_dia_tmp
                                   else:
                                       raise ValueError
                               except ValueError:
                                   print ("Debes escribir un número entre 1 y 31")
                               else:
                                   break

                           print("Introduce el mes a buscar (2 cifras)")
                           while 1:
                               try:
                                   lista_pagos_buscar_fecha_mes_tmp = input("Mes: ").zfill(2)
                                   if lista_pagos_buscar_fecha_mes_tmp.isdigit() and int(lista_pagos_buscar_fecha_mes_tmp) > 0 and int(lista_pagos_buscar_fecha_mes_tmp) <=12:
                                       lista_pagos_buscar_fecha_mes = lista_pagos_buscar_fecha_mes_tmp
                                   else:
                                       raise ValueError
                               except ValueError:
                                   print ("Debes escribir un número entre 1 y 12")
                               else:
                                   break

                           print("Introduce el año a buscar (4 cifras)")
                           while 1:
                               try:
                                   lista_pagos_buscar_fecha_anio_tmp = input("Año: ").zfill(4)
                                   if lista_pagos_buscar_fecha_anio_tmp.isdigit() and int(lista_pagos_buscar_fecha_anio_tmp) > 0 and int(lista_pagos_buscar_fecha_anio_tmp) <=9999:
                                       lista_pagos_buscar_fecha_anio = lista_pagos_buscar_fecha_anio_tmp
                                   else:
                                       raise ValueError
                               except ValueError:
                                   print ("Debes escribir un número de cuatro cifras")
                               else:
                                   break

                           lista_pagos_buscar_fecha = lista_pagos_buscar_fecha_dia+"/"+lista_pagos_buscar_fecha_mes+"/"+lista_pagos_buscar_fecha_anio

                       # Error al seleccionar fecha
                       else:
                           print("Error al seleccionar la fecha")


                       # Ya tengo la fecha guardada en sus variables, venga de donde venga. Procedo a buscar
                       if lista_pagos_buscar_fecha_anio+lista_pagos_buscar_fecha_mes in diccionario_pagos:
                           print("Pagos del mes", lista_pagos_buscar_fecha_mes, "del año", lista_pagos_buscar_fecha_anio)
                           for fecha, registros in diccionario_pagos.items():
                               lista_pagos_buscar_fecha_aux = 1
                               if fecha == lista_pagos_buscar_fecha_anio+lista_pagos_buscar_fecha_mes:
                                   if not registros:
                                       print("Lista del mes creada pero sin pagos registrados.")
                                   else:
                                       for nombre in registros:
                                           if registros[nombre][2] == lista_pagos_buscar_fecha:
                                               if lista_pagos_buscar_fecha_aux == 1:
                                                   print("NOMBRE", "\t\t", "CANTIDAD PAGADA", "\t", "FORMA PAGO", "\t", "FECHA PAGO")
                                                   lista_pagos_buscar_fecha_aux = 0
                                               print(nombre, "\t", registros[nombre][0], "\t\t\t", registros[nombre][1], "\t\t", registros[nombre][2])
                                   if lista_pagos_buscar_fecha_aux == 1:
                                       print("No hay registros coincidentes con la fecha de pago introducida en", fecha[4:], "/", fecha[:4])
                       else:
                           print("No hay registros del mes", lista_pagos_buscar_fecha_mes, "del año", lista_pagos_buscar_fecha_anio,", lista del mes no creada")


           # Error al seleccionar modo
           else:
               print("Error al seleccionar el modo")

       # Entramos al modo MODIFICAR DATOS

       elif modo_principal == 3:
           print_titulo1("MODO MODIFICAR DATOS", 1)

           # Menú para preguntar si se quieren modificar tarifas o pagos
           print("Introduce el modo (1-2) en el que quieres entrar y presiona Enter:")
           print("\t1: Modificar lista de tarifas")
           print("\t2: Modificar lista de pagos")

           while 1:
               try:
                   modo_modificar_datos = int(input("Modo: "))
               except ValueError:
                   print ("Debes escribir un número")
               else:
                   break

           # Modo modificar LISTA DE TARIFAS
           if modo_modificar_datos == 1:
               print("Modo seleccionado: Modificar lista de tarifas")
               print("Introduce el modo (1-3) en el que quieres entrar y presiona Enter:")
               print("\t1: Añadir registro a la lista de tarifas")
               print("\t1: Modificar registro de la lista de tarifas")
               print("\t1: Eliminar registro de la lista de tarifas")

               while 1:
                   try:
                       modo_modificar_datos_tarifas = int(input("Modo: "))
                   except ValueError:
                       print("Debes escribir un número")
                   else:
                       break

               # Modo AÑADIR REGISTRO A LISTA DE TARIFAS
               if modo_modificar_datos_tarifas == 1:
                   while 1:
                       print("Modo seleccionado: Añadir registro a la lista de tarifas")

                       # Pido el nombre del paciente y compruebo que al menos tiene 10 caracteres
                       print("Introduce el nombre del paciente (Ej: Marcos Pérez Martín)")
                       modo_modificar_datos_tarifas_aniadir_nombre = input("Nombre: ")
                       if len(modo_modificar_datos_tarifas_aniadir_nombre) >= 5:
                           break
                       else:
                           input("\nNombre demasiado corto. Pulsa Enter para volver")

                   print("Introduce la tarifa mensual del paciente (Ej: 50)")
                   modo_modificar_datos_tarifas_aniadir_tarifa = input("Tarifa: ")

                   print("Se va a introducir un nuevo pago con los siguientes datos: ")
                   print("Nombre: ",  modo_modificar_datos_tarifas_aniadir_nombre)
                   print("Tarifa: ", modo_modificar_datos_tarifas_aniadir_tarifa)
                   print("¿Confirmar?")
                   print("\t1: Sí")
                   print("\t2: No")

                   while 1:
                       try:
                           modo_modificar_datos_tarifas_aniadir_confirmar = int(input())
                       except ValueError:
                           print ("Debes escribir un número")
                       else:
                           break

                   # Confirmar introduccion registro en lista tarifas
                   if modo_modificar_datos_tarifas_aniadir_confirmar == 1:
                       # AQUI HAY QUE COMPROBAR QUE ESE NOMBRE NO EXISTA YA
                       diccionario_tarifas[modo_modificar_datos_tarifas_aniadir_nombre] = modo_modificar_datos_tarifas_aniadir_tarifa
                       print("Nuevo registro introducido")

                   # Cancelar introduccion registro
                   elif modo_modificar_datos_tarifas_aniadir_confirmar == 2:
                       print("Añadir nuevo registro cancelado")

                   # Error al seleccionar confirmacion
                   else:
                       print("Error al seleccionar confirmación")

                   if Config.modo_diccionarios == 1:
                       print("Guardando datos de tarifas...")
                       guardar_datos_tarifas(diccionario_tarifas)
                       print("Datos de tarifas guardados")
                       print("Guardando datos de pagos...")
                       guardar_datos_pagos(diccionario_pagos)
                       print("Datos de pagos guardados")

                   print("Operación finalizada")
                   print("\t1: Volver al menú principal")
                   print("\t2: Volver al menú de nuevo pago")
                   print("\t3: Salir de la aplicación")


           elif modo_modificar_datos == 2:
               print("Modo seleccionado: Modificar lista de pagos")
           else:
               print("Error al seleccionar el modo")


       # Entramos al modo GENERAR INFORME
       elif modo_principal == 4:
           print_titulo1("MODO GENERAR INFORME", 1)

       # Entramos al modo NUEVO MES
       elif modo_principal == 5:
           print_titulo1("MODO NUEVO MES", 1)

           mes = time.strftime("%m")
           anio = time.strftime("%Y")

           while 1:
               print("Mes: ", mes)
               print("Año: ", anio)
               print("\n¿Quieres crear la lista con los datos anteriores?")
               print("\t1: Sí, crear la lista")
               print("\t2: No, modificar datos\n")

               while 1:
                   try:
                       modo_nuevo_mes = int(input("Opción: "))
                   except ValueError:
                       print ("Debes escribir un número")
                   else:
                       break

               # Modo GENERAR LISTA NUEVO MES
               if modo_nuevo_mes == 1:
                   # AQUI DEBEMOS COMPROBAR QUE NO EXISTA EL ARCHIVO DEL MES YA EN EL DICCIONARIO DE PAGOS
                   diccionario_pagos[anio+mes] = {}
                   print(diccionario_pagos)
                   print("Lista del mes", mes, "del año", anio, "creada satisfactoriamente")
                   if Config.modo_diccionarios == 1:
                       print("Guardando datos de tarifas...")
                       guardar_datos_tarifas(diccionario_tarifas)
                       print("Datos de tarifas guardados")
                       print("Guardando datos de pagos...")
                       guardar_datos_pagos(diccionario_pagos)
                       print("Datos de pagos guardados")
                   break

               elif modo_nuevo_mes == 2:
                   print("Escribe el número del mes del que deseas crear la lista (2 cifras)")
                   while 1:
                       try:
                           mes_tmp = input("Mes: ").zfill(2)
                           if mes_tmp.isdigit() and int(mes_tmp) > 0 and int(mes_tmp) <=12:
                               mes = mes_tmp
                           else:
                               raise ValueError
                       except ValueError:
                           print ("Debes escribir un número entre 1 y 12")
                       else:
                           break

                   print("Escribe el número del año del que deseas crear la lista (4 cifras)")
                   while 1:
                       try:
                           anio_tmp = input("Año: ").zfill(4)
                           if anio_tmp.isdigit() and int(anio_tmp) > 0 and int(anio_tmp) <=9999:
                               anio = anio_tmp
                           else:
                               raise ValueError
                       except ValueError:
                           print ("Debes escribir un número de cuatro cifras")
                       else:
                           break

       # Entramos al modo SALIR
       elif modo_principal == 6:
           if Config.modo_diccionarios == 1:
               print("\nGuardando datos de tarifas...")
               guardar_datos_tarifas(diccionario_tarifas)
               print("Datos de tarifas guardados")
               print("Guardando datos de pagos...")
               guardar_datos_pagos(diccionario_pagos)
               print("Datos de pagos guardados\n")

               input("Pulsa Enter para cerrar el programa")
               os.system('cls')
           break

       # Error al entrar al modo
       else:
           print("Error al seleccionar el modo")


    # In[ ]:





    # In[ ]:
