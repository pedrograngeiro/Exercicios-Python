# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo.
# Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos
# entender a multiplicação de dois números como somas sucessivas de um deles.
# Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4

# inicilizando as variaveis com 0
i = 0
soma = 0
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
multi = num1 * num2

# end add para ao fim do print não pular linha
print("Soma: %d X %d = %d = " % (num1, num2, multi), end="")

while i != num2: # numero de vezes que o num1 ira se repetir sera igual ao num2
    soma = soma + num1
    print("+%d " % num1, end="") # end add para ao fim do print não pular linha
    if i == num1: # Para add o sinal de = quando chegar ao resultado
        print(" = ", end="") # end add para ao fim do print não pular linha
    i = i + 1

print(" = ", end="")
i = 0
while i != num1: # numero de vezes que o num2 ira se repetir sera igual ao num1
    soma = soma + num1
    print("+%d " % num2, end="") # end add para ao fim do print não pular linha

    i = i + 1