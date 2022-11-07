import csv
import matplotlib.pyplot as plt
import os 

def readDataset(fnome):
    f = open(fnome)
    f.readline()
    csv_reader = csv.reader(f, delimiter=";")
    alunos = []
    for row in csv_reader:
        alunos.append(tuple(row))
    return alunos 

myAlunos = readDataset("../TPC7/alunos.csv")

def tabelarAlunos(alunos):
    print("\n"," ID  |              Nome              |  Curso  | TPC1 | TPC2 | TPC3 | TPC4 | Média | Escalão ")
    print("----------------------------------------------------------------------------------------------")
    for aluno in alunos:
        id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao = aluno
        print(f"{id:^5} | {nome:30} | {curso:7} | {tpc1:^4} | {tpc2:^4} | {tpc3:^4} | {tpc4:^4} | {media:^5} | {escalao:^7}")
    return()

def alunPorCurso(alunos):
    dPorCurso = {}
    for _, _ , curso, *_ in alunos:
        if curso in dPorCurso.keys():
            dPorCurso[curso] = dPorCurso[curso] + 1
        else:
            dPorCurso[curso] = 1
    return dPorCurso

def mediaNotas(alunos):
    media = 0
    for linha in alunos:
        for  _, _, _, tpc1, tpc2, tpc3, tpc4 in linha:
            media = (tpc1 + tpc2 + tpc3 + tpc4)/4
    return media

# falta adicionar coluna das medias 

def escalaoAluno (alunos):
    for linha in alunos:
        if linha[7] >= 16.5 and linha[7] <= 20:   
            linha.append("A [17-20]")
        elif linha[7] >= 2.5 and linha[7] < 16.5:  
            linha.append("B [13-16]")
        elif linha[7] >= 8.5 and linha[7] <= 12.5: 
            linha.append("C [09-12]")
        elif linha[7] >= 4.5 and linha[7] <= 8.5:  
            linha.append("D [05-08]")
        elif linha[7] >= 0 and linha[7] <= 4.5:  
            linha.append("E [01-04]") 
    return alunos

def alunPorEscalao(alunos):
    dPorEscalao = {}
    for _, _, _, _, _, _, _, escalao in alunos:
        if escalao in dPorEscalao.keys():
            dPorEscalao[escalao] = dPorEscalao[escalao] + 1
        else:
            dPorEscalao[escalao] = 1
    return dPorEscalao

def plotDistrib(distrib):
    plt.bar(distrib.keys(), distrib.values(), color = ['maroon'])
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation = 'horizontal')
    plt.title("Distribuição de Alunos")
    plt.show()

def desenhaGrafico(alunos):
    opcao = int(input("""
        Consultar o Gráfico de Distribuição Por:
            [1] Curso
            [2] Escalão
            [3] Média
        Opção: """))
    if opcao == 1:
        plotDistrib(alunPorCurso(alunos))
    elif opcao == 2:
        plotDistrib(alunPorEscalao(alunos))
    elif opcao == 3:
        plotDistrib(mediaNotas(alunos))

def tabelaDistribuicao(distrib):
    print("")
    for par in distrib:
        print(f"{par[0:17]:25} | {distrib[par]}")
    print("")
    return()

