# Escreva um programa que pergunte o valor inicial de uma dívida e juro mensal.
# Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja
# paga, o total pago e o total juros pago.

divida = float(input("Digite o total da divida: "))
juro_mensal = float(input("Digite o juro mensal: "))
pagamento_mensal = 0
contador = 1
while divida >= 0:
    divida = divida * ((juro_mensal / 100) + 1)

    pagamento_mensal = float(input("Digite o pagamento mensal"))

    divida = divida - pagamento_mensal

    print("A divida é: R$%5.2f" % (divida))
    # meses passados
    contador = contador + 1