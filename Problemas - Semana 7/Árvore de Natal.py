global atual
global resposta

def ordena(prefixa, infixa, i, j):
    if (i <= j):
        global atual
        global resposta
        posicao = infixa.index(prefixa[atual])
        atual = atual + 1
        ordena(prefixa, infixa, i, posicao - 1)
        ordena(prefixa, infixa, posicao + 1, j)
        resposta.append(infixa[posicao])

try:
    while(1):
        entrada = input()
        atual = 0
        prefixa = entrada.split(" ")
        infixa = prefixa[1]
        prefixa = prefixa[0]
        resposta = []
        ordena(prefixa, infixa, 0, len(prefixa)-1)
        impressao = ""
        for c in resposta:
            impressao += c
        print (impressao)
except EOFError:
    atual = 0
