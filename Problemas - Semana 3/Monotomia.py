"""
Este é o documento com uma proposta de solução do problema Produtor de Televisão Irresponsável. A solução para o problema é feita para fins didáticos.
Monitor autor: Max Pereira Ziller
Disciplina: Estrutura de Dados II
Janeiro de 2022

Vídeo com revisão de MergeSort e com explicação do exercício no link https://www.youtube.com/watch?v=46a8LYuzQHE

Uma sequência é chamada de não monótona se cada (e toda) subsequência contígua contém ao menos um elemento único, ou seja, um elemento que seja diferente de todo outro elemento daquela subsequência. Dada uma sequência de inteiros, faça um programa que verifique se ela é monótona ou não.

Entrada
A primeira linha da entrada contém o número de casos de teste T. As descrições dos casos de teste seguem: Cada caso de teste começa com um inteiro n (1 ≤ n ≤ 200000) denotando o comprimento da sequência.
Na próxima linha seguem os n elementos da sequência, separados por espaços simples. Os elementos são inteiros não negativos menores que 10000000000.

Saída
Imprima as respostas dos casos de teste na ordem em que aparecem na entrada. Para cada caso de teste imprima uma única linha contendo 'não monótona' ou 'monótona'.
"""

def monotona(lista):
    tamanhodalista = len(lista)
    tamanho = 1
    while tamanho < tamanhodalista:
        for sequencia in range (0, tamanhodalista - (tamanho*2)):
            listateste1 = lista[ sequencia : sequencia + tamanho ]
            listateste2 = lista[ sequencia + tamanho : sequencia + tamanho + tamanho]
            if (set(listateste1) == set(listateste2)):
                return True
        tamanho += 1
    return False


tests = input()

for i in range(int(tests)):
    testlength = input()
    newlist = []
    element = input()
    newlist = element.split()
    if (monotona(newlist)):
        print("monótona")
    else:
        print("não monótona")
