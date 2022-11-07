import alunos
import os
import csv
import matplotlib.pyplot as plt

myAlunos = alunos.readDataset("../TPC7/alunos.csv")

def menu():
    print('''
    [1] Lista Total de Alunos
    [2] Distribuição Dos Alunos Por Curso 
    [3] Acrescentar Média
    [4] Distribuição Dos Alunos Por Médias 
    [5] Acrescentar Escalões
    [6] Distribuição Dos Alunos Por Escalão
    [7] Distribuição Em Gráficos
    [0] Sair  
    ''')
    return 

opcao = - 1
os.system("cls")
while opcao != 0:
    menu()
    opcao = int(input(" Qual a opção que deseja selecionar? ")) 
    
    if opcao == 1:
        alunos.tabelarAlunos(myAlunos)

    elif opcao == 2:
        alunos.alunPorCurso(myAlunos)

    elif opcao == 3:
        print(" [ ERRO ] ")

    elif opcao == 4:
        alunos.mediaNotas(myAlunos)

    elif opcao == 5:
        print(" [ ERRO ] ")

    elif opcao == 6:
        alunos.alunPorEscalao(myAlunos)

    elif opcao == 7:
        alunos.desenhaGrafico(myAlunos)  
   
    else:
        print(" Opção inválida. Tente novamente. ")

os.system("cls")

print(" Fim do programa. Volte Sempre! ")  