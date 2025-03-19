# Lista de exercícios PBE
'''
# 01

# Declarando a variável nome
nome = "João"

# Exibindo a variável na tela
print(nome)
'''
# 02
'''
# Declarando as variáveis a e b com os valores 5 e 10
a = 5
b = 10

# Calculando e imprimindo a soma das variáveis
print(f"a + b = {a + b}")

# Calculando e imprimindo a subtração de a por b
print(f"a - b = {a - b}")

# Calculando e imprimindo o produto entre as variáveis
print(f"a * b = {a * b}")

# Calculando e imprimindo o quociente entre a e b
print(f"a / b = {a / b}")
'''
# 03
'''
# Declarando as variáveis preco e desconto
preco = 50
desconto = 10

# Calculando o valor final
preco = preco - desconto

# Exibindo o valor final
print(preco)
'''
# 04
'''
# Declarando a variável
resultado = 10 + 5 * 2

# Imprimindo o resultado
print(resultado)
'''
# 05
'''
# Declarando a variável texto, armazenando a string "150"
texto = "150"

# Convertendo o valor de texto de string para int
texto = int(texto) * 2

# Imprimindo o resultado
print(texto)
'''
# 06
'''
# Declarando a array numeros
numeros = [1,2,3,4,5]

# Imprimindo numeros
print(numeros)

# Alterando o segundo elemento para 20
numeros[1] = 20

# Imprimindo numeros novamente
print(numeros)
'''
# 07
'''
# Solicitando os valores de a e b ao usuário
a, b = float(input("Digite o valor de a: ")), float(input("Digite o valor de b: "))

# Imprimindo a soma de a e b
print(a + b)
'''
# 08
'''
# Solicitando os valores de x e y ao usuário
x, y = float(input("Digite o valor do numerador: ")), float(input("Digite o valor do denominador: "))

# Calculando o quociente entre x e y e imprimindo o resultado
print(x // y)
'''
# 09
'''
# Solicitando os valores de num1 e num2 ao usuário
num1, num2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: "))

# Verificando se num1 é maior que num2 e imprimindo o resultado
print(num1 > num2)
'''
# 10
'''
# Solicitando ao usuário a sua idade
idade = int(input("Digite a sua idade: "))

# Calculando a idade aproximada do usuário em dias
idade = idade * 365

# Imprimindo o resultado
print(f"Você tem {idade} dias de vida.")
'''
# 11
'''
# Solicitando os valores da base e do expoente ao usuário
base, expoente = float(input("Digite a base: ")), float(input("Digite o expoente: "))

# Calculando o valor da potência
potencia = base ** expoente

# Imprimindo o resultado
print(f"O resultado da operação é {potencia}.")
'''
# 12
'''
# Solicitando o valor de preco ao usuário
preco = float(input("Digite o preço: "))

# Convertendo a float preco para string
preco = str(preco)

# Concatenando preco com a string "O preço é R$" e imprimindo o resultado
print(f"O preço é R${preco}.")
'''
# 13
'''
# Aproximando o valor de pi em 3,14
pi = 3.14

# Solicitando o valor do raio ao usuário
raio = float(input("Digite o valor do raio: "))

# Calculando a área do círculo
area = pi*raio**2

# Imprimindo o resultado
print(area)
'''
# 14
'''
# Solicitando os valores de a e b ao usuário
a, b = input("Escolha o valor de a: "), input("Escolha o valor de b: ")

# Trocando os valores das duas variáveis sem criar uma nova variável
a,b = b,a

# Imprimindo os novos valores das variáveis
print(f"a: {a} b: {b}")
'''
# 15
'''
# Solicitando os valores das notas ao usuário e definindo os pesos 2, 3 e 5 a elas
nota1,nota2,nota3 = float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: ")), float(input("Digite a terceira nota: "))
peso1,peso2,peso3 = 2,3,5

# Calculando a média ponderada das três notas
media = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)

# Imprimindo a média ponderada
print(media)
'''
# 16
'''
# Solicitando as posiçãos dos dois pontos ao usuário
x1, y1 = float(input("Digite a posição do primeiro ponto no eixo x: ")), float(input("Digite a posição do primeiro ponto no eixo y: "))
x2, y2 = float(input("Digite a posição do segundo ponto no eixo x: ")), float(input("Digite a posição do segundo ponto no eixo y: "))

# Calculando a distância entre os dois pontos no plano cartesiano
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

# Imprimindo a distância
print(f"A distância entre o primeiro e o segundo ponto no plano cartesiano é de {distancia}")
'''