# Modifique o programa para aceitar valores decimais, ou seja, também contar moedas de 0,01 0,02 0,05 0,10 e 0,50.

valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100.00
apagar = valor

while True:
    if atual <= apagar:
        apagar = apagar - atual
        cedulas = cedulas + 1
    else:
        if cedulas != 0:
            print("%d cédulas(s) de R$%.2f" % (cedulas,atual))
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        elif atual == 0.01 and cedulas == 0:
            break


        cedulas = 0