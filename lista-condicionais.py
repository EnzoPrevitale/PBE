# 01 - Número par ou ímpar
'''
# Solicitando um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verificando se o número digitado é par ou ímpar
if numero % 2 == 0: # Número par
    print("O número digitado é par.")
else: # Número ímpar
    print("O número digitado é ímpar.")
'''
# 02 - Número maior que 10 ou não
'''
# Solicitando um número ao usuário
numero = float(input("Digite um número: "))

# Verificando se o número é maior que 10
if numero > 10: # Número maior que 10
    print("O número digitado é maior que 10.")
else:
    print("O número digitado não é maior que 10.")
'''
# 03 - Verificação de idade
'''
# Solicitando a idade do usuário
idade = int(input("Digite a sua idade, em anos: "))

# Verificando se a idade digitada é superior a 18 anos
if idade >= 18: # Maior de idade
    print("Você é maior de idade.")
else: # Menor de idade
    print("Você é menor de idade.")
'''
# 04 - Verificação de voto
'''
# Solicitando a idade do usuário
idade = int(input("Informe a sua idade, em anos: "))

# Verificando a obrigatoriedade do voto do usuário
if idade < 16: # Não vota
    print("Você não é elegível para votar.")
elif idade < 18: # Facultativo
    print("O seu voto é facultativo.")
else: # Obrigatório
    print("O seu voto é obrigatório.")
'''
# 05 - Verificando se o número é positivo, negativo ou zero
'''
# Solicitando um número ao usuário
numero = float(input("Digite um número: "))

# Verificando se o número é menor, igual ou maior que zero
if numero < 0: # Negativo
    print("O número é negativo.")
elif numero > 0: # Positivo
    print("O número é positivo.")
else: # Zero
    print("O número é zero.")
'''
# 06 - Classificação de notas
'''
# Solicitando uma nota ao usuário
nota = int(input("Digite uma nota de 0 a 10: "))

# Verificando e classificando a nota
if nota > 10 or nota < 0: # Nota inválida
    print("Nota inválida.")
elif nota >= 9: # A
    print("A nota é A.")
elif nota >= 7: # B
    print("A nota é B.")
elif nota >= 5: # C
    print("A nota é C.")
elif nota >= 3: # D
    print("A nota é D.")
elif nota >= 0: # E
    print("A nota é E.")
'''
# 07 - Verificando desconto
'''
# Solicitando a idade do usuário
idade = int(input("Digite a sua idade: "))

# Verificando o direito a desconto do usuário
if idade <= 12 or idade >= 60: # Tem direito a um desconto
    print("Você tem direito a um desconto.")
else: # Não tem direito a um desconto
    print("Você não tem direito a um desconto.")
'''
# 08 - Verificação de triângulo - NÂO FINALIZADO
'''
# Solicitando os três lados ao usuário
ladoA = float(input("Digite a medida do lado A: "))
ladoB = float(input("Digite a medida do lado B: "))
ladoC = float(input("Digite a medida do lado C: "))

# Verificando os maiores lados e se os lados digitados correspondem a um triângulo
if ladoA >= ladoB and ladoA > ladoC or ladoA == ladoC and ladoA > ladoB:
    # ladoA é o maior
elif ladoB >= ladoA and ladoB > ladoC:
    # ladoB é o maior
elif ladoC >= ladoB and ladoC > ladoA:
    # ladoC é o maior
elif ladoA == ladoB and ladoB == ladoC:
    # Lados iguais
    # Triângulo equilátero
    triangulo = "Equilátero"
'''
# 09 - Desconto
'''
# Solicitando o valor total da compra ao usuário
valor = float(input("Digite o valor total da compra: "))

# Verificando o desconto a aplicar na compra
if valor < 100: # 5%
    valor_final = valor * 0.95
    print("O desconto será de 5%.")
elif valor <= 500: # 10%
    valor_final = valor * 0.9
    print("O desconto será de 10%")
else: # 15%
    valor_final = valor * 0.85
    print("O desconto será de 15%")

# Imprimindo o valor final
print(f"O valor final será {valor_final}.")
'''
# 10 - Ano bissexto
'''
# Solicitando um ano ao usuário
ano = int(input("Digite um ano: "))

# Verificando se o ano é bissexto
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0: # Bissexto
            print("O ano é bissexto.")
        else: # Não bissexto
            print("O ano não é bissexto.")
    else: # Bissexto
        print("O ano é bissexto.")
else: # Não bissexto
    print("O ano não é bissexto.")
'''
# 11 - Calculadora de IMC
'''
# Solicitando o peso e a altura do usuário
peso = float(input("Digite o seu peso, em kg: "))
altura = float(input("Digite a sua altura, em m: "))

# Calculando o IMC do usuário
imc = peso / altura ** 2
print(imc)

# Classificando o IMC do usuário
if imc < 18.5: # Abaixo do peso
    print("Você está abaixo do peso.")
elif imc < 25: # Peso normal
    print("O seu peso é normal.")
elif imc < 30: # Sobrepeso
    print("Você tem sobrepeso.")
else: # Obesidade
    print("Você é obeso.")
'''
# 12 - Ordem numérica
'''
# Solicitando três números ao usuário
num = [float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: ")), float(input("Digite o terceiro número: "))]
print(num)

# Verificando em qual ordem os números estão
if num[0] > num[1] > num[2] or num[0] == num[1] > num[2] or num[0] > num[1] == num[2]: # Descrescente
    print("Os números estão em ordem decrescente.")
elif num[2] > num[1] > num[0] or num[2] == num[1] > num[0] or num[2] > num[1] == num[0]: # Crescente
    print("Os números estâo em ordem crescente.")
elif num[0] == num[1] == num[2]: # Iguais
    print("Os números são iguais.")
else: # Não ordenados
    print("Os números não estão ordenados.")
'''
# 13 - Temperatura
'''
# Solicitando a temperatura em ºC
temperatura = float(input("Digite a temperatura, em ºC: "))

# Classificando a temperatura
if temperatura <= 10:  # Frio
    print("Está frio.")
elif temperatura <= 25:  # Aconchegante
    print("Está aconchegante.")
elif temperatura <= 40:  # Quente
    print("Está quente.")
else:  # Muito quente
    print("Está muito quente.")
'''
# 14 e # 17 - Validação de data e conversão de formato
'''
# Solicitando a data no formato dd/mm/aaaa ao usuário
data = input("Digite a data no formato dd/mm/aaaa: ")

# Separando as três partes da string pela barra
dd = int(data.split('/')[0])
mm = int(data.split('/')[1])
aaaa = int(data.split('/')[2])

# Verificando se a data é válida
valido = True

if aaaa % 4 == 0:
    bissexto = True
else:
    bissexto = False

for i in range(1, 8):
    if mm == i:
        if i % 2 != 0:
            # 31 dias
            if dd > 31:
                # Data inválida
                valido = False
        else:
            # 28, 29 ou 30 dias
            if mm == 2:
                # Fevereiro
                if bissexto:
                    if dd > 29:
                        # Data inválida
                        valido = False
                else:
                    if dd > 28:
                        # Data inválida
                        valido = False
            else:
                if dd > 30:
                    # Data inválida
                    valido = False

for i in range(8, 13):
    if mm == i:
        if mm % 2 == 0:
            if dd > 31:
                # Data inválida
                valido = False
        else:
            if dd > 30:
                # Data inválida
                valido = False
if mm > 12:
    valido = False

# Imprimindo a data no formato aaaa-mm-dd, caso ela não seja válida, imprimindo a mensagem "Data inválida"
if valido:
    print(f"{aaaa}-{mm:02}-{dd:02}")
else:
    print("Data inválida.")
'''
# 16 - Raiz quadrada

# Solicitando um número ao usuário
num = float(input("Digite um número: "))

# Analisando se é possível obter a raiz quadrada do número no conjunto especificado (pertencente aos números reais e menor ou igual a 100)
if num < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo.")
elif num > 100:
    print("Número muito grande, reduza para um valor abaixo de 100.")
else:
    print(num ** (1/2))