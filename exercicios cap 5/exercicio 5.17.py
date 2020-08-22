# O que acontece se digitarmos 0 (zero) no valor de pagar

# Execute o programa (Listagem 5.14) para os seguintes valores: 501, 745, 384, 2, 7 e 1

valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
apagar = valor

while True:
    if atual <= apagar:
        apagar = apagar - atual
        cedulas = cedulas + 1
    else:
        print("%d cédulas(s) de R$%d" % (cedulas,atual))
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
