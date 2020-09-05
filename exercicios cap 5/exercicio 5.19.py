valor_float = float(input("Digite o valor que você quer sacar, se necessário digite quantos cents: "))
valor_int = int(valor_float)
print(valor_int)


# Parte cédula
valor_dinheiro = valor_int
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
            céd = 2
        elif céd == 2:
            céd = 1
        totcéd = 0
        if total == 0:
            break

valor_float = valor_float - valor_int
valor_float = valor_float * 100
total = round(valor_float,2)
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total = total - céd
        totcéd = totcéd + 1
    else:
        if totcéd > 0:
            print("Total de %d moedas de %d" % (totcéd, céd))
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        elif céd == 2:
            céd = 1
        totcéd = 0
        if total == 0:
            break