import csv
import matplotlib.pyplot as plt

def readDataset(fnome):
    f = open(fnome)
    f.readline()
    csv_reader = csv.reader(f, delimiter=";")
    obras = []
    for row in csv_reader:
        obras.append(tuple(row))
    return obras

# def pp(obras): #exercicio da aula
   # print(f"{obras[0][:25]:25} | {obras[1][:30]:30} | {obras[4][:15]:15} | {obras[2][:6]:6}")

def contarObras(obras):
    return len(obras)

def listarObras(obras):
    print("\n","Título                         | Descrição                                          | Compositor                     | Ano de Criação ")
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    for titulo, desc, anoCriacao, _, compositor,*_ in obras:
        print(f" {titulo[0:30]:30} | {desc[0:50]:50} | {compositor[0:30]:30} | {anoCriacao:15}")
    return()

def ordTit(t):
    return t[0]

def titAno(obras):
    res = []
    for nome, _, ano, *_ in obras:
        res.append((nome, ano))
    res.sort(key=ordTit)
    print("\n"," Título                         | Ano de Criação ")
    print("-------------------------------------------------")
    for titulo, anoCriacao in res:
        print(f" {titulo[0:30]:30} | {anoCriacao:15}")
    return res

def titPorAno(obras):
    listarTitPorAno = []
    for titulo, _, anoCriacao, *_ in obras:
        listarTitPorAno.append((anoCriacao, titulo))
    listarTitPorAno.sort()
    print("\n"," Ano de Criação | Título                     ")
    print("-------------------------------------------------")
    for anoCriacao, titulo in listarTitPorAno:
        print(f" {anoCriacao:15} | {titulo[0:30]:30}")
    return ()

def dicionariotitPorAno(obras):
    res = {}
    for nome, _, anoCriacao, *_ in obras:
        if anoCriacao in res.keys():
            res[anoCriacao].append(nome)
        else:
            res[anoCriacao] = [nome]
    return res

def lCompositores(obras):
    listaCompositores = []
    for _, _, _, _, compositor, *_ in obras:
        if compositor not in listaCompositores:
            listaCompositores.append(compositor)
    listaCompositores.sort()
    print("\n"," Lista De Compositores          ")
    print("---------------------------------")
    for n in listaCompositores:
        print(" - ",n)
    return ()

def tabelaDistribuicao(distrib):
    print("")
    for par in distrib:
        print(f"{par[0:17]:25} | {distrib[par]}")
    print("")
    return()

def distObrasPeriodo(obras):
    dObrasPeriodo = {}
    for _, _ , _, periodo, *_ in obras:
        if periodo in dObrasPeriodo.keys():
            dObrasPeriodo[periodo] = dObrasPeriodo[periodo] + 1
        else:
            dObrasPeriodo[periodo] = 1
    return dObrasPeriodo

def distObrasAno(obras):
    dObrasAno = {}
    for _, _, anoCriacao, *_ in obras:
        if anoCriacao in dObrasAno.keys():
            dObrasAno[anoCriacao] = dObrasAno[anoCriacao] + 1
        else:
            dObrasAno[anoCriacao] = 1
    return dObrasAno

def distObrasCompositor(obras):
    dObrasCompositor = {}
    for _, _, _, _, compositor, *_ in obras:
        if compositor in dObrasCompositor.keys():
            dObrasCompositor[compositor] = dObrasCompositor[compositor] + 1
        else:
            dObrasCompositor[compositor] = 1
    return dObrasCompositor

def plotDistrib(distrib):
    plt.bar(distrib.keys(), distrib.values(), color = ['maroon'])
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation = 45)
    plt.title("Gráfico da Distribuição de Obras")
    plt.show()
    return

def desenhaGrafico(obras):
    opcao = int(input("""
Consultar o Gráfico de Distribuição Por:
[1] Período
[2] Ano
[3] Compositor
Opção: """))
    if opcao == 1:
        plotDistrib(distObrasPeriodo(obras))
    elif opcao == 2:
        plotDistrib(distObrasAno(obras))
    elif opcao == 3:
        plotDistrib(distObrasCompositor(obras))

def tuploCompObras(obras):
    return list(inversEstrut(obras).items())

def inversEstrut(obras):
    disObrCompAux = {}
    for titulo, _, _, _, compositor, *_ in obras:
        if compositor in disObrCompAux.keys():
            disObrCompAux[compositor].append(titulo)
        else:
            disObrCompAux[compositor] = [titulo]
    return disObrCompAux

def compObras(obras):
    print("")
    comp = str(input(" Inserir nome do Compositor: "))
    tuploAux = tuploCompObras(obras)
    for compositor, listarObras in tuploAux:
        if str(comp) == str(compositor):
            print("Obras compostas por ", comp, ": ","\n")
            print(listarObras)
            print("")