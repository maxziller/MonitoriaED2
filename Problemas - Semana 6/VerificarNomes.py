import os

path = "C:/Users/Dell/Documents/Monitoria/Problemas - Semana 6/"

for file in os.listdir(path):
    documento = []
    endereco = path + file
    with open(endereco) as arquivo:
        for line in arquivo:
            documento.append(line.rstrip())
        documento.pop(0)
    dicionario = {}
    for nome in documento:
        if ";" in nome:
            menos = nome.split(";")
            
            if menos[0] in dicionario:
                print (file + ": " + nome)
            else:
                dicionario.update({menos[0]: nome})
