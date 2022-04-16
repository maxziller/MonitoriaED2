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

def medalhas(atleta):
    select = atleta.split(" ",1)
    return (int(select[0]))

def quicksort(lista):
    pivo = lista[0]
    esquerda = []
    direita = []

    for i in lista[1:]:
        if medalhas(i) < medalhas(pivo):
            esquerda.append(i)
        else:
            direita.append(i)
            
    if (len(esquerda) > 1):
        ordenaesquerda = quicksort(esquerda)
    else:
        ordenaesquerda = esquerda
    if (len(direita) > 1):
        ordenadireita = quicksort(direita)
    else:
        ordenadireita = direita
    
    ordenaesquerda.append(pivo)
    listaconjunta = ordenaesquerda + ordenadireita
    return listaconjunta

n = input()
h = input()
atletas = []

for i in range(int(n)):
    atleta = input()
    atletas.append(atleta)

atletas = quicksort(atletas)

homenageados = atletas[:int(h)]

for p in homenageados:
    nome = p.split(" ",1)
    print(nome[1])

