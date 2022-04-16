import os
import random

class Arvore:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        novo = Folha(valor)
        if (self.raiz == None):
            self.raiz = novo
            return True
        else:
            return self.raiz.insere(novo)

    def inserealeatorio(self,valor):
        novo = Folha(valor)
        if (self.raiz == None):
            self.raiz = novo
            return True
        else:
            return self.raiz.inserealeatorio(novo)

    def busca(self, destino):
        if (self.raiz == None):
            return False
        else:
            return self.raiz.busca(destino)

    def escrevearquivo(self, arquivo):
        if (self.raiz == None):
            arquivo.write("Mapa vazio")
            return False
        else:
            return self.raiz.escrevearquivo(arquivo)
            

class Folha:
    def __init__(self, valor):
        self.valor = valor
        self.pai = None
        self.esquerda = None
        self.direita = None

    def getvalor(self):
        return self.valor

    def busca(self, destino):
        if (self.getvalor() == destino):
            return [self.getvalor()]
        else:
            if (self.esquerda != None):
                caminho = self.esquerda.busca(destino)
                if(caminho != None):
                    caminho.insert(0,self.getvalor())
                    return caminho
            if (self.direita != None):
                caminho = self.direita.busca(destino)
                if (caminho != None):
                    caminho.insert(0,self.getvalor())
                    return caminho
        return None

    def escrevearquivo(self, arquivo):
        texto = self.getvalor()
        if (self.pai != None):
            texto += " - " + self.pai.getvalor()
        texto += "\n"
        arquivo.write(texto)
        if (self.esquerda != None):
            self.esquerda.escrevearquivo(arquivo)
        if (self.direita != None):
            self.direita.escrevearquivo(arquivo)
        return True

    def insere(self, novo):
        if (novo.getvalor() > self.getvalor()):
            return self.inseredireita(novo)
        else:
            return self.insereesquerda(novo)

    def insereesquerda(self, novo):
        if (self.esquerda == None):
            self.esquerda = novo
            novo.pai = self
            return True
        else:
            return self.esquerda.insere(novo)

    def inseredireita(self, novo):
        if (self.direita == None):
            self.direita = novo
            novo.pai = self
            return True
        else:
            return self.direita.insere(novo)

    def inserealeatorio(self, novo):
        lado = random.choice([True,False])
        if (lado):
            if (self.esquerda == None):
                self.insereesquerda(novo)
                return True
            else:
                return self.esquerda.inserealeatorio(novo)
        else:
            if (self.direita == None):
                self.inseredireita(novo)
                return True
            else:
                return self.direita.inserealeatorio(novo)

path = "C:/Users/Dell/Documents/Monitoria/Problemas - Semana 7/Cidades.txt"
palavras = []
with open(path,encoding='utf8') as arquivo:
    for line in arquivo:
        linha = line.strip()
        if linha not in palavras:
            palavras.append(linha)

for x in range (6):
    pais = palavras.copy()

    quantidadecidades = 0
    for i in range(x + 4):
        quantidadecidades += 2 ** i

    cidades = random.choices(pais,k=quantidadecidades)
    destino = random.choice(cidades)
    mapa = Arvore()
    
    for cidade in cidades:
        mapa.inserealeatorio(cidade)

    arquivoentrada = "Teste "+str(x)+".txt"
    arquivosaida = "Resposta "+str(x)+".txt"
    f = open(arquivoentrada,"w")
    f.write(str(quantidadecidades))
    f.write("\n")
    f.write(destino)
    f.write("\n")
    mapa.escrevearquivo(f)
    f.close()

    caminho = mapa.busca(destino)

    f = open(arquivosaida,"w")
    for cidade in caminho:
        f.write(cidade)
        f.write("\n")
    f.close()
