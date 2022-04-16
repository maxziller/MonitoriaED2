class Pessoa:
    def __init__(self, nome, cpf, idade, telefone, valor, visitas = 1):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.telefone = telefone
        self.valor = valor
        self.visitas = visitas

    def imprime(self):
        texto = self.nome + ";" + self.cpf + ";" + str(self.idade)+ ";" + self.telefone+ ";" + self.valor
        return texto

    def getnome(self):
        return self.nome

    def getcpf(self):
        return self.cpf

    def getidade(self):
        return self.idade

    def gettelefone(self):
        return self.telefone

    def getvalor(self):
        return self.valor

    def getvisitas(self):
        return self.visitas

    def novavisita(self):
        self.visitas += 1
        return True


def buscabinaria(vetor, inicio, fim, elemento):
    meio = (fim + inicio)//2
    if (vetor[meio] == elemento):
        return meio
    elif (inicio == fim):
        return None
    elif (vetor[meio] > elemento):
        return buscabinaria(vetor, inicio, meio, elemento)
    else:
        return buscabinaria(vetor, meio, fim, elemento)

def mediaidades(pessoas):
    idade = 0
    quantidade = len(pessoas)
    for pessoa in pessoas:
        idade += pessoas[pessoa].idade
    media = float(idade)/quantidade
    media = round(media, 4)
    return media

def maiorvalor(pessoas):
    maior = list(pessoas.keys())[0]
    for p in pessoas:
        if pessoas[p].valor > pessoas[maior].valor:
            maior = p
    return pessoas[maior]

def visitas(pessoa):
    return pessoa[1].visitas

def maisvisitas(pessoas):
    ordenado = list(pessoas.items())
    ordenado.sort(key = visitas,reverse = True)
    return ordenado[:5]



clientes = {}
n = int(input())
for i in range(n):
    entrada = input()
    if ";" in entrada:
        dados = entrada.split(";")
        cliente = Pessoa(dados[0],dados[1],int(dados[2]),dados[3],float(dados[4]))
        clientes[dados[0]] = cliente
    else:
        clientes[entrada].novavisita()

print(mediaidades(clientes))
rico = maiorvalor(clientes)
print(rico.nome + " " + rico.telefone)
assiduos = maisvisitas(clientes)
for i in assiduos:
    print (i[1].nome + " " + i[1].cpf + " visitou " + str(i[1].visitas) + " vezes")
