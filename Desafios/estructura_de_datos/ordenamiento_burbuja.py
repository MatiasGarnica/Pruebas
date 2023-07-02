def ordenamiento_numeros(lista):
    #lista_ordenada = sorted(lista)
    for i in range (len(lista)):
        for j in range (0,len(lista)-i-1):
            if lista[j] > lista[j+1]:
                temporal = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temporal
                print(lista)

    return lista


print(ordenamiento_numeros([1,7,3,5,6,1,6]))