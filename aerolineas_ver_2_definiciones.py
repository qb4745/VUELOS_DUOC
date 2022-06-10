import string
import numpy as np

lista_asientos = [str(x) for x in range(1,43)]
lista_datos = ["Nombre:   ", "RUT:      ", "Celular:  ", "Banco:    ", "Asiento:  "]
ar_asi = np.array(lista_asientos).reshape(7,6)
anular_asiento = "0"
asientos_vendidos = []
simbolos = "0123456789+-*/=¿?¡!"
datos_pasajero = []
lista_grupo = ["Miembro Número 1:   ", "Miembro Número 2:   ","Miembro Número 3:   ","Miembro Número 4:   ","Miembro Número 5:   "]
nombres_grupo = ["Bóris Arriagada", "Ana González", "Esteban Rojas", "Guillermo Velasquez", "Jaime Vicencio"]

def MuestraAsientos(ar_asi): #dibuja los asientos disponibles

    print("                         ASIENTOS DISPONIBLES")
    print()
    print("|	 "+ ar_asi[0][0] +"	 "+ ar_asi[0][1] +"	 "+ ar_asi[0][2]+"		 "+ ar_asi[0][3] +"	 "+ ar_asi[0][4] +"	 "+ ar_asi[0][5] +"	|")
    print("|								|")
    print("|	 "+ ar_asi[1][0] +"	 "+ ar_asi[1][1] +"	 "+ ar_asi[1][2]+"              "+ ar_asi[1][3] +"	"+ ar_asi[1][4] +"	"+ ar_asi[1][5] +"	|")
    print("|								|")
    print("|	"+ ar_asi[2][0] +"	"+ ar_asi[2][1] +"	"+ ar_asi[2][2]+"              "+ ar_asi[2][3] +"	"+ ar_asi[2][4] +"	"+ ar_asi[2][5] +"	|")
    print("|								|")
    print("|	"+ ar_asi[3][0] +"	"+ ar_asi[3][1] +"	"+ ar_asi[3][2]+"              "+ ar_asi[3][3] +"	"+ ar_asi[3][4] +"	"+ ar_asi[3][5] +"	|")
    print("|								|")
    print("|	"+ ar_asi[4][0] +"	"+ ar_asi[4][1] +"	"+ ar_asi[4][2]+"              "+ ar_asi[4][3] +"	"+ ar_asi[4][4] +"	"+ ar_asi[4][5] +"	|")
    print("|_______________________________________________________________|")
    print("|_______________________________________________________________|")
    print("|	"+ ar_asi[5][0] +"	"+ ar_asi[5][1] +"	"+ ar_asi[5][2]+"              "+ ar_asi[5][3] +"	"+ ar_asi[5][4] +"	"+ ar_asi[5][5] +"	|")
    print("|								|")
    print("|								|")
    print("|	"+ ar_asi[6][0] +"	"+ ar_asi[6][1] +"	"+ ar_asi[6][2]+"              "+ ar_asi[6][3] +"	"+ ar_asi[6][4] +"	"+ ar_asi[6][5] +"	|")
    print()

def Array_Asientos(asientos_vendidos): #actualiza el array de asientos disponibles
    global ar_asi
    lista_asientos = [str(x) for x in range(1,43)]
    ar_asi = np.array(lista_asientos).reshape(7,6)
    for asiento_vendido in asientos_vendidos:
        for fila in range(7):
            for asiento in range(6):
                if asiento_vendido == ar_asi[fila][asiento]:
                    ar_asi[fila][asiento] = "X"
    return ar_asi         

def Comprar_Pasajes(descuento_banco):
    global asientos_vendidos
    global num_asiento
    global datos_pasajero
    while True:
        print("Elija el número de asiento a comprar.\nAsientos del 1 al 30  - $78,900   - Clase Normal.\nAsientos del 31 al 42  - $240,000   - Clase VIP.")   
        try:
            num_asiento = int(input())
            if num_asiento >= 1 and num_asiento <= 42:
                num_asiento = str(num_asiento)
                if num_asiento not in asientos_vendidos:
                    num_asiento = int(num_asiento)
                    if num_asiento >=1 and num_asiento <= 30:
                        num_asiento = str(num_asiento)
                        pasaje_clase = "Clase Normal"
                        pasaje_precio = 78_900
                    else:
                        num_asiento = str(num_asiento)
                        pasaje_clase = "Clase VIP"
                        pasaje_precio = 240_000
                else:
                    print("Número de asiento ya está reservado, elija otro por favor.\n")
            print(f"El número de asiento '{num_asiento}' pertenece a '{pasaje_clase}', con un valor de ${pasaje_precio:,}.")
            if descuento_banco == 0.85:
                print(f"Por ser Miembro BancoDUOC, obtiene un 15% de descuento.\nTotal a pagar ${round(pasaje_precio*0.85):,}.\n")
            print("¿Desea continuar?\n1.- SI.\n2.- NO.")
            try:
                compra_opcion = int(input())
                print(compra_opcion)
                if compra_opcion >=1 and compra_opcion <=2:
                    if compra_opcion == 1:
                        num_asiento = str(num_asiento)
                        asientos_vendidos.append(num_asiento)
                        print("2")
                        return num_asiento
                    else:
                        print("Elija otro asiento para cambiar la tarifa.\n")
                else:
                    Comprar_Pasajes(descuento_banco) 
            except:
                print("ex-num asiento Opción no válida. Vuelva a intentarlo.\n")
        except:
            print(" Opción no válida. Vuelva a intentarlo.\n")
            
            
def Anular_Pasaje():
    global datos_pasajero
    print("Digite numero de asiento para anular compra.\nNota: Si anula pasaje se eliminaran todos los datos relacionado con esa compra.\n")
    try:
        anular_asiento = int(input())
        if anular_asiento >= 1 and anular_asiento <= 42:
            anular_asiento = str(anular_asiento)
            if anular_asiento in asientos_vendidos:
                asientos_vendidos.remove(anular_asiento)
                datos_pasajero = []
                Array_Asientos(asientos_vendidos)
                print("Anulación Exitosa.\n")
                return datos_pasajero
            else:
                print("Asiento no está reservado. Vuelva a intentarlo.\n")
        else:
            print("Número de asiento no es válido. Vuelva a intentarlo.\n")
    except:
        print("Opción no válida, vuelva a intentarlo.\n")

def Modificar_Datos(datos_pasajero): #submenu de modificacion de datos
    try:
        mod_asiento, mod_rut = [int(x) for x in input("Para Modificar datos, ingrese numero de asiento seguido de rut del comprador sin digito verificador ni puntos.\nEjemplo 13 13912058 \n").split()]
        mod_asiento = str(mod_asiento)
        mod_rut = str(mod_rut)
        if mod_asiento in asientos_vendidos and mod_rut in datos_pasajero:
            while True:
                print(f"¿Que dato desea modificar?\nDigite el número de la opción que necesite modificar.  Ejemplo: 1\n1.- {lista_datos[0]}{datos_pasajero[0]}.\n2.- {lista_datos[2]}{datos_pasajero[2]}.\n3.- Salir.\n")
                try:
                    modificar_opcion = int(input())
                    if modificar_opcion >=1 and modificar_opcion <=3:
                        if modificar_opcion == 1:
                            print("Ingrese el nombre para la modificacíon.\n")
                            nombre = input()
                            nombre = str(nombre.upper())
                            nombre_check2 = []
                            nombre_check2 = [x for x in nombre if x in simbolos]
                            if nombre_check2 == []:
                                datos_pasajero[0] = nombre.upper()
                        if modificar_opcion == 2:
                            print("Ingrese numero de celular para modificar la reserva.\n")
                            celular = int(input())
                            if celular >= 1_000_000 and celular <= 999_999_999:
                                celular = str(celular)
                                datos_pasajero[2] = celular
                            print("Datos reserva:")
                            for dato_requerido,dato_pasajero in zip(lista_datos,datos_pasajero):
                                print(dato_requerido,dato_pasajero)
                        if modificar_opcion == 3:
                            break
                except:
                    print("Opción no es válida, intente nuevamente.\n")

                print("Ingrese numero de celular para modificar la reserva.\n")       
        else:
            print("Datos ingresados no concuerdan con reservaciones.  Vuelva a intentarlo.\n")
    except:
        print("Opción no válida, vuelva a intentarlo.")


def Menu_Principal():
    global datos_pasajero
    while True:
        print("*"*5, "Bienvenido a Vuelos-Duoc","*"*5)
        print("1.- Ver asientos disponibles.\n2.- Comprar asiento.\n3.- Anular vuelo.\n4.- Modificar datos de pasajero.\n5.- Salir.\n")
        try:
            menu_opcion = int(input())
            if menu_opcion >= 1 and menu_opcion <=5:
                if menu_opcion == 1:
                    MuestraAsientos(ar_asi)
                if menu_opcion == 2:
                    print("*"*5, "Comprar Asiento","*"*5)
                    while True:
                        print("Ingrese nombre.\n")
                        compra_nombre = input()
                        compra_nombre = compra_nombre.upper()
                        nombre_check = [x for x in compra_nombre if x in simbolos]
                        if nombre_check == []:
                            datos_pasajero = []
                            datos_pasajero.append(compra_nombre)
                            break
                        else:
                            print("Nombre ingresado no es válido, intente nuevamente.\n")
                    while True:
                        print("Ingrese RUT (sin puntos ni guión):\n")
                        try:                
                            compra_rut = int(input())
                            if compra_rut >= 5000000 and compra_rut <= 99999999:
                                datos_pasajero.append(str(compra_rut))
                                break
                            else:
                                print("Ingreso de RUT incorrecto, intente nuevamente.\n")
                        except:
                            print("Ingreso de RUT incorrecto, intente nuevamente.\n")
                    while True:
                        print("Ingrese Número de Celular. Ejemplo. 945081197\n")                
                        try:                
                            compra_celular = int(input())
                            if compra_celular >= 1000000 and compra_celular <= 999999999:
                                datos_pasajero.append(str(compra_celular))
                                break
                            else:
                                print("Ingreso de Número de Celular incorrecto, intente nuevamente.\n")
                        except:
                            print("Ingreso de Número de Celular incorrecto, intente nuevamente.\n")
                    while True:
                        print("¿Es usted miembro de 'BancoDuoc'?. Digite 1 para SI, 2 para NO.\n1.- SI.\n2.- NO.")
                        try:
                            compra_op_banco = int(input())
                            if compra_op_banco >= 1 and compra_op_banco <=2:
                                if compra_op_banco == 1:
                                    datos_pasajero.append("Miembro BancoDUOC")
                                    descuento_banco = 0.85
                                    break
                                if compra_op_banco == 2:
                                    descuento_banco = 1
                                    datos_pasajero.append("Otro Banco")
                                    break
                            else:
                                print("Opción no Válida, vuelva a intentarlo\n")
                        except:
                            print("except banco.Opción no Válida, vuelva a intentarlo")
                            
                    while True:
                        Comprar_Pasajes(descuento_banco)
                        datos_pasajero.append(num_asiento)
                        print("Datos reserva:")
                        for dato_requerido,dato_pasajero in zip(lista_datos,datos_pasajero):
                            print(dato_requerido,dato_pasajero)
                        print()
                        Array_Asientos(asientos_vendidos)
                        break                           
                if menu_opcion == 3:
                    Anular_Pasaje()
                if menu_opcion == 4:
                    Modificar_Datos(datos_pasajero)
                if menu_opcion == 5:
                    print("Realizado para PROGRAMACION DE ALGORITMOS_002V - DUOC Viña del Mar.\nProfesor: HERNAN SAAVEDRA.\n\n\t\tMiembros Del Grupo.\n")
                    for miembro,nombre in zip(lista_grupo,nombres_grupo):
                        print(miembro,nombre)
                    break
            else:
                print("Número de opción no es válida.  Intente nuevamente.\n")

        except:
            print("Número de opción no es válida.  Intente nuevamente.\n")

