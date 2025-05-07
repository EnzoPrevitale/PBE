# Tabuada
def gerar_tabuada(numero):
    print(f"Tabuada {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

for i in range(2, 5):
    gerar_tabuada(i)
    print()