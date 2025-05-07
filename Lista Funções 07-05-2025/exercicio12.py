# Fatorial
def fatorial(numero):
    if numero > 0:
        produto = 1
        for i in range(1, numero + 1):
            produto *= i
        return produto
    else:
        return "Este programa calcula apenas o fatorial de números positivos."

print(fatorial(3))
print(fatorial(7))
print(fatorial(9))
print(fatorial(25))
print(fatorial(26))