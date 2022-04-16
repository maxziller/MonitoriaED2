def ataque(entrada):
    valor = 1
    tamanho = len(entrada)
    for i in range(tamanho):
        valor *= i+1
    return valor

entrada = input()
entrada = input()
numero = int(entrada)

for i in range(numero):
    entrada = input()
    print ( ataque(entrada))
        
