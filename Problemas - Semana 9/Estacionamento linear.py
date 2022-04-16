def valores(placa):
    caracteres = list(placa)
    e1 = 0
    e2 = 0
    for i in range(len(caracteres)):
        e1 += ord(caracteres[i]) ** 2
        if (i+1 < len(caracteres)):
            e2 += (ord(caracteres[i]) + ord(caracteres[i+1])) ** 2
    valor = e1 + e2
    return valor

def menorvaga(placas):
    contador = len(placas)
    while (contador <= 1000):
        vagas = []
        for placa in placas:
            vaga = valores(placa) % contador
            if (vaga not in vagas):
                vagas.append(vaga)
            else:
                break
        if ( len(vagas) == len(placas) ):
            return contador
        else:
            contador += 1
    return ( -1 )


placas = []
placa = input()
placa = placa.strip()
while (placa != ""):
    placas.append(placa)
    placa = input()
    placa = placa.strip()
print( menorvaga(placas))

