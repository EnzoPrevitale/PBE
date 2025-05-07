# Palíndromos
def verificar_palindromo(texto):
    temp = "".join(texto.upper().split(" "))[::-1]

    if temp == "".join(texto.upper().split(" ")):
        return True
    else:
        return False

print(verificar_palindromo("Ana Ana"))
print(verificar_palindromo("1DS-TB"))
print(verificar_palindromo("Subi no Onibus"))