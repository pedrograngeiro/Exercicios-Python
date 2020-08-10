# Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

count = 1
x = 1

# count até 10 para mostrar os multiplos de 3
while count < 10:
    # se o modulo por 3 for igual a zero ele é multiplo
    if x % 3 == 0:
        print(x)
        count = count + 1
    x = x + 2