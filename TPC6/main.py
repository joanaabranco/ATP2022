import obras

myObras = obras.readDataset("../Aula P6/obras.csv")

def menu():
    print('''
    (1) Número Total De Obras
    (2) Listar Base de Dados
    (3) Obras Ordenadas Por Título
    (4) Obras Ordenadas Por Ano
    (5) Lista Ordenada De Compositores
    (6) Distribuição das Obras Por Período
    (7) Distribuição das Obras Por Ano
    (8) Distribuição das Obras Por Compositor
    (9) Ver Gráficos
    (10) Ver Compositores E Respetivas Obras
    (0) Sair
    ''')

opcao = 1
while menu != 0:
    menu()
    opcao = input(" Introduza uma opção: ")
    if menu == 1:
        contagem = obras.contarObras(myObras)
        print(" O número total de obras na base de dados é ", contagem,".")

    elif menu == 2:
        listar = obras.listarObras(myObras)
        print(listar)
    
    elif menu == 3:
        titulos = obras.titAno(myObras)
        print(titulos)

    elif menu == 4:
        anos = obras.titPorAno(myObras)
        print(anos)
        
    elif menu == 5:
        compositores = obras.lCompositores(myObras)
        print(compositores)

    elif menu == 6:
        obras.tabelaDistribuiçao(obras.distObrasPeriodo(myObras))   

    elif menu == 7:
        obras.tabelaDistribuiçao(obras.distObrasAno(myObras)) 

    elif menu == 8:
        obras.tabelaDistribuiçao(obras.distObrasCompositor(myObras))   

    elif menu == 9:
        obras.desenhaGrafico(myObras)

    elif menu == 10:
        obras.compObras(myObras)

    else: 
        print(" Opção Inválida. Tente Novamente.")

print(" Fim. Obrigada!" )