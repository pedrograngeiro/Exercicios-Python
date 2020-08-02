# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do
# salario e porcentagem do aumento. Exiba o valor do aumento e do novo salario.

salario = float(input("Digite o salario atual: "))
aumento = float(input("Digite a % de aumento: "))

# Ex: se o aumento for 30%. Portanto 30 / 100, temos que aumento = 0,30
# Como resultado do fator de aumento temos que somar uma unidade
# 0,30 + 1 = 1,30
# Que se multiplicado pelo salario é o novo aumento.

salario_novo = salario * ((aumento / 100) + 1)


# Para escrever o simbolo de % é necessario acompanha-lo por outro do mesmo, ou seja %%
print("Seu antigo salário era de %5.2f e recebeu um aumento de %.2f%%" % (salario, aumento))
print("Totalizando um aumento liquido de R$%5.2f" % (salario_novo - salario))
print("Portanto seu novo salário será de: R$%5.2f" % (salario_novo))