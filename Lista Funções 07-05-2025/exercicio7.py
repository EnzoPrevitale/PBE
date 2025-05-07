# 10% de desconto
def aplicar_desconto(preco, porcentagem_desconto):
    return preco - preco * (porcentagem_desconto/100)


desconto = 10
print(aplicar_desconto(50, desconto))
print(aplicar_desconto(120, desconto))
print(aplicar_desconto(200, desconto))