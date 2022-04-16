while(1):
    entrada = input()
    n = int(entrada)
    alunos = []
    grades = []
    maior = 0
    quantidade = 0
    if (n == 0):
        break
    for i in range(n):
        entrada = input()
        aluno = entrada.split(" ")
        aluno = filter(None, aluno)
        grade = set(aluno)
        if (grade not in grades):
            grades.append(grade)
            alunos.append(1)
        else:
            posicao = grades.index(grade)
            alunos[posicao] += 1
    for aluno in alunos:
        if (maior < aluno):
            maior = aluno
    for aluno in alunos:
        if (aluno == maior):
            quantidade += aluno
    print(quantidade)
        
