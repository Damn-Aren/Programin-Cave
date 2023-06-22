import time
from funciones_utilizables import *
#{=========================================================================================}
os.system('cls')
#{=========================================================================================}
list_Bebidas = [] # Jugos Caseros - Bebidas express - Cerveza lata
list_Postres = [] # Rebanada Torta casera - Banana Split - menú infantil
list_PlatosP = [] # Lomo Vetado con Papas Duquesas - Fideos con Salsa y albondigas - Chorrillana
#{-----------------------------------------------------------------------------------------}
list_ruts = []
list_nombres = []
list_correos = []
list_cant_pers = []
list_fila = []
list_columna = []
#{=========================================================================================}
while True:
    os.system ('cls')
    print ("""
    Menú restaruante:
    {====== Menú restaruante: =======}
    1.- Ver la sala
    2.- Reserva de mesa
    3.- Carta // menu bebidas platos postre pedir cancelar
    {================================}
    4.- Ejecutar compra
    5.- Cancelar compra

    6.- SALIR 
    {================================}
    """)
#{=========================================================================================}
    opci = vali_opcion()
#{=========================================================================================}
    if opci == 1:
        print (ver_restaurant())
#{=========================================================================================}
    elif opci == 2:
        rut = vali_ruts()
        nombre = vali_nombres()
        correo = vali_correos()
#{-----------------------------------------------------------------------------------------}
        list_ruts.append (rut)
        list_nombres.append (nombre)
        list_correos.append (correo)
#{-----------------------------------------------------------------------------------------}
        cant_personas()
#{-----------------------------------------------------------------------------------------}
        ver_restaurant()
        while True:
            try:
                fila = int(input("Ingrese la fila a comprar: "))
                if fila in (1,2,3):
                    break
                else:
                    print(bcolor.R + "Fila no existente" + bcolor.reset)
            except:
                print(bcolor.R + "Debe ingresar el numero de Fila" + bcolor.reset)
#{-----------------------------------------------------------------------------------------}
        while True:
            try:
                columna = int(input("Ingrese la columna a comprar: "))
                if columna in (1,2,3):
                    break
                else:
                    print(bcolor.R + "Columna no existente" + bcolor.reset)
            except:
                print(bcolor.R + "Debe ingresar el numero de Fila" + bcolor.reset)
#{-----------------------------------------------------------------------------------------}
        if arreglo_mesas[fila-1][columna-1] == 0:
            arreglo_mesas[fila-1][columna-1] = 1
            list_fila.append(fila-1)
            list_columna.append(columna-1)
            print(bcolor.G + "Registro realizado con exito!" + bcolor.reset)
            time.sleep(3)
        else:
            print (bcolor.R + "Su asiento esta ocpuado actualmente" + bcolor.reset)
            time.sleep(3)
#{=========================================================================================}
    elif opci == 3:
        while True:
            os.system ('cls')
            print("""
            {========= Carta =========}
            1.- Bebidas
            2.- Platos Principales
            3.- Postres

            4.- Ordenar
            5.- Cancelar orden
            {=========================}
            """)
#{-----------------------------------------------------------------------------------------}
            while True:
                try:
                    selec = int(input("Ingrese una opción: "))
                    if selec in (1,2,3,4,5):
                        break
                    else:
                        print(bcolor.R+ "Opcion no valida, reintente" +bcolor.reset)
                except:
                    print(bcolor.R+ "Debe ingresar un numero de opcion" +bcolor.reset)
                    os.system('cls')
#{-----------------------------------------------------------------------------------------}
            if selec == 1:
                pass
#{-----------------------------------------------------------------------------------------}
            elif selec == 2:
                pass
#{-----------------------------------------------------------------------------------------}
            elif selec == 3:
                pass
            elif selec == 4:
                pass
#{-----------------------------------------------------------------------------------------}
            elif selec == 5:
                pass
#{=========================================================================================}
    elif opci == 4:
        pass
#{=========================================================================================}
    elif opci == 5:
        pass
#{=========================================================================================}
    else:
        break
