"""
Este é o documento com uma proposta de solução do problema Diretora Gringa. A solução para o problema é feita para fins didáticos.
Monitor autor: Max Pereira Ziller
Disciplina: Estrutura de Dados II
Janeiro de 2022

DIRETORA GRINGA

A diretora da escola onde você trabalha resolveu se aposentar para viver uma vida de natureza numa cabana isolada nas montanhas dos Andes. A nova diretora contratada é linha dura e quer repaginar toda a escola. Ela veio do exterior, de um país com tradição muito forte e quer que até os menores detalhes sejam refeitos de acordo com o gosto dela. Você foi encarregado por reorganizar todas as listas de chamada da escola, pois em seu país o sobrenome é mais importante que o primeiro nome.

Você quer manter seu emprego nesta escola, então precisa obedecer o que a nova diretora pediu. Todas as listas da escola estão organizadas em ordem alfabética do primeiro nome e você precisa reordená-las. Todos os alunos devem ficar em ordem alfabética pelo último sobrenome. No caso de estudantes com o mesmo sobrenome, a nova diretora tem outra exigência estranha: ela quer que os nomes fiquem organizados inversamente à ordem alfabética.

Entrada
Na primeira linha tem o número de alunos que estão na lista para serem organizados.

Cada linha seguinte contém uma string contendo o nome de um aluno.

Você pode assumir que a string com o nome dos estudantes não tem mais que 100 caracteres. Também pode assumir que os nomes já estejam ordenados em ordem alfabética.

Saída
Para cada linha, o seu programa deve retornar uma string com o nome do estudante na ordem solicitada pela diretora.

Ou seja, os nomes devem estar ordenados pela ordem alfabética do seu último nome. No caso de alunos com o mesmo sobrenome, eles devem ser ordenados entre si na ordem inversa à alfabética.
"""

import os

#Função Sobrenome recebe o nome completo e retorna apenas o último sobrenome
def sobrenome(nome):
    espaco = nome.rfind(" ") + 1
    ultimonome = nome[espaco:]
    return ultimonome

#Função Ordenar ordena a lista.
#Primeiro, ordena-se os nomes em ordem alfabética pelo método SelectionSort, uma vez que as pessoas de mesmo sobrenome devem estar em ordem alfabética inversa
#Depois, ordena-se os sobrenomes em ordem alfabética pelo método InsertionSort. SelectionSort não poderia ser usado novamente, pois não é um método estável.
def ordenar(alunos):
    #variável ordenado aponta até onde na lista já 
    ordenado = 0
    tamanho = len(alunos)
    lista = alunos.copy()


    #Loop de ordenação por nome. Em cada interação do loop é selecionado o menor elemento de toda a lista, o qual troca de posição com o primeiro elemento
    #não ordenado. É usado o método SelectionSort
    while ordenado < tamanho:
        #variável menor é um registrador da posição do menor elemento da lista
        menor = ordenado
        #variável contador vai percorrer toda a lista. Ela começa do elemento seguinte ao registro da variável ordenado pois ela marca, no momento, o primeiro
        #elemento da lista ainda não ordenado e não e necessário comparar o elemento consigo mesmo
        contador = ordenado + 1
        while contador < tamanho:
            if ( lista[menor] >= lista[contador] ):
                menor = contador
            contador += 1

        #Realiza a troca da posição dos dois elementos
        temporario = lista[ordenado]
        lista[ordenado] = lista[menor]
        lista[menor] = temporario
        
        ordenado += 1

    
    ordenado = 1
    #Loop de ordenação por nome. Em cada interação do loop, um elemento é reinserido à lista na posição ordenada.
    #É usado o método InsertionSort
    while ordenado < tamanho:
        contador = 0
        while (sobrenome(lista[contador]) < sobrenome(lista[ordenado])) and (contador < ordenado):
            contador += 1
        if contador != ordenado:
            valor = lista.pop(ordenado)
            lista.insert(contador, valor)
        ordenado += 1
    

    return lista

path = "C:/Users/Dell/Documents/Monitoria/Listas para testes"
for file in os.listdir(path):
    documento = []
    with open("Listas para testes/" + file, encoding='UTF-8') as arquivo:
        for line in arquivo:
            documento.append(line.rstrip())
    nomearquivoresposta = str(file)[0:-4] + "- resposta.txt"
    print(file)

    n = documento[0]
    #n = input()
    alunos = []

    contador = 0
    while contador < int(n):
        nome = documento[contador + 1]
        #nome = input()
        alunos.append(nome)
        contador += 1
    alunos = ordenar (alunos)

    f = open(nomearquivoresposta,"x")
    for a in alunos:
        print(a)
        f.write(a + "\n")
    f.close()
        
        

    
