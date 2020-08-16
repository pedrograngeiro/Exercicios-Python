# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total ganho com juros período.
# Selic dia 14/08/2020, 1,90%
selic = 1.9
dep_inicial = float(input("Digite o deposito inicial em R$: "))
cont = 1
juro = 0
acumulador = dep_inicial
while cont <= 24:
    juro = acumulador * (selic  / 100)
    acumulador = acumulador + juro
    print(acumulador)
    cont = cont + 1