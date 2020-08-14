# Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo assim como o resto da
# divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender
# o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo.
# Logo, 20 % 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

dividendo = int(input("Digite o primeiro número da divisão: "))
divisor = int(input("Digite o segundo número: "))
quociente = 0
resto = 0
soma = 0
#div = num1 // num2             #Lembre-se que não podemos utilizar estas operações
#resto = num1 % num2            #Apenas soma e subtração

# Para funcionar o dividendo tem que ser maior que soma
while dividendo > soma:
    soma = soma + divisor
    if soma > dividendo:
        soma = soma - divisor # retira a soma a mais
        break
    quociente = quociente + 1

resto = dividendo - soma
print(resto)
print(quociente)