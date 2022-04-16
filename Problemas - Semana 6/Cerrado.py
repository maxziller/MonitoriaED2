
def imprimirrelatorio(arvores, total):
    relatorio = list(arvores.keys())
    relatorio.sort()
    for a in relatorio:
        porcentagem = round( (arvores[a] / float(total))*100 , 4)
        percent = str(porcentagem)
        print(a + " " + percent)
    return None



n = int(input())
input()

try:
    for i in range(n):
        arvores = {}
        total = 0
        arvore = input().strip()
        while( arvore != "" and arvore != " " and arvore != "\n"):
            if arvore in arvores:
                x = arvores[arvore] + 1
                arvores.update({arvore: x})
            else:
                arvores[arvore] = 1
            total += 1
            arvore = input()
        imprimirrelatorio(arvores, total)
        print("")
        
except EOFError:
    imprimirrelatorio(arvores, total)
