def bubblesort(numeros):
    
    lista = []
    
    for i in numeros:
        numero = int(i)
        lista.append( numero )
        
    tamanho = len(lista)
    contadordetrocas = 0
    jaarrumados = 0

    for i in range(tamanho-1):
        for j in range (tamanho - 1 - i):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
                contadordetrocas += 1
                
    return contadordetrocas

q = input()
numero = int(q)
if numero > 0:
    for i in range ( numero ):
        n = input()
        lista = input()
        lista2 = lista.strip()
        novalista = lista2.split(" ")
        if (len(novalista) > 1):
            x = bubblesort(novalista)
        else:
            x = 0
        print("A quantidade ajeitamentos deve ser "+str(x)+".")
else:
    print("A quantidade ajeitamentos deve ser 0.")

        
