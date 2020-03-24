# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 08:19:49 2020

@author: IvyGonz
"""
#Para acceder al menu de administrador, escriba 'Admin' e ingrese los siguientes datos:
#Nombre: Valentina
#Contraseña: 1234

class Registro:
    def __init__ (self):
        pass
    
    @staticmethod
    def inicio_sesion ():
        Menu = Registro
        print("")
        print("        =====================")
        print("        | Ingrese sus datos |")
        print("        =====================")
        print("")
        Nombre = str(input("Nombre: "))
        Contraseña = input("Contraseña: ")
        if Nombre+'\n' == open("Nombre.txt").read() and Contraseña == open("Contraseña.txt").read():
            print("Bienvenido", Nombre)
            Menu.calculadora()
        else:
            print("Usuario no registrado.")
            Menu1()

    @staticmethod
    def registrar ():
        archivo = 'Nombre.txt'
        with open(archivo, 'a') as f:
            f.write(input("Ingrese su Nombre: ") + '\n')
        archivo = 'Apellido.txt'
        with open(archivo, 'a') as f:
            f.write(input("Ingrese su Apellido: "))
        archivo = 'Correo.txt'
        with open(archivo, 'a') as f:
            f.write(input("Ingrese su correo electronico: "))
        archivo = 'Contraseña.txt'
        with open(archivo, 'a') as f:
            f.write(input("Ingrese su contraseña: "))
        Menu1()
        
    @staticmethod
    def mostrarA ():
        archivo = open('Nombre.txt', 'r')
        cadena = archivo.read()
        archivo.close()
        print(cadena)
        
    @staticmethod
    def calculadora ():
        Menu = Registro
        print("")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("| OPERACIONES ARITMETICAS BASICAS |")
        print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
        print("")
        print('Ingrese su primer numero: ')
        n1 = int(input())
        print('Ingrese su segundo numero: ')
        n2 = int(input())
        print("""Que desea hacer con estos numeros?
            1) Sumar 
            2) Restar
            3) Multiplicar
            4) Dividir""")
        opc = input()
        if opc == '1':
            resultado = n1 + n2
        elif opc == '2':
            resultado = n1 - n2
        elif opc == '3':
            resultado = n1 * n2
        elif opc == '4':
            resultado = n1 / n2
        else:
            print("Comando desconocido, vuelva a intentarlo.")
        print("Resultado: ", resultado)
        print("")
        print("¿Desea cerrar sesion? S/N")
        opcion = input().upper()
        if opcion == 'S':
            Menu.calculadora()
        if opcion == 'N':
            Menu1()


def Menu1 ():
    Menu = Registro
    print("")
    print("          =================")
    print("""          |  ¡Bienvenido! |
          =================
          ¿Que desea hacer?
          1- Registrarme
          2- Iniciar sesion
          0- Salir """)
    opcion = input()
    if opcion == '1':
        Menu.registrar()
    elif opcion == '2':
        Menu.inicio_sesion()
    elif opcion == 'Admin':
        print("        =====================")
        print("        | Ingrese los datos |")
        print("        =====================")
        print("")
        print("Ingrese el nombre de administrador: ")
        Admin_Nombre = input()
        if Admin_Nombre == 'Valentina':
            print("Ingrese la contraseña de administrador: ")
            Admin_Contraseña = input()
            if Admin_Contraseña == '1234':
                print("    =============================================")
                print("    ||  ¡Bienvenido al menu de Administrador!  ||")
                print("    =============================================")
                print("""¿Que desea hacer?
                1- Mostrar los usuarios registrados 
                0- Volver """)
                opcion1 = input()
                if opcion1 == '1':
                    print("Estos son los usuarios registrados: ")
                    Menu.mostrarA()
                else:
                    Menu1()
            else:
                print("Contraseña invalida.")
                Menu1()
        else:
            print("Usuario no valido.")
            Menu1()
    else:
        print("Vuelva pronto :D")
        
Menu1()