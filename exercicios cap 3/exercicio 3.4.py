# Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
# Considere que pagam imposto cujo salário é maior que R$ 1200,00

salario = float(input("Digite o salario da pessoa: "))

if salario > 1200:
    print("A pessoa deve pagar imposto.")
else:
    print("A pessoa não precisa pagar imposto.")