""" def calcular_factorial(numero):

    factorial = 1
    for i in range(2, numero+1):
        print(f"{i}a")
        factorial = factorial * i

    return factorial

print(calcular_factorial(0))
print(calcular_factorial(1))
print(calcular_factorial(2))
print(calcular_factorial(3))
print(calcular_factorial(5))
print(calcular_factorial(8))
 """
def calcular_factorial_recursivo(numero):

    """ 
    3*factorial(2)
    3*2*factorial(1)
    3*2*1
    """
    
    if numero == 0 or numero == 1:
        return 1

    return numero * calcular_factorial_recursivo(numero-1)

print(calcular_factorial_recursivo(0))
print(calcular_factorial_recursivo(2))
print(calcular_factorial_recursivo(3))
print(calcular_factorial_recursivo(5))

