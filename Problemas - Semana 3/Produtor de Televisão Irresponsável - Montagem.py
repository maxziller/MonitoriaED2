"""
Este é o documento com uma proposta de solução do problema Produtor de Televisão Irresponsável. A solução para o problema é feita para fins didáticos.
Monitor autor: Max Pereira Ziller
Disciplina: Estrutura de Dados II
Janeiro de 2022

10 - PRODUTOR DE TELEVISÃO IRRESPONSÁVEL

Você trabalha na equipe de um reality show que está a uma semana de começar. Com pouco prazo pra levar todos os participantes para a ilha onde ocorrerão as gravações, o diretor da equipe ainda está correndo com as coisas. Na verdade, parece até que ele nem começou a organizar nada!

Hoje, o diretor te chamou na sala dele pra te delegar uma tarefa que disse ser urgente. Ele então explicou que até agora não selecionou os participantes e não há mais tempo para estudar todos os quase 20000 candidatos. Passado o seu choque, você presta atenção no que fazer para resolver o problema.

O diretor te orienta a listar todos os candidatos do reality imediatamente e ordená-los em ordem alfabética. Os participantes selecionados serão aqueles que, na ordem, estarão em posições na lista relativas a potências de 2. Ou seja, o primeiro nome da lista, o segundo, o quarto, o oitavo, o décimo sexto e assim sucessivamente.

A lista é grande, então é melhor utilizar métodos de ordenação eficientes para ter tempo hábil de convocar os participantes. É melhor começar logo!

Entrada
Na primeira linha tem o número de candidatos que estão na lista para serem organizados. 

Cada linha seguinte contém uma string contendo o nome de um candidato.

Você pode assumir que a string com o nome dos estudantes não tem mais que 100 caracteres.

Saída
Para cada linha, o seu programa deve retornar uma string com o nome de um participante selecionado, em ordem alfabética.

"""

import os

#Função Ordenar ordena a lista.
#Primeiro, ordena-se os nomes em ordem alfabética pelo método MergeSort
def ordenar(lista):
    pessoas = merge(lista)
    
    return pessoas

def merge(lista):

    fim = len(lista)-1
    if (fim < 1):
        return lista
    else:
        meio = len(lista)//2
        esquerda = lista[:meio]
        direita = lista[meio:]

        esquerda = merge(esquerda)
        direita = merge(direita)

        novalista=[]
        

        # Loop corre enquanto houver elementos à esquerda e à direita e monta uma lista auxiliar de forma ordenada
        while len(esquerda) > 0 and len(direita) > 0:
            if esquerda[0] <= direita[0]:
                novoelem = esquerda.pop(0)
                novalista.append( novoelem )
            else:
                novoelem = direita.pop(0)
                novalista.append( novoelem )
            

        while len(esquerda) > 0:
            novoelem = esquerda.pop(0)
            novalista.append( novoelem )

        while len(direita) > 0:
            novoelem = direita.pop(0)
            novalista.append( novoelem )
        return novalista


def selecionar(candidatos):
    i = 0
    posicao = 0
    novalista = []
    tamanho = len(candidatos)
    while posicao < tamanho:
        elemento = candidatos[posicao]
        novalista.append(elemento)
        i += 1
        posicao = 2 ** i - 1
    return novalista

path = "C:/Users/Dell/Documents/Monitoria/Entradas"
for file in os.listdir(path):
    documento = []
    endereco = "C:/Users/Dell/Documents/Monitoria/Entradas/" + file
    with open(endereco) as arquivo:
        for line in arquivo:
            documento.append(line.rstrip())
    nomearquivoresposta = str(file)[0:-4] + "- resposta.txt"
    print(nomearquivoresposta)

    n = documento[0]
    #n = input()
    candidatos = []

    contador = 0
    while contador < int(n):
        nome = documento[contador + 1].lower()
        #nome = input()
        candidatos.append(nome)
        contador += 1

    candidatos = ordenar (candidatos)

    participantes = selecionar(candidatos)

    for p in participantes:
        print(p)
    
    f = open(nomearquivoresposta,"x")
    for a in participantes:
        print(a)
        f.write(a + "\n")
    f.close()
