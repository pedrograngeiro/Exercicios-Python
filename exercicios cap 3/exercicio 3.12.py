# Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distancia a percorrer e a velocidade média esperada para viagem.
# tempo = distancia / velocidade media

distancia = int(input("Digite a distancia a percorrer: (em km)"))
velocidade_media = int(input("Quantos km/h de média? "))

tempo = distancia / velocidade_media

#Variavel tempo sendo convertida para minutos
tempo = tempo * 60
print("O tempo de vigem é de %d minutos." % (tempo))