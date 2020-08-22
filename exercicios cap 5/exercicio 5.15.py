# Escreva um programa para controlar uma pequena máquina registradora.
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de códigos abaixo para obeter o preço de cada produto:
#       Código      Preço
#         1         0,50
#         2         1,00
#         3         4,00
#         5         7,00
#         9         8,00
# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve geral a mensagem de erro " Código invalido"

print("-----Maquina Registradora-----")
codigo = 0
quant = 0
preco = 0
while True:
    codigo = int(input("Digite o código do produto: "))
    if codigo == 1:
        preco = preco + 0.50
    elif codigo == 2:
        preco = preco + 1.00
    elif codigo == 3:
        preco = preco + 4.00
    elif codigo == 5:
        preco = preco + 7.00
    elif codigo == 9:
        preco = preco + 8.00
    elif codigo == 0:
        break
    else:
        print("Código invalido.")
        quant = quant - 1

    print("Total da compra: R$%5.2f" % (preco))
    quant = quant + 1
