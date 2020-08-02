# Escreva um programa que converta uma temperatura digitada em ºC em ºF. A fórmula para essa conversão é:
# F = (9 x C / 5) + 32 # Formula para converter graus para fahrenheit

C = int(input("Digite a temperatura em graus: "))

F = (9 * C / 5) + 32

print("A temperatura em Graus é igual a: %dºC. E em fahrenheit %dºF." % (C, F))