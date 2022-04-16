import os
import random
import math

class Pessoa:
    def __init__(self, nome, cpf, idade, telefone, valor):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.telefone = telefone
        self.valor = valor
        self.visitas = 1

    def imprime(self):
        texto = self.nome + ";" + self.cpf + ";" + str(self.idade)+ ";" + self.telefone+ ";" + self.valor
        return texto


def mediaidades(pessoas):
    idade = 0
    quantidade = len(pessoas)
    for pessoa in pessoas:
        idade += pessoa.idade
    media = float(idade)/quantidade
    media = round(media, 4)
    return media

def maiorvalor(pessoas):
    maior = pessoas[0]
    for p in pessoas[1:]:
        if p.valor > maior.valor:
            maior = p
    return maior

def visitas(pessoa):
    return pessoa.visitas

def maisvisitas(pessoas):
    ordenado = pessoas.copy()
    ordenado.sort(key = visitas,reverse = True)
    return ordenado[:5]

def escolheidade():
    return random.randint(18,65)

def escolhecpf():
    cpf = ""
    numeros = []
    primeiro = 0
    segundo = 0
    for i in range(9):
        n = random.randint(0,9)
        numeros.append (n)
        primeiro += (10-i)*n
        segundo += (11-i)*n
    j = primeiro % 11
    if (j <= 1):
        numeros.append(0)
    else:
        numeros.append( 11-j )
        segundo += 2*(11-j)

    k = segundo % 11
    if (k <= 1):
        numeros.append(0)
    else:
        numeros.append(11-k)

    for numero in numeros:
        cpf += str(numero)

    cpf = cpf[:3]+"."+cpf[3:6]+"."+cpf[6:9]+"-"+cpf[9:]

    return cpf

def escolhetelefone():
    tel = ""
    for i in range(10):
        n = random.randint(0,9)
        tel += str(n)
    tel = "("+tel[:2]+")9"+tel[2:6]+"-"+tel[6:]
    return tel

def escolhevalor():
    valor = round(random.uniform(0.00,100000.00),2)
    din = str(valor)
    return din

def sortenovo(i,n):
    porcentagem = (1/float(i+1))*(float(n)**0.5)
    sortear = random.random()
    if sortear < porcentagem:
        return True
    else:
        return False

nomes = []
path = "C:/Users/Dell/Documents/Monitoria/Entradas"
for file in os.listdir(path):
    documento = []
    endereco = "C:/Users/Dell/Documents/Monitoria/Entradas/" + file
    with open(endereco) as arquivo:
        for line in arquivo:
            documento.append(line.rstrip())
        documento.pop(0)
    nomes += documento

primeirosnomes = []
sobrenomes = []
for nome in nomes:
    x = nome.split(" ")
    primeirosnomes.append(x[0])
    sobrenomes.append(x[-1])

arquivos = 7

for x in range (arquivos):
    n = input()
    pessoas = []
    arquivoentrada = "Teste " + str(x) + ".txt"
    arquivosaida = "Resposta " + str(x) + ".txt"
    f = open(arquivoentrada,"w")
    f.write(str(n)+"\n")

    for i in range(int(n)):
        if (sortenovo(i,n)):
            name = primeirosnomes[ random.randrange( len(primeirosnomes) ) ] + " " + sobrenomes[ random.randrange( len(sobrenomes) ) ]
            cpf = escolhecpf()
            idade = escolheidade()
            telefone = escolhetelefone()
            valor = escolhevalor()
            p = Pessoa(name, cpf, idade, telefone, valor)
            pessoas.append(p)
            linha = p.imprime()
        else:
            p = random.choice(pessoas)
            p.visitas += 1
            linha = p.nome
        linha += "\n"
        f.write(linha)
    f.close()

    f = open(arquivosaida,"w")
    media = mediaidades(pessoas)
    f.write(str(media) + "\n")
    rico = maiorvalor(pessoas)
    texto = rico.nome + " " + rico.telefone + "\n"
    f.write(texto)
    assiduos = maisvisitas(pessoas)
    for assiduo in assiduos:
        texto = assiduo.nome + " " + assiduo.cpf + "\n"
        f.write(texto)
    f.close()
