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
        n1 = float(input("Digite o número: "))
        tabuada = 1
        while tabuada <= 10:
            print("%d + %d = %d" % (n1, tabuada, (tabuada + n1)))
            tabuada+= 1

    if operacao == "-":
        n1 = float(input("Digite o número: "))
        tabuada = 1
        while tabuada <= 10:
            print("%d - %d = %d" % (n1, tabuada, (n1 - tabuada)))
            tabuada+= 1

    if operacao == "*":
        n1 = float(input("Digite o número: "))
        tabuada = 1
        while tabuada <= 10:
            print("%d * %d = %d " % (n1, tabuada, (tabuada * n1)))
            tabuada+=1

    if operacao == "/":
        n1 = float(input("Digite o número: "))
        tabuada = 1
        while tabuada <= 10:
            print("%d / %d = %d " % (n1, tabuada, (n1 / tabuada)))
            tabuada += 1

    if operacao == "0":
        break