def lista_unidimensional(lista):
    lista_transformada = []

    for element in lista:
        if type(element) == list:
            for item in element:
                lista_transformada.append(item)
        else:
            lista_transformada.append(element)
    
    return lista_transformada


print(lista_unidimensional([[1,2,3],1,6,1,[1,7],1]))

