import numpy as np
import os
import msvcrt
arreglo_mesas = np.zeros((3,3), int)
#{===================================COLORES======================================================}
class bcolor:
    G = '\033[92m'
    R = '\033[91m'
    reset = '\033[0m'
#{====================================RUTS========================================================}
def vali_ruts():
    while True:
        try:
            rut = int(input("\nIngrese su Rut: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print(bcolor.R + "Rut no valido" + bcolor.reset)
        except:
            print (bcolor.R + "Formato de Rut no valido" + bcolor.reset)
#{===================================NOMBRES======================================================}
def vali_nombres():
    while True:
        nombre = input("\nIngrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha:
            return nombre
        else:
            print(bcolor.R + "Nombre mal ingresado, reintente con 3 letras o más" + bcolor.reset)
#{===================================CORREOS======================================================}
def vali_correos():
    while True:
        correo = input("\nIngrese su correo: ")
        if "@" in correo:
            return correo
        else:
            print(bcolor.R + "El formato de correo no es valido" + bcolor.reset)
#{===================================OPCIONES=====================================================}
def vali_opcion():
    while True:
        try:
            opci = int(input("Ingrese una opción: "))
            if opci in (1,2,3,4,5,6):
                return opci
            else:
                print(bcolor.R+ "Opcion no valida, reintente" +bcolor.reset)
        except:
            print(bcolor.R+ "Debe ingresar un numero de opcion" +bcolor.reset)
            os.system('cls')
#{=====================================EDAD=======================================================}
def vali_edad():
    while True:
        try:
            edad = int(input("\nIngrese su Edad: "))
            if edad >= 5 and edad <= 120:
                return edad
            else:
                print(bcolor.R + "Usted no puede manejar este programa" + bcolor.reset)
        except:
            print (bcolor.R + "???" + bcolor.reset)
#{================================================================================================}
def ver_restaurant():
        os.system ('cls')
        print("  = Mostrando mesas del Restaurante =")
        print("")
        for x in range(3): #filas
            print(f"Mesas de {(x+1)*2}  |", end=" ")
            for y in range(3): #columnas
                if arreglo_mesas [x][y] == 0:
                    print (bcolor.G + f"{arreglo_mesas[x][y]}", end=" " + bcolor.reset)
                else:
                    print (bcolor.R + f"{arreglo_mesas[x][y]}", end=" " + bcolor.reset)
            print ()
        print("\t    ---------")
        print("\t    | 1 2 3 |")
        print("")
        print(bcolor.G + "Presione una tecla para continuar" + bcolor.reset)
        msvcrt.getch()
#{================================================================================================}
def cant_personas():
    while True:
        try:
            cant_pers = int(input("\nIngrese la cantidad de personas: "))
            if cant_pers >= 1 and cant_pers <= 6:
                return cant_pers
            else:
                print(bcolor.R + "Rut no valido" + bcolor.reset)
        except:
            print (bcolor.R + "Formato de Rut no valido" + bcolor.reset)
#{================================================================================================}
#{================================================================================================}