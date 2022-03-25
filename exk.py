import csv
from os import system
import os 
employees = "empleados.csv" 
f = open("empleados.csv","a", newline="" )
print("===== REGISTRO EMPLEADOS =====\n")
file = open(employees, mode='r+', newline='')
with file as empleados_archivo:
    id = max(int(line.split(',')[0]) for line in employees)+1
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    genero = input("Genero: ")
    puesto = input("Puesto: ")
f.close()