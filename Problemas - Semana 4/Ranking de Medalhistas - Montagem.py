"""
Este é o documento com uma proposta de solução do problema Ranking de Medalhistas. A solução para o problema é feita para fins didáticos.
Monitor autor: Max Pereira Ziller
Disciplina: Estrutura de Dados II
Janeiro de 2022

A população de Saturno está em festa com a realização da milésima edição dos Jogos Olímpicos Saturnianos! A competição acontece apenas uma vez a cada 4 anos, o que é muito tempo se considerarmos que cada ano em Saturno dura 29 anos terrestres. Para homenagear os maiores exemplos do esporte de sua história, o Comitê Olímpico vai organizar uma lista de homenageados com os maiores medalhistas olímpicos de todos os 999 Jogos que já ocorreram. A quantidade de homenageados ainda não foi definida, pois depende de outros fatores que não estão sob sua responsabilidade. Mas você foi encarregado de rankear todos os atletas pela quantidade de Medalhas de Lítio (não pergunte, aparentemente os saturnianos acham lítio um metal muito precioso). Mas é bom você utilizar um método eficiente, pois em 999 edições, muitos atletas já foram medalhistas.

Entrada
A primeira linha da entrada contém o número de atletas N que houve na história de Saturno. A segunda linha da entrada contém o número H de atletas a serem homenageados As N linhas seguintes contém um número de medalhas que um atleta ganhou, seguindo pelo nome do atleta

Saída
A saída deve imprimir, em cada linha, em ordem de melhor qualificado para o pior qualificado, um nome de atleta. A resposta só deve imprimir a quantidade H dos primeiros colocados no ranking. Não há necessidade de tratar casos de empate, pois há a certeza de que isso não ocorrerá em Saturno.

Exemplo de Entrada
8
3
2 Blumberg Silva
4 Jabba The Hut
1 ET Bilu
8 Clefairy Pokemon
15 J'onn J'onzz
5 Sailor Moon
7 Steven Universo
9 M'gann M'orzz

Exemplo de Saída
J'onn J'onzz
M'gann M'orzz
Clefairy Pokemon
"""

import os

def medalhas(atleta):
    coloc = atleta.split(" ",1)
    return (int(coloc[0]))

path = "C:/Users/Dell/Documents/Monitoria/Problemas - Semana 4/Entrada/"
for file in os.listdir(path):
    documento = []
    endereco = path + file
    with open(endereco) as arquivo:
        for line in arquivo:
            documento.append(line.rstrip())
    nomearquivoresposta = str(file)[0:-4] + "- resposta.txt"
    print(nomearquivoresposta)

    n = int( documento.pop(0) )
    #n = input()
    h = int( documento.pop(0) )
    #h = input()
    atletas = []

    for i in range(n):
        atleta = documento[i]
        atletas.append(atleta)

    atletas.sort(reverse=True,key=medalhas)

    homenageados = atletas[:h]
    
    f = open(nomearquivoresposta,"x")
    for a in homenageados:
        nome = a.split(" ",1)
        f.write(nome[1] + "\n")
    f.close()
