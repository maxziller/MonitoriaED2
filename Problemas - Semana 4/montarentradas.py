import os
import random

path = "C:/Users/Dell/Documents/Monitoria/Entradas"
for file in os.listdir(path):
    documento = []
    endereco = path + "/" + file
    with open(endereco) as arquivo:
        for line in arquivo:
            documento.append(line.rstrip())
    nomearquivoresposta = str(file)
    print(nomearquivoresposta)

    entrada = []
    quantidade = int(documento.pop(0))
    homenageados = int(quantidade ** 0.5)

    entrada.append(str(quantidade))
    entrada.append(str(homenageados))
    
    
    for linha in documento:
        escrito = str( random.randint(1, 10*quantidade)) + " " + linha
        entrada.append( escrito )
        
    
    f = open(nomearquivoresposta,"x")
    for a in entrada:
        w = a.lower()
        f.write(w + "\n")
    f.close()
