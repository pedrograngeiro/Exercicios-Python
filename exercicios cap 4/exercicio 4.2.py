# Escreva um programa que pergunte a velocidade do carro de um usuário.
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de km/h.

velocidade = int(input("Digite a velocidade em km/h: "))

if velocidade > 80:
    diferenca = velocidade - 80
    diferenca = diferenca * 5
    print("Você ultrapassou a velocidade permitida ( 80 km/h , portanto a multa será de R$%5.2f." % (diferenca))