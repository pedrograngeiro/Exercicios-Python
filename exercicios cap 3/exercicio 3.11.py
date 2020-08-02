# Faça um programa que solicite o preço de uma mercadoria e o percetual de desconto.
# Exiba o valor do descoto e o preço a pagar.

valor = float(input("Digite o preco da mercadoria: "))
percentual = float(input("O valor do desconto: "))


valor_novo = (valor * (percentual/ 100))
valor_novo_final = valor - valor_novo


print(valor_novo_final)
