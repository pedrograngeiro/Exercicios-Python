# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km.

quilometros = float(input("Digite a quantidade de km percorridos."))
dias = int(input("Por quantos dias o carro foi alugado: "))
# deixei a variável preco como float, para declarar números com casas decimais.
preco = float((0.15 * quilometros) + (60 * dias))

print("Foi percorrido %d Km em %d dias." % (quilometros, dias))
print("O preço é: R$%5.2f" % (preco))