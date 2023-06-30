def palindromo(texto):
    
    texto_minuscula = texto.lower()
    texto_sin_espacio = texto_minuscula.replace(" ","")
    return texto_sin_espacio == texto_sin_espacio[::-1]

texto = input("Ingrese un texto que consideres palindromo: ")
print(palindromo(texto))
