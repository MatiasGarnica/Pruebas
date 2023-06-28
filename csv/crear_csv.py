import csv
import os

ruta = "csv_vacio.csv"
ruta_absoluta = "C:\\Users\\Matías\\Documents\\GitHub\\Pruebas\\csv_vacio.csv"
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv")

print(ruta_absoluta)
print(ruta_absoluta_os)


