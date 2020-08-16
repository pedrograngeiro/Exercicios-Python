# Modifique o programa da listagem 5.10 para que aceite respostas com letras maúslas em todas as questões

pontos = 0
questao = 1
while questao <= 3:
    resposta = input("Resposta da questão %d: " % questao)
    if questao == 1 and resposta == "B" or resposta == "b":
        pontos = pontos + 1
    if questao == 2 and resposta == "A" or resposta == "a":
        pontos = pontos + 1
    if questao == 3 and resposta == "D" or resposta == "d":
        pontos = pontos + 1
    questao = questao + 1
print("O aluno fez %d ponto(s)" % pontos)