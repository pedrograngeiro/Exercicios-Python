# Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer a verificação, calcule o resto da divisão do número por 2 e depois por todos os números
# ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo.
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

núm = int(input("Digite um número: "))
tot = 0
cont = 1
while cont <= núm:
    if núm % cont == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{}' .format(cont) , end='')

    cont+=1

print('\n\033[mO número {} foi divisivel {} vezes' .format(núm, tot))

if tot == 2:
    print('E por isso ele é primo É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
