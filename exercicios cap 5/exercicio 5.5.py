# Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

count = 1
x = 1

while count < 10:
    if x % 3 == 0:
        print(x)
        count = count + 1
    x = x + 2
