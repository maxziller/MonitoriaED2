def paridade(numero):
    if (numero%2 > 0):
        return False
    else:
        return True

def antes(numero1,numero2,modulo):
    if (numero1 > 0):
        modulo1 = numero1 % modulo
    else:
        modulo1 = (-1) * (numero1 % modulo)
    if (numero2 > 0):
        modulo2 = numero2 % modulo
    else:
        modulo2 = (-1) * (numero2 % modulo)

    if modulo1 < modulo2:
        return True
    elif modulo1 > modulo2:
        return False
    else:
        paridade1 = paridade(numero1)
        paridade2 = paridade(numero2)
        if paridade1 != paridade2:
            if (paridade1):
                return False
            else:
                return True
        else:
            if (paridade1):
                if (numero1 > numero2):
                    return False
                else:
                    return True
            else:
                if (numero1 > numero2):
                    return True
                else:
                    return False

def merge(lista, m):

    fim = len(lista)-1
    if (fim < 1):
        return lista
    else:
        meio = len(lista)//2
        esquerda = lista[:meio]
        direita = lista[meio:]

        esquerda = merge(esquerda,m)
        direita = merge(direita,m)

        novalista=[]
        

        while len(esquerda) > 0 and len(direita) > 0:
            if antes(esquerda[0],direita[0],m):
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

for i in range(20):
    entrada = input()
    valorentrada = entrada.split(" ")
    n = int(valorentrada[0])
    m = int(valorentrada[1])
    lista = []

    for i in range(n):
        lista.append( int( input() ) )

    novalista = merge(lista,m)

    print(entrada)

    for i in novalista:
        print(i)

pararentrada = input()
print(pararentrada)
