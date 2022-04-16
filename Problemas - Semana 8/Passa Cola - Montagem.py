import os
import random

def montarespostas(respostas,qtdd):
    resposta = ""
    for i in range(qtdd):
        letra = random.choice(respostas)
        resposta += letra
    return resposta

print("O número de respostas possíveis")
n = input()
respostas = []
letra = 'A'
entrada = []
for i in range(int(n)):
    respostas.append(letra)
    letra = ord(letra)
    letra += 1
    letra = chr(letra)

print("O número de questões")
i = input()
print("O número de alunos")
j = input()
entrada.append(i)
entrada.append(j)
alunos = []


gabarito = montarespostas(respostas,int(i))
entrada.append(gabarito)
for d in range(int(j)):
    resposta = montarespostas(respostas,int(i))
    entrada.append(resposta)
    alunos.append(resposta)

cola = []
for c in range(int(i)):
    cola.append(c)
c = 0
while ( (len(cola)>0) and (c < int(j)) ):
    aluno = alunos[c]
    for k in cola:
        if (aluno[k] == gabarito[k]):
            cola.remove(k)
    c += 1
if (len(cola)>0):
    c = "Não conseguiram"
print("O nome do arquivo da resposta")
arquivo = input()
arquivo += ".txt"
print("A resposta é:")
with open(arquivo, 'w') as f:
    for linha in entrada:
        f.write(linha + "\n")
f.close()
print(c)
