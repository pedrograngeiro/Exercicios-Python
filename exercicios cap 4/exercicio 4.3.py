# Escreva um programa que leia três números e que imprima o maior e o menor.

n1 = int(input("Digite o número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 >= n2 and n1 >= n3:
    print("O %d é o maior número!" % (n1))

if n2 >= n1 and n2 >= n3:
    print("O %d é o maior número:" % (n2))

if n3 >= n1 and n3 >= n2:
    print("O %d é o maior número:" % (n3))

if n1 <= n2 and n1 <= n3:
    print("O %d é o menor número: " % (n1))

if n2 <= n1 and n2 <= n3:
    print("O %d é o menor número: " % (n2))

if n3 <= n1 and n3 <= n2:
    print("O %d é o menor número: " % (n3))