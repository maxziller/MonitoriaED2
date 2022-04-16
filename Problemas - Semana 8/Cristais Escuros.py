casos = int(input())
for a in range(casos):
    n = int(input())
    lista = []
    for i in range(n):
        cristal = int(input())
        lista.append( cristal )
    maximo = 0
    for i in range(n-1):
        count = 1
        j = i+1
        while (j < n) and (lista[j] not in lista[i:j]):
            count += 1
            j += 1
        if (count > maximo):
            maximo = count
    if (n == 1):
        maximo = 1
    print(maximo)
