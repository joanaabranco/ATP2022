# --------------------------------------- #
#   Modelo:                               #
#   Cinema = [Sala]                       # 
#   Sala = (nlugares, Vendidos, filme)    #
#   nlugares = Int                        #
#   filme = String                        #
#   Vendidos = [Int]                      #
# --------------------------------------- #

# menu
def menu():
    print(''' Bem vindo! 
    [1] Ver Filmes em Exibição
    [2] Testar Disponibilidade
    [3] Comprar Bilhete
    [4] Ver Lugares Disponíveis
    [5] Adicionar Sala de Cinema
    [6] Adicionar Filme
    [0] Sair 
    ''')

# listar(cinema)
def listar(cinema):
    print("Sala      Filmes")
    print("----------------")
    for p in cinema:
        nLugares, vendidos, filme = p
        print(sala, filme)

# disponivel(cinema)
def disponivel(cinema):
    res = True
    for p in cinema:
        nLugares, vendidos, filmes = p
        if nomep == nome:
            if lugar in ocupados:
                res = False
    return res
    return 

# venderBilhete(cinema, filme, lugar)
def venderBilhete(cinema, filme, lugar):
    
    return 

# listarDisponibilidades(cinema)
def listarDisponibilidade(cinema):

    return 

# inserirSala(cinema, sala)
def inserirSala(cinema, sala):
    cinema.append(sala)
    return cinema

# inserirFilme(cinema, filme)
def inserirFilme(cinema, filme):
    cinema.append(filme)
    return cinema


#
#
#
#
#

cinema = []
opcao = 1
while opcao != '0':
    menu()
    opcao = input(" Qual a opção que deseja selecionar? ")
    if opcao == '1':
        print(listar(cinema))
        menu()
    
    #elif opcao == '2':
        

    #elif opcao == '3':
        
    
    #elif opcao == '4':
        

    #elif opcao == '5':
       

    #elif opcao == '6':
        
    
    #elif opcao == '7':
        

    #elif opcao == '8':
       
    
    #elif opcao == '9'':
      
    elif opcao == '0':
        print(" Fim do programa. Volte Sempre! ")

    else:
        print(" Opção inválida. Tente novamente. ")
        menu()

sala1 = (150, [], "Twilight")
sala2 = (200, [], "Hannibal")
cinema1 = []