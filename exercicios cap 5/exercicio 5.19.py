
print("=" * 30)
print("{:^30}" . format("BANCO CEV"))
print("=" * 30)

# Parte cédula
valor_dinheiro = int(input("Que valor você quer sacar? R$"))
total = valor_dinheiro
céd = 100
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f"Total de {totcéd} cédulas de R${céd}")
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totcéd = 0
        if total == 0:
            break

# Parte moeda
valor_moeda = int(input("Digite a parte da moeda: "))
total = valor_moeda
moeda = 50
totmoeda = 0

while True:
    if total >= moeda:
        total -= moeda
        totmoeda += 1
    else:
        if totmoeda > 0:
            print(f"Total de {totmoeda} moedas de R${moeda}")

        if moeda == 50:
            moeda = 20
        elif moeda == 20:
            moeda = 10
        elif moeda == 10:
            moeda = 5
        elif moeda == 5:
            moeda = 1
        totmoeda = 0
        if total == 0:
            break