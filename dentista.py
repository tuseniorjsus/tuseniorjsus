from os import system
from datetime import datetime
import csv
import os

producto_archivo = "producto.csv"
while(True):
    op=int(input("Eliga una opcion entre 0 y 1:"))
    if op==0:
        if os.path.exists(producto_archivo):
            filesize = os.path.getsize(producto_archivo)
            if filesize == 0:
                id = 0
            else:
                file = open(producto_archivo, mode='r+', newline='')
                with file as producto_archivos:
                    id_p = max(int(line.split(',')[0])for line in producto_archivos)+1
                    nombre_pro = input("Nombre: ")
                    stock = int(input("Stock:"))
                    cliente_lectura = csv.writer(producto_archivos, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    cliente_lectura.writerow([id_p, nombre_pro, stock])
            file.close()
        else:
            file = open('producto.csv', mode='a', newline='')
            with file as producto_archivos:
                id_p = 0
                nombre_pro = input("Nombre: ")
                stock = int(input("Stock:"))
                producto_lectura = csv.writer(producto_archivos, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                producto_lectura.writerow([id_p, nombre_pro, stock])
            file.close()
    elif op==1:
        break
    else:
        break
             
    
id_ped=int(input("Id del Producto:"))
file = open(producto_archivo, mode='r', newline='')
with file as producto_archivos:
    csv_reader = csv.reader(producto_archivos, delimiter=',')
    for row in csv_reader:
        if id_ped==int(row[0]):
            idR=row[0]
            nombreR=row[1]
            stockR=int(row[2])-5
            producto_lectura = csv.writer(producto_archivos, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            producto_lectura.writerow([idR, nombreR, stockR])
file.close()

print(producto_archivo)