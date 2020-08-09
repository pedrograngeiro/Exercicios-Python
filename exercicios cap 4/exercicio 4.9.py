# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input("Digite o preço da casa: "))
salario = float(input("Digite o salario: "))
anos = int(input("Em quantos anos deseja pagar: "))

prestacao = valor_casa / (anos * 12)

if prestacao > (0.30 * salario):
    print("Emprestimo negado.")
else:
    print("Emprestimo aprovado. As prestações serão: %d de R$ %5.2f" % ((anos * 12), prestacao))