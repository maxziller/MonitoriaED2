class Arvore:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if (self.raiz == None):
            novo = Folha(valor)
            self.raiz = novo
            print("Raiz da árvore - "+valor)
            return True
        else:
            cidade = valor.split(" - ")
            print("vamos inserir: "+cidade[0])
            return self.raiz.insere(cidade[1],cidade[0])

    def busca(self, destino):
        if (self.raiz == None):
            return False
        else:
            return self.raiz.busca(destino)
            

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

    def insere(self, pai, novo):
        if (self.getvalor() == pai):
            if (self.esquerda == None):
                return self.insereesquerda(novo)
            else:
                return self.inseredireita(novo)
        else:
            inserido = False
            if (self.esquerda != None):
                inserido = self.esquerda.insere(pai,novo)
                if (inserido):
                    return True
            if (self.direita != None):
                inserido = self.direita.insere(pai,novo)
                if (inserido):
                    return True
        return False

    def insereesquerda(self, novo):
        if (self.esquerda == None):
            novono = Folha(novo)
            self.esquerda = novono
            novono.pai = self
            print("Inserido novo nó "+novono.getvalor()+" na esquerda do pai "+self.getvalor())
            return True
        else:
            return self.esquerda.insere(novo)

    def inseredireita(self, novo):
        if (self.direita == None):
            novono = Folha(novo)
            self.direita = novono
            novono.pai = self
            print("Inserido novo nó "+novono.getvalor()+" na direita do pai "+self.getvalor())
            return True
        else:
            return self.direita.insere(novo)

quantidadecidades = int(input())
destino = input()
cidades = []

mapa = Arvore()

for i in range(quantidadecidades):
    cidades.append(input())
    
for cidade in cidades:
    mapa.insere(cidade)

caminho = mapa.busca(destino)
for cidade in caminho:
    print(cidade)
