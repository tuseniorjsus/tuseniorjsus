from os import system
from datetime import datetime
import csv
import os


cliente_archivo = "cliente.csv"
producto_archivo = "producto.csv"


def get_current_date_time():
    today = datetime.now()
    today = today.strftime("%d/%m/%Y-%H:%M:%S")
    return today


class Empleados():
    def __init__(self, id_empleado, nombre_empleado, edad, genero, puesto, clientes_cargo=""):
        self.id_empleado = id_empleado
        self.nombre = nombre_empleado
        self.edad = edad
        self.genero = genero
        self.puesto = puesto
        self.clientes_cargo = [clientes_cargo]
        self.estaHabilitado = True

    def imprimirT(self):
        print(
            f"ID:{self.id_empleado} Nombre: {self.nombre} Edad:{self.edad} Genero:{self.genero}")
        print(
            f"Puesto:{self.puesto} Cargo:{self.clientes_cargo} Estatus:{self.estaHabilitado}")
        print("----------------------------------------------------------------------------------------\n")


class Clientes():
    def __init__(self, id_cliente, nombre_clientes, rfc, domicilio, contacto, nombre_responsable):
        self.id_cliente = id_cliente
        self.nombre = nombre_clientes
        self.esMoral = True
        self.RFC = rfc
        self.domicilio = domicilio
        self.contacto = contacto
        self.nombre_responsable = nombre_responsable

    def imprimirCliente(self):
        print(f"ID: {self.id_cliente} - Nombre:{self.nombre} - RFC:{self.RFC}")
        print(
            f"Domicilio:{self.domicilio} - Contacto:{self.contacto} - Nombre Responsable:{self.nombre_responsable}")
        print("----------------------------------------------------------------------------------------\n")


class Factura():
    def __init__(self):

        self.nombre = nombre_clientes
        self.RFC = rfc
        self.domicilio = domicilio
        self.contacto = contacto
        self.compras

    def imprimirFactura(self):
        pass


def Ticket():
    pass


class Productos():
    def __init__(self, id_producto, nombre_p, stock, clave_sat, precio_renta, precio_costo):
        self.id_producto = id_producto
        self.nombrep = nombre_p
        self.stock = stock
        self.clave_sat = clave_sat
        self.precio_renta = precio_renta
        self.precio_costo = precio_costo
        self.tieneIVA = True

    def ImprimirP(self):
        print(
            f"ID:{self.id_producto} Nombre:{self.nombrep}  Stock:{self.stock}   Precio:{self.precio_costo}")


class Venta():
    def __init__(self, id_venta, fecha, folio, id_cliente, total):
        self.id = id_venta
        self.fecha = fecha
        self.folio = folio
        self.id_cliente = id_cliente
        self.total = total

    def imprimirV(self):
        print(
            f"ID:{self.id} fecha:{self.fecha} Folio:{self.folio}   Total={self.total}")


class Empresa():
    def __init__(self):
        self.nombre = "Factureros"
        self.domiclio = {
            'Calle': "Rodin",
            'Num,ext': 12,
            'Colonia': "Benito Ju�rez",
            'CP': "03900",
            'Pais': "Mexico"
        }
        self.empleados = []
        self.clientes = []
        self.productos = []

    def agregarFactura(self):
        pass

    def domicilio__completo(self):
        pass

    def editardatos(self):
        pass

    
    def registro_empleado(self, i):
        self.empleados.append(i)
        print("---------------------------------------------------")
        print("\nSe agreg� el usuario correctamente...")

    def desabilitar_empleado(self, i):
        flag = 0
        for j in range(len(self.empleados)):
            if(self.empleados[j].id_empleado == i):
                if (self.empleados[j].estaHabilitado == True):
                    self.empleados[j].estaHabilitado = False
                    print("USUARIO DESHABILITADO")
                    print(
                        "---------------------------------------------------------------")
                    flag = 1
                    break
                else:
                    print("USUARIO YA DESHABILITADO")
                    flag = 1
                    print(
                        "---------------------------------------------------------------")
        if flag == 0:
            print("No hay un id que coincida")

    def habilitar_empleado(self, i):
        flag = 0
        for j in range(len(self.empleados)):
            if(self.empleados[j].id_empleado == i):
                if (self.empleados[j].estaHabilitado == False):
                    self.empleados[j].estaHabilitado = True
                    print("USUARIO HABILITADO")
                    print(
                        "---------------------------------------------------------------")
                    flag = 1
                    break
                else:
                    print("USUARIO YA HABILITADO")
                    flag = 1
                    print(
                        "---------------------------------------------------------------")
                    break
        if flag == 0:
            print("NO SE ENCONTRO EL ID")
            print("---------------------------------------------------------------")

    def Ver_empleado(self):
        for i in range(0, len(self.empleados), 1):
            self.empleados[i].imprimirT()

    def actualizar_cliente(self):
        self.clientes.clear()
        file = open(cliente_archivo, mode='r', newline='')
        with file as cliente_archivos:
            csv_reader = csv.reader(cliente_archivos, delimiter=',')
            for row in csv_reader:
                temp = Clientes(row[0], row[1], row[2], row[3], row[4], row[5])
                self.clientes.append(temp)
        file.close()

    def imprimir_cliente(self):
        self.actualizar_cliente()
        for i in range(0, len(self.clientes), 1):
            self.clientes[i].imprimirCliente()

    def actualizar_producto(self):
        self.productos.clear()
        file = open(producto_archivo, mode='r', newline='')
        with file as producto_archivos:
            csv_reader = csv.reader(producto_archivos, delimiter=',')
            for row in csv_reader:
                temp = Productos(row[0], row[1], row[2],
                                 row[3], row[4], row[5])
                self.productos.append(temp)

    def Ver_productos(self):
        self.actualizar_producto()
        for i in range(0, len(self.productos), 1):
            self.productos[i].ImprimirP()

    def Ventas(self, productos, ventas, buscar):
        toprod = 0
        with open("cliente.csv") as archivo:
            linea = archivo.readlines()
            dic = {}
            for x in linea:
                lista = x.rstrip("\n").split(",")
                dic[lista[0]] = [lista[1], (lista[2])]

            #buscar = input("Ingresa tu ID de usuario : ")
            encontrado = dic.get(buscar)

            if encontrado:
                print("BIENVENID@: \n")
                for i in range(len(productos)):
                    print(f"{productos[i]}\n")
                while(True):
                    prodIn = int(input(
                        "Ingresa el id del producto que desee comprar o tecleee 900 para salir: \n"))
                    flagl = 0
                    if prodIn == 900:
                        break
                    for l in range(len(productos)):
                        if prodIn == productos[l]['ID']:
                            flagl = 1
                            m = l

                    if flagl == 1:
                        while(True):
                            quant = int(
                                input("Ingresa la cantidad de articulos que necesitas de este producto: "))
                            if quant <= productos[m]['stock']:
                                resta = productos[m]['stock']-quant
                                xtra = {'ID': productos[m]['ID'],
                                        'Nombre del producto':  productos[m]['Nombre del producto'],
                                        'stock':  resta,
                                        'Clave SAT':  productos[m]['Clave SAT'],
                                        'Renta del producto':  productos[m]['Renta del producto'],
                                        'Costo del producto ':  productos[m]['Costo del producto '],
                                        }
                                totalc = productos[m]['Costo del producto ']*quant
                                toprod = toprod + totalc
                                miau = {'ID de usuario': buscar,
                                        'Nombre del producto':  productos[m]['Nombre del producto'],
                                        'Cantidad':  quant,
                                        'Clave SAT':  productos[m]['Clave SAT'],
                                        'Costo del producto ':  productos[m]['Costo del producto '],
                                        'total de productos ': totalc,
                                        }
                                ventas.append(miau)
                                productos.pop(m)
                                productos.append(xtra)

                                break

                            else:
                                print("No hay la cantidad necesaria de productos")
                    else:
                        print("No hay producto con ese Id")
        return toprod

    def ImpV(self):
        Venta.imprimirV()


def Calculadora(tot):
    print("Bienvenido Cajero\n")

    while (True):
        print(f"Dinero a pagar {tot}\n")
        ingress = float(input("ingrese el dinero recibido: \n"))
        if ingress > tot:
            totls = ingress-tot
            sentence = f"Dinero recibido: {ingress} \n Cambio: {totls}\n Gracias por su compra"
            break
        elif ingress == tot:
            sentence = f"Dinero recibido: {ingress} \n Cambio {tot}\n Gracias por su compra "
            break
        elif ingress < tot:
            tot = tot - ingress
            print(f"FALTAN DE PAGAR {tot} \n")

    return sentence


def mesesSinIntereses(tot):
    print("Menu")
    print("01.DE CONTADO \n")
    print("02. 3 MESES SIN INTERESES\n")
    print("03. 6 MESES SIN INTERESES\n")
    selec = int(input("Seleccione una opcion: \n"))
    if selec == 1:
        pagos = f"Su total de compra es de  ${tot}\n"
    elif selec == 2:
        tot = tot/3
        pagos = f"Su total de compra es de 3 x  ${tot}\n"
    elif selec == 3:
        tot = tot/6
        pagos = f"Su total de compra es de 6 x  ${tot}\n"
    return pagos


def menu():
    print("====== MENU ======")
    print("1)Alta empleado")
    print("2)Baja empleado")
    print("3)Habilitar empleado")
    print("4)Imprimir Datos Empleado")
    print("5)Alta productos")
    print("6)Ver productos")
    print("7)Alta cliente")
    print("8)Imprimir Datos Cliente")
    print("9)Realizar Venta ")
    print("\nSeleccione la opción: ")


def cambioaDiccionarioProductos(productos):
    separador = ","
    with open(producto_archivo, mode='r', newline='') as archivo:

        for linea in archivo:

            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(separador)

            bandera = 0
            ID = int(columnas[0])
            nombre = columnas[1]
            stock = float(columnas[2])
            SAT = columnas[3]
            renta = float(columnas[4])
            costo = float(columnas[5])
            for n in range(len(productos)):
                if ID == productos[n]['ID']:
                    bandera += 1
            if bandera == 0:
                xd = ({
                    'ID': ID,
                    'Nombre del producto': nombre,
                    'stock': stock,
                    'Clave SAT': SAT,
                    'Renta del producto': renta,
                    'Costo del producto ': costo,
                })
                productos.append(xd)

    return productos


def Factura():
    pass


def Ticket():
    pass


def facturaoTicket(ventas, buscar):
    while(True):
        seleccion = int(input("Quieres Factura 1. o Ticket 2"))
        if seleccion == 1 or seleccion == 2:
            break
        else:
            print("Ingrese una opcion válida")
    for x in range(len(ventas)):
        if buscar == ventas[x]['ID de usuario']:
            print("Bienvenido al portal de pagos")
            if seleccion == 1:
                Factura()
            else:
                Ticket()


clientes_cargo = [""]
id_global_empleado = 0
id_global_venta = 0
productos = []
ventas = []
Facturas = Empresa()
while(True):

    menu()

    opcion = int(input())
    if(opcion == 1):
        system('cls')
        print("===== REGISTRO EMPLEADOS =====\n")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        genero = input("Genero: ")
        puesto = input("Puesto: ")
        i = Empleados(id_global_empleado, nombre, edad,
                      genero, puesto, clientes_cargo)
        Facturas.registro_empleado(i)
        print("Tu id de empleado es: " + str(id_global_empleado)+"\n")
        print("---------------------------------------------------")
        input("\nPresione enter para continuar ...")
        id_global_empleado += 1

    elif(opcion == 2):
        system('cls')
        print("===== BAJA EMPLEADOS =====\n")
        ide = int(input("\nIngrese el id del empleado que desea desabilitar:"))
        Facturas.desabilitar_empleado(ide)
        input("\nPresione enter para continuar ...")

    elif(opcion == 3):
        system('cls')
        print("===== HABILITAR EMPLEADO =====\n")
        ida = int(input("\nIngresa el id del usuario que quieras habilitar:"))
        Facturas.habilitar_empleado(ida)
        input("\nPresione enter para continuar ...")

    elif(opcion == 4):
        system("cls")
        print("===== LISTA EMPLEADOS =====\n")
        Facturas.Ver_empleado()
        input("\nPresione enter para continuar ...")

    elif(opcion == 5):
        system('cls')
        print("===== REGISTRO PRODUCTO =====\n")
        if os.path.exists(producto_archivo):
            filesize = os.path.getsize(producto_archivo)
            if filesize == 0:
                id = 0
            else:
                file = open(producto_archivo, mode='r+', newline='')
                with file as producto_archivos:
                    id_p = max(int(line.split(',')[0])
                               for line in producto_archivos)+1
                    nombre_pro = input("Nombre: ")
                    stock = int(input("Stock:"))
                    Sat = input("Clave SAT:")
                    precio_renta = float(input("Precio Renta:"))
                    precio_costo = float(input("Precio Costo:"))
                    cliente_lectura = csv.writer(
                        producto_archivos, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    cliente_lectura.writerow(
                        [id_p, nombre_pro, stock, Sat, precio_renta, precio_costo])
            file.close()
        else:
            file = open('producto.csv', mode='a', newline='')
            with file as producto_archivos:
                id_p = 0
                nombre_pro = input("Nombre: ")
                stock = int(input("Stock:"))
                Sat = input("Clave SAT:")
                precio_renta = float(input("Precio Renta:"))
                precio_costo = float(input("Precio Costo sin IVA:"))
                precio_total=precio_costo + (precio_costo*0.16)
                cliente_lectura = csv.writer(
                    producto_archivos, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                cliente_lectura.writerow(
                    [id_p, nombre_pro, stock, Sat, precio_renta, precio_total])
            file.close()
        print("---------------------------------------------------")
        input("\nPresione enter para continuar ...")
    elif(opcion == 6):
        productoc = cambioaDiccionarioProductos(productos)
        for k in range(len(productoc)):
            print(productoc[k])

    elif(opcion == 7):
        system('cls')
        print("===== REGISTRO CLIENTE =====\n")
        if os.path.exists(cliente_archivo):
            filesize = os.path.getsize(cliente_archivo)
            if filesize == 0:
                id = 0
            else:
                file = open(cliente_archivo, mode='r+', newline='')
                with file as cliente_archivos:
                    id = max(int(line.split(',')[0])
                             for line in cliente_archivos)+1
                    nombre_clientes = input("Nombre: ")
                    rfc = input("RFC: ")
                    domicilio = input("Domicilio: ")
                    contacto = input("Contacto ")
                    nombre_responsable = input("Nombre Responsable: ")
                    today = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
                    cliente_lectura = csv.writer(
                        cliente_archivos, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    cliente_lectura.writerow(
                        [id, nombre_clientes, rfc, domicilio, contacto, nombre_responsable, today])
            file.close()
        else:
            file = open('cliente.csv', mode='a', newline='')
            with file as cliente_archivos:
                id = 0
                nombre_clientes = input("Nombre: ")
                rfc = input("RFC: ")
                domicilio = input("Domicilio: ")
                contacto = input("Contacto: ")
                nombre_responsable = input("Nombre Responsable: ")
                today = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
                cliente_lectura = csv.writer(
                    cliente_archivos, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                cliente_lectura.writerow(
                    [id, nombre_clientes, rfc, domicilio, contacto, nombre_responsable, today])
            file.close()
        print("---------------------------------------------------")
        input("\nPresione enter para continuar ...")
    elif(opcion == 8):
        system('cls')
        print("===== LISTA DE CLIENTES =====\n")
        Facturas.imprimir_cliente()
        input("\nPresione enter para continuar ...")
    elif(opcion == 9):
        buscar = input("Ingresa tu ID de usuario : ")
        productoc = cambioaDiccionarioProductos(productos)
        tot = Facturas.Ventas(productoc, ventas, buscar)
        print(tot)
        metodoPago = int(
            input("Con que va a pagar\n 1) Tarjeta de Credito,\n 2) Efectivo\n"))
        if metodoPago == 1:
            totals = mesesSinIntereses(tot)
            print(totals)
        else:
            totals = Calculadora(tot)
            print(totals)
        facturaoTicket(ventas, buscar)
