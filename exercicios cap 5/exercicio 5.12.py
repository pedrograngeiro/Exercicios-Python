# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
# Esse valor será depositado no inicio de cada mês, e você deve cosiderá-lo para o cálculo de juros
# mês seguinte.

selic = 1.9
dep_inicial = float(input("Digite o deposito inicial em R$: "))
deposito_mensal = 0
cont = 1
juro = 0
acumulador = dep_inicial
while cont <= 24:
    juro = acumulador * (selic / 100)

    if cont >= 2: #a partir do segundo mês
        deposito_mensal = float(input("Digite o valor a ser depositado esse mês: "))
    juro = juro + deposito_mensal
    acumulador = acumulador + juro
    print(acumulador)
    cont = cont + 1