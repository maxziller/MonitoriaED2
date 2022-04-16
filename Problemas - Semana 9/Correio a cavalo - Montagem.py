import os
import random

def distancia(xa, xb, ya, yb):
    d = float((xa-xb)**2) + ((ya-yb)**2)
    d = d**(1/2)
    d = round(d,5)
    return d

def novapartida(visitados,partidos):
    for i in range(len(visitados)):
        if ( visitados[i] and not partidos[i] ):
            return i
    return False

class Mapa():
    def __init__(self,capital):
        self.inicio = capital
        self.cidades = []
        self.matrizadjacencias=[]

    def inserecidade(self,cidade,x,y):
        tupla = (cidade,x,y)
        listanao = []
        i = len(self.matrizadjacencias)
        if (i == 0):
            self.matrizadjacencias.append([0])
        else:
            for a in range(i):
                listanao.append(False)
                self.matrizadjacencias[a].append(False)
        self.cidades.append(tupla)
        listanao.append(0)
        self.matrizadjacencias.append(listanao)
        return True

    def montarestradas(self):
        for i in range(len(self.cidades)):
            distancias = []
            for j in range(len(self.cidades)):
                if (i == j):
                    distancias.append(0)
                else:
                    a = self.cidades[i]
                    b = self.cidades[j]
                    d = distancia(a[1],b[1],a[2],b[2])
                    distancias.append(d)
            menores = [0,1,2,3]
            menores.sort()
            for d in range(4,len(distancias)):
                if (distancias[d] < distancias[menores[0]]):
                    menores[3] = menores[2]
                    menores[2] = menores[1]
                    menores[1] = menores[0]
                    menores[0] = d
                elif (distancias[d] < distancias[menores[1]]):
                    menores[3] = menores[2]
                    menores[2] = menores[1]
                    menores[1] = d
                elif (distancias[d] < distancias[menores[2]]):
                    menores[3] = menores[2]
                    menores[2] = d
                elif (distancias[d] < distancias[menores[3]]):
                    menores[3] = d
            for d in menores:
                self.matrizadjacencias[i][d] = distancias[d]
                self.matrizadjacencias[d][i] = distancias[d]
        return True

    def conectamapa(self):
        visitado = []
        partido = []
        for i in self.cidades:
            visitado.append(False)
            partido.append(False)

        visitado[0] = True
        conexao = 1
        
        while conexao < len(self.cidades):
            local = novapartida(visitado,partido)
            if (local != False):
                partido[local] = True
                for i in range(len(self.cidades)):
                    if (self.matrizadjacencias[local][i] != False):
                        visitado[i] = True
                        conexao += 1
                local = novapartida(visitado,partido)
            else:
                i = random.randint(0,len(self.cidades)-1)
                while (visitado[i]):
                    i = random.randint(0,len(self.cidades)-1)
                self.matrizadjacencias[local][i] = distancia(self.cidades[local][1],self.cidades[i][1],self.cidades[local][2],self.cidades[i][2])
                visitado[i] = True
                conexao += 1
        return True

    def retornaindice(self,cidade):
        for i in range(len(self.cidades)):
            if (self.cidades[i][0] == cidade):
                return i
        return False

    def retornacidades(self):
        retorno = []
        for cidade in self.cidades:
            texto = cidade[0] + " - x: " + str(cidade[1]) + " y: " + str(cidade[2])
            retorno.append(texto)
        caminhos = []
        for i in range(len(self.cidades)):
            for j in range(i+1,len(self.cidades)):
                if (self.matrizadjacencias[i][j] != False):
                    texto = self.cidades[i][0] + " tem estrada para " + self.cidades[j][0]
                    caminhos.append(texto)
        random.shuffle(caminhos)
        retorno = retorno + caminhos
        return retorno

path = "C:/Users/Dell/Documents/Monitoria/Problemas - Semana 7/Cidades.txt"
palavras = []
with open(path,encoding='utf8') as arquivo:
    for line in arquivo:
        linha = line.strip()
        if linha not in palavras:
            palavras.append(linha)
arquivo.close()
for a in range (6):
    pais = palavras.copy()

    quantidadecidades = 0
    for i in range(a + 3):
        quantidadecidades += 2 ** i

    cidades = random.sample(pais,k=quantidadecidades)
    origem = random.choice(cidades)
    destino = random.choice(cidades)
    cidades.pop(cidades.index(origem))
    cidades.insert(0,origem)
    pais = Mapa(origem)

    for i in range(quantidadecidades):
        x = random.randint(0,1000)
        y = random.randint(0,1000)
        pais.inserecidade(cidades[i],x,y)
        
    pais.montarestradas()
    pais.conectamapa()

    arquivopergunta = "Exemplo "+str(a)+".txt"
    f = open(arquivopergunta,"w")
    f.write( str(quantidadecidades) + "\n")
    f.write( destino + "\n")
    texto = pais.retornacidades()
    for linha in texto:
        f.write(linha)
        f.write("\n")
    f.write("Acabaram as estradas")
    f.close()
