def editapalavra(palavra):
    maiuscula = palavra.upper()
    return (maiuscula)

def listar(dicionario):
    lista = []
    for i in range(26):
        letra = chr(65 + i)
        saida = str(letra) + " " + str( dicionario[letra] )
        lista.append(saida)
    return (lista)

def peganumero(valor):
    return (int(valor[2:]))

n = input()
palavras = []
letras = {}

for i in range(26):
    letras[chr(65 + i)] = 0

for i in range(int(n)):
    palavra = input()
    editada = editapalavra(palavra)
    palavras.append(editada)

for palavra in palavras:
    for letra in palavra:
        if letra in letras:
            n = letras[letra] + 1
            letras.update({letra: n})


lista = listar(letras)
lista.sort(reverse=True,key=peganumero)

for p in lista:
    if peganumero(p) > 0:
        print(p)

