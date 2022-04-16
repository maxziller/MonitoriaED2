
def inserecarga(pilhas, carga):
    i = 0
    while (i < len(pilhas)):
        if (pilhas[i] >= carga):
            pilhas[i] = carga
            return pilhas
        else:
            i += 1
    pilhas.append(carga)
    return pilhas

def organizapilhas(cargas):
    pilhas = []
    i = 0
    for carga in cargas:
        pilhas = inserecarga(pilhas, carga)
    return len(pilhas)
    

entrada = input()
i = 1
while (entrada != "fim"):
    n = organizapilhas(entrada)
    print("Caso " + str(i) + ": " + str(n))
    i += 1
    entrada = input()
