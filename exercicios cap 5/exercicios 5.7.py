# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada
# em vez de começar com 1 e 10

n = int(input("Tabuada de: "))
x = int(input("Começando por vezes: x"))
fim = int(input("Terminando em vezes: x"))
resultado = 0
while x <= fim:
    resultado = n * x
    print("%d x %d = %d" % (n, x, resultado))
    x = x + 1