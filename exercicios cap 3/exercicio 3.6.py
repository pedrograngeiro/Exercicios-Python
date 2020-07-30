# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
# Para ser aprovado, todas as médias do aluno devem ser maiores que 7.
# Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes
# variáveis: matéria1, matéria2 e matéria3.

materia1 = int(input("Digite a nota da materia1: "))
materia2 = int(input("Digite a nota da materia2: "))
materia3 = int(input("Digite a nota da materia3: "))

print("A nota da materia 1 foi %d" % (materia1))
print("A nota da materia 2 foi %d" % (materia2))
print("A nota da materia 3 foi %d" % (materia3))
# Condição Materia1
if materia1 >= 7:
    materia1 = True
else:
    materia1 = False
###########################

# Condição Materia2
if materia2 >= 7:
    materia2 = True
else:
    materia2 = False
###########################

# Condição Materia3
if materia3 >= 7:
    materia3 = True
else:
    materia3 = False
##########################



aluno = materia1 + materia2 + materia3

# True recebe o valor de 1 e se resultado = 3 aprovado.
if aluno == 3:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")