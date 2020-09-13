# Modifique o programa anterior de forma a ler um número n.
# Imprima os n primeiros números primos.

núm = int(input("Digite um número: "))
while True:
    tot = 0
    cont = 1
    while cont <= núm: # cont vai percorrer todos os números abaixo de núm
        if núm % cont == 0:
            tot = tot + 1 # se tot igual a 2 ele é primo

        cont+=1
    if tot ==2: # mostra o número primo em tela
        print(núm)

    núm -=1 # variavel que faz percorrer todos os números abaixo de núm
    if núm == 0: # encerra o loop
        break