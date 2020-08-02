# Escreva um programa que leia a quantidade de dias, horas, minutos do usuario.
# Calcule o total em segundos.

#01 minuto = 60 segundos
#01 hora = 3.600 segundos
#24 horas = 86.400 segundos

dias = int(input("Digite os dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

dias_em_segundos = dias * 86400
horas_em_segundos = horas * 3600
minutos_em_segundos = minutos * 60

total_segundos = dias_em_segundos + horas_em_segundos + minutos_em_segundos + segundos

print("%d dias." % (dias))
print("%d horas." % (horas))
print("%d minutos." % (minutos))
print("%d segundos." % (segundos))

print("Totalizando %d segundos." % (total_segundos))