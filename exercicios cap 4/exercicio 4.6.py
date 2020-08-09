# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço
# da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distancia = float(input("Digite a distancia em km a percorrer: "))
preco = 0

if distancia < 200:
    preco = distancia * 0.50
    print("A distancia foi: %d e o valor a ser pago é: R$ %5.2f" % (distancia, preco))
else:
    preco = distancia * 0.45
    print("A distancia foi: %d e o valor a ser pago é: R$ %5.2f" % (distancia, preco))