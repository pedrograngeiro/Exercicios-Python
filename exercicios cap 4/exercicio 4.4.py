# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%.
# Para inferiores ou iguais, de 15%

salario = float(input("Digite o salario: "))
salario_new = 0
if salario > 1250:
    salario_new = salario * 1.10
else:
    salario_new = salario * 1.15

print(salario)
print(salario_new)