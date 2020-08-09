# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para industria
# e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

#   Preço por tipo e faixa de consumo
#Tipo           Faixa(kWh)          Preço
###########################################
#               Até 500             R$ 0,40
#Residencial
#               Acima de 500        R$ 0,65
###########################################
#               Até 1000            R$ 0,55
#Comercial
#               Acima de 1000       R$ 0,60
###########################################
#               Até 5000            R$ 0,55
#Industrial
#               Acima de 5000       R$ 0,60
###########################################
valor = 0
kwh = int(input("Digite a quantidade de kWh: "))

print("Digite R para residencial, C para comercial e I para industrial.")
tipo = input("Digite o tipo:" )

if tipo == "R":
    if kwh < 500:
        valor = kwh * 0.40
    else:
        valor = kwh * 0.65

if tipo == "C":
    if kwh < 1000:
        valor = kwh * 0.55
    else:
        valor = kwh * 0.65

if tipo == "I":
    if kwh < 5000:
        valor = kwh * 0.40
    else:
        valor = kwh * 0.65

print("O valor a ser pago é: R$ %5.2f" % (valor))