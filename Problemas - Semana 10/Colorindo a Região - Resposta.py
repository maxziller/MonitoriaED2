class Mapa:
    def __init__(self):
        self.cidades = []
        self.limites = []

    def inserecidade(self,cidade):
        local = [False] * len(self.cidades)
        self.cidades.append(cidade)
        local.append(False)
        for limite in self.limites:
            limite.append(False)
        self.limites.append(local)
        return True

    def crialimite(self,entrada):
        limite = entrada.split(" faz limite com ")
        i = limite[0]
        i = self.cidades.index(i)
        j = limite[1]
        j = self.cidades.index(j)
        self.limites[i][j] = True
        self.limites[j][i] = True
        return True

    def dsatur(self):
        quantidade = len(self.cidades)
        ordem = []
        cor = [False] * quantidade
        for i in range(quantidade):
            ordem.append(i)
        ordem.sort(reverse=True, key=self.grau)
        for cidade in ordem:
            corusada = set()
            for i in range(quantidade):
                if ( (self.limites[cidade][i]) and (cor[i] != False) ):
                    corusada.add(cor[i])
            corusada.discard(False)
            corusada = list(corusada)
            corusada.sort()
            if (len(corusada) == 0):
                cor[cidade] = 1
            elif( corusada[-1] == len(corusada) ):
                cor[cidade] = len(corusada)+1
            else:
                for i in range(1,len(corusada)):
                    if (i != corusada):
                        cor[cidade] = i
                        break
        cor.sort()
        return cor[-1]
                    

    def grau(self, indice):
        i = 0
        for cidade in self.limites[indice]:
            if (cidade):
                i+=1
        return i

pais = Mapa()
n = int(input())
for i in range(n):
    cidade = input()
    pais.inserecidade(cidade)
limite = input()
while (limite != "O mapa está completo"):
    pais.crialimite(limite)
    limite = input()
print(pais.dsatur())
