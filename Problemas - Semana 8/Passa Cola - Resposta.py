def tudocerto(respostas):
    for i in respostas:
        if not (i):
            return False
    return True

questoes = int(input())
alunos = int(input())
gabarito = input()
tacerto = []
for resposta in gabarito:
    tacerto.append(False)
respostas = []
for i in range(alunos):
    respostas.append(input())
i = 0
for resposta in respostas:
    i += 1
    for j in range(len(resposta)):
        if (resposta[j] == gabarito[j]):
            tacerto[j] = True
    if tudocerto(tacerto):
        break
print(i)   
