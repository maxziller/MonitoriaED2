"""
Este é o documento com uma proposta de solução do problema Produtor de Televisão Irresponsável. A solução para o problema é feita para fins didáticos.
Monitor autor: Max Pereira Ziller
Disciplina: Estrutura de Dados II
Janeiro de 2022

Uma medida de "desorganização" em uma sequência é o número de pares de entradas que estão fora de ordem com respeito um ao outro.

Por exemplo, na seqüência de letras “DAABEC”, a medida de desorganização é 5, já que D é maior do que quatro letras à sua direita e E é maior do que uma letra à sua direita. Esta medida é chamada o número de inversões na sequência. A sequência “AACEDGG” possui apenas uma inversão (E e D) e está quase ordenada enquanto ZWQM tem 6 inversões e está desorganizada o máximo possível.

Em Bioinformática é possível avaliar a similaridade entre sequências DNA a partir da medida de desorganização. Sequências de DNA são longas sequências das letras A, D, G e T que codificam todas as funções biológicas em seres vivos.

Neste exercício você vai programar uma parte da análise dessas sequências. Você deve ordenar bases de sequências de DNA de acordo com a ordem de organização (e não usando a ordem alfabética). Observe que todas as sequências em uma base o mesmo número de letras.

Entrada
A primeira linha da entrada é um inteiro M que é seguida por uma linha em branco. Em seguida há M conjuntos de sequências que são separados entre si por uma linha em branco.

A primeira linha de cada conjunto de dados contém dois inteiros: um inteiro positivo N (0 < N < 51) que indica o tamanho das sequências; e um inteiro positivo K (0 < K < 101) fornecendo o número de sequências. Esses são seguidos por K linhas, cada uma contendo uma sequência de comprimento N.

Saída
Para cada conjunto de sequências, imprimir a lista começando da sequência mais organizada e terminando na menos organizada. Se duas sequências tem a mesma medida de organização, você deve imprimí-las na mesma ordem em que elas apareceram na entrada. Separe os conjuntos de sequências ordenadas por uma linha em branco.

"""

def getmedida(tupla):
    return tupla[1]

def desorganizacao (dna):
    i = 0
    tamanho = len(dna)
    medida = 0
    while i < tamanho:
        j = i
        while j < tamanho:
            if (dna[i] > dna[j]):
                medida += 1
            j += 1
        i += 1
    return medida
    


n = input()
contador = 0

while contador < int(n):
    espaco = input()
    espaco = "\n"
    if (contador > 0):
        print("")
    contador += 1
    quantidades = input()
    valores = quantidades.split()
    tamanho = int(valores[0])
    linhas = int(valores[1])
    contador2 = 0
    sequencias = []
        
    while contador2 < linhas:
        dna = input()
        medidadesorganizacao = desorganizacao(dna)
        tupla = ( dna, medidadesorganizacao )
        sequencias.append(tupla)
        contador2 += 1
    sequencias.sort(key = getmedida)
    for s in sequencias:
        print(s[0])
        
