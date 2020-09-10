# Escreva um programa que exiba uma lista de opções(menu): adição, subtração, divisão, multiplicação e sair.
# Imprima a tabuada da operação escolida
# Repita até que a opção saída seja escolhida

print("Digite + para adição")
print("Digite - para subtração")
print("Digite * para multiplicação")
print("Digite / para divisão")
print("Digite 0 para sair.")

while True:
    operacao = input("Digite a operação desejada: ")

    resultado = 0

    print(operacao)

    if operacao == "+":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 + n2
        print("A soma entre %5.2f e %5.2f é: %5.2f " % (n1, n2, resultado))

    if operacao == "-":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 - n2
        print("A subtração entre %5.2f e %5.2f é: %5.2f " % (n1, n2, resultado))

    if operacao == "*":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resulado = n1 * n2
        print("A multiplicação entre %5.2f e %5.2f é: %5.2f " % (n1, n2, resultado))

    if operacao == "/":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resulado = n1 / n2
        print("A divisão entre %5.2f e %5.2f é: %5.2f " % (n1, n2, resultado))

    if operacao == "0":
        break