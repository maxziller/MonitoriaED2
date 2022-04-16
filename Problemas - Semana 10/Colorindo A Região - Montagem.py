import os
import random


def novapartida(visitados,partidos):
    i = random.randint(0,len(visitados)-1)
    return i
    return False

class Mapa():
    def __init__(self):
        self.cidades = []
        self.matrizadjacencias=[]

    def inserecidade(self,cidade):
        listanao = []
        i = len(self.matrizadjacencias)
        if (i == 0):
            self.matrizadjacencias.append([0])
        else:
            for a in range(i):
                listanao.append(False)
                self.matrizadjacencias[a].append(False)
        self.cidades.append(cidade)
        listanao.append(0)
        self.matrizadjacencias.append(listanao)
        return True

    def conectamapa(self):
        visitado = []
        partido = []
        for i in self.cidades:
            visitado.append(False)
            partido.append(False)

        visitado[0] = True
        conexao = 1
        
        while conexao < len(self.cidades)*4:
            local = novapartida(visitado,partido)
            if (local != False):
                partido[local] = True
                i = random.randint(0,len(visitado)-1)
                if ( (self.matrizadjacencias[local][i] != False) or ( i == local)):
                    visitado[i] = True
                else:
                     self.matrizadjacencias[local][i] = True
                conexao += 1
                local = novapartida(visitado,partido)
        return True

    def retornaindice(self,cidade):
        for i in range(len(self.cidades)):
            if (self.cidades[i][0] == cidade):
                return i
        return False

    def retornacidades(self):
        retorno = []
        for cidade in self.cidades:
            texto = cidade
            retorno.append(texto)
        caminhos = []
        for i in range(len(self.cidades)):
            for j in range(i+1,len(self.cidades)):
                if (self.matrizadjacencias[i][j] != False):
                    texto = self.cidades[i] + " faz limite com " + self.cidades[j]
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
    cidades.pop(cidades.index(origem))
    cidades.insert(0,origem)
    pais = Mapa()

    for i in range(quantidadecidades):
        pais.inserecidade(cidades[i])
    
    pais.conectamapa()

    arquivopergunta = "Exemplo "+str(a)+".txt"
    f = open(arquivopergunta,"w")
    f.write( str(quantidadecidades) + "\n")
    texto = pais.retornacidades()
    for linha in texto:
        f.write(linha)
        f.write("\n")
    f.write("O mapa está completo")
    f.close()
