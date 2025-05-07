def classificar_numero(numero):
    if numero < 5:
        return "Pequeno"
    elif numero < 10:
        return "Médio"
    else:
        return "Grande"


print(classificar_numero(3))
print(classificar_numero(9))
print(classificar_numero(12))