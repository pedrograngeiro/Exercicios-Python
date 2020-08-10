# Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 =4

n = int(input("Tabuada de: "))
x = 1
resultado = 0
while x <= 10:
    resultado = n * x
    print("%d x %d = %d" % (n, x, resultado))
    x = x + 1