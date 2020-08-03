# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perder 10 minutos de vida a cada cigarro, calcule quantos dias
# de vida um fumante perderá. Exiba o total de dias.

num_cigarros = int(input("Digite o numero de cigarros fumados ao longo da vida: "))

min_perdidos = num_cigarros * 10

dias = min_perdidos / 24
anos = dias / 365


print("%.0d anos e %d dias." % ((anos), (dias - 365)))