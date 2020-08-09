# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular a soma(+), subtração(-), multiplicação(*) e divisão (/).
# Exiba o resultado da operação solicitada.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("soma(+), subtração(-), multiplicação(*) e divisão (/).")
operacao = input("Digite a operacao: ")

resultado = 0


if operacao == "+":
    resultado = num1 + num2
    print("Soma selecionado")
else:
    if operacao == "-":
        resultado = num1 - num2
        print("Subtração selecionado")
    else:
        if operacao == "*":
            resultado == num1 * num2
            print("Multiplicação selecionado")
        else:
            if operacao == "/":
                resultado == num1 / num2
                print("Divisão selecionado")
            else:
                print("Operação invalida")
print("O resultado da operação é: %.1f" % (resultado))