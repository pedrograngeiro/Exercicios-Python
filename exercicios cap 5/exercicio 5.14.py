# Escreva um programa que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
soma = 0
num = 0
contador = 0
while True:
    num = int(input("Digite um número: "))
    soma = soma + num

    if num == 0: # Parar o loop
        print("A média aritmética é: %2f" % (soma / contador))
        break

    contador = contador + 1

