#!/usr/bin/env python
# coding: utf-8

# In[4]:


# PySBM - Python Small Business Management
# v1.0
# 18/01/2019
# Marcos Pérez Martín

# Configuration of the program. On future versions maybe a different file that
# can be changed inside program and loaded to have all variables.

#from EM import *
#from PM import *


#######################################################################

# Program flow

while 1:
    print("PySMB")

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
    print("\t8: Salir")

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
        print("1")

    # Entramos al modo PAGOS DE CLIENTES
    elif modo == 2:
        print("2")

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
        print("8")
        
    # Error al seleccionar modo
    else:       
        print("Error al seleccionar el modo")
        


# In[ ]:




