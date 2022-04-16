"""
Este é o documento com uma proposta de solução do problema Ranking de Medalhistas. A solução para o problema é feita para fins didáticos.
Monitor autor: Max Pereira Ziller
Disciplina: Estrutura de Dados II
Janeiro de 2022

Você e seus amigos estão numa biblioteca que está organizada de uma forma um pouco confusa. Os livros não estão organizados por tema ou autor,
mas apenas com a ordem alfabética de todos os seus títulos. Cada estante tem expresso no canto, no entanto, o nome do primeiro livro que guarda.
Dessa forma, vocês precisam primeiro encontrar em que estante o livro que querem ler se encontra.

Entrada
A primeira linha da entrada terá a quantidade M de estantes que há na biblioteca A segunda linha, a quantidade N de amigos que estão com você procurando
livros A partir daí, haverá N entradas com os títulos que cada amigo seu está procurando Depois, haverá M entradas com os títulos que constam nas estantes
como sendo o primeiro livro de sua ordem

Saída
A saída deverá constar com M títulos de livro, sendo cada título o indicador da estante onde o seu amigo consegue encontrar o livro. A ordem da resposta
deve ser a mesma que seus amigos te pediram os livros.

Exemplo de Entrada

8
2
Drácula
Os Filhos da Meia-Noite
A Divina Comédia
Cem Anos de Solidão
Harry Potter
Metamorfoses
O Mestre e Margarida
Robinson Crusoe
The Handmaid's Tale
Wide Sargasso Sea

Exemplo de Saída

Cem Anos de Solidão
O Mestre e Margarida
"""

#Função recebe como parâmetros o título do livro procurado e a lista das estantes
#Pelo descrição do problema, um livro estará numa estante quando o primeiro livro da próxima estante estiver, na ordem alfabética, depois do livro buscado
# BUSCA LINEAR
def buscaestante(livro,estantes):
    for i in range(len(estantes)):
        if livro < estantes[i]:
            return estantes[i-1]
    #Caso não encontre uma estante com o primeiro livro depois na ordem alfabética que o procurado, significa que ele está na última estante
    return estantes[-1]

n = int(input())
amigos = int(input())

procurados = []
estantes = []

for i in range(amigos):
    procurados.append( input() )

for i in range(n):
    estantes.append( input() )

for livro in procurados:
    print( buscaestante(livro,estantes))
