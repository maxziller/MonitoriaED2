import os

path = "C:/Users/Dell/Documents/Monitoria/Listas para testes"
for file in os.listdir(path):
    documento = []
    endereco = "C:/Users/Dell/Documents/Monitoria/Listas para testes/" + file
    with open(endereco, encoding='UTF-8') as arquivo:
        for line in arquivo:
            documento.append(line.rstrip())
    nomearquivoresposta = str(file)
    print(nomearquivoresposta)
    
    f = open(nomearquivoresposta,"x")
    for a in documento:
        w = a.lower()
        print(w)
        f.write(w + "\n")
    f.close()
