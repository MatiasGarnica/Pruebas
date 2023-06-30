def numero_primo(numero):
    
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

print(numero_primo(5))
print(numero_primo(7))
print(numero_primo(19))
print(numero_primo(22))
