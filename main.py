

def calcular_cuadrado(numero):
    return numero**2

def es_par(number):
    return numero % 2 == 0

list_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = [calcular_cuadrado(numero) for num in list_num]
print(lista_cuadrados)


