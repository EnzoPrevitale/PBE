def exibir_calculadora(numero_exibido):
    print(f"""
         ______________________
        |  _________________  |
        | |{" " * (16 - len(str(numero_exibido)))}{numero_exibido} | |
        | |_________________| |
        |  ___ ___ ___   ___  |
        | | 7 | 8 | 9 | | + | |
        | |___|___|___| |___| |
        | | 4 | 5 | 6 | | - | |
        | |___|___|___| |___| |
        | | 1 | 2 | 3 | | x | |
        | |___|___|___| |___| |
        | | . | 0 | = | | / | |
        | |___|___|___| |___| |
        |_____________________|
            """)


def realizar_operacao(num1, num2, operacao):
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao.upper() == "x":
        resultado = num1 * num2
    elif operacao.upper() == "/":
        resultado = num1 / num2

    return resultado


def processar_input(numero_exibido):
