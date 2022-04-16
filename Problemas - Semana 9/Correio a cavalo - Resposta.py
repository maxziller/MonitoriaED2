def aresta(x1, x2, y1, y2):
    a = float(x1)
    b = float(x2)
    d = (a-b)**2
    a = float(y1)
    b = float(y2)
    d += (a-b)**2
    d = d**(0.5)
    d = round(d,5)
    return d

class Mapa():
    def __init__(self,inicio):
        self.inicio = inicio
        self.cidades = []
        self.matrizadjacencias=[]
        self.x = []
        self.y = []
        self.quantidade = 0

    def novacidade(self,cidade,x,y):
        limites = []
        i = len(self.matrizadjacencias)
        if (i == 0):
            self.matrizadjacencias.append([0])
        else:
            for a in range(i):
                limites.append(False)
                self.matrizadjacencias[a].append(False)
        self.cidades.append(cidade)
        self.x.append(x)
        limites.append(0)
        self.y.append(y)
        self.quantidade += 1
        self.matrizadjacencias.append(limites)
        return True

    def retornaindice(self,cidade):
        for i in range(self.quantidade):
            if (self.cidades[i] == cidade):
                return i
        return False

    def criaestrada(self, cidade1, cidade2):
        a = self.retornaindice(cidade1)
        b = self.retornaindice(cidade2)
        d = aresta(self.x[a],self.x[b],self.y[a],self.y[b])
        self.matrizadjacencias[b][a] = d
        self.matrizadjacencias[a][b] = d
        return True
        
    def retornacidades(self):
        resp = []
        for cidade in self.cidades:
            texto = cidade[0] + " - x: " + str(cidade[1]) + " y: " + str(cidade[2])
            resp.append(texto)
        caminhos = []
        for i in range(len(self.cidades)):
            for j in range(i+1,len(self.cidades)):
                if (self.matrizadjacencias[i][j] != False):
                    texto = self.cidades[i][0] + " tem estrada para " + self.cidades[j][0]
                    caminhos.append(texto)
        random.shuffle(caminhos)
        retorno = resp + caminhos
        return resp

    def menorcaminho(self,inicio,destino):
        n = len( self.cidades)
        final = self.retornaindice(destino)
        comeco = self.retornaindice(inicio)
        caminho = [1000]*n
        fechado = [False]*n
        caminho[ final ] = 0
        fechado[ final ] = True
        fila = []
        local = final
        while not (fechado[comeco]):
            for i in range(n):
                if ( ( not fechado[i] ) and (self.matrizadjacencias[i][local]) ):
                    temp = self.matrizadjacencias[ local ][ i ] + caminho[ local ]
                    if (temp < caminho[i]):
                        caminho[i] = temp
            local = fechado.index(False)
            for i in range(n):
                if ( (caminho[i] < caminho[local]) and not ( fechado[i] ) ):
                    local = i
            fechado [local] = True
        return(caminho[comeco])
            

entrada = input()
n = entrada
n = int(n)
final = input()
pais = Mapa(1000)
for cout in range(n):
    cidade = input()
    cidade = cidade.split(" - ")
    coordenadas = cidade[1].split(": ")
    cidade = cidade[0]
    x = coordenadas[1][:-2]
    y = coordenadas[2]
    x = int(x)
    y = int(y)
    pais.novacidade(cidade,x,y)
inicio = pais.cidades[0]
estrada = input()
while (estrada != "Acabaram as estradas"):
    pontas = estrada.split(" tem estrada para ")
    pais.criaestrada(pontas[0],pontas[1])
    estrada = input()
distancia = pais.menorcaminho(inicio,final)
print(distancia)
