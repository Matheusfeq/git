import os, time

#############################
#Cores
limpar = "\033[0m"
vermelho = "\033[38;5;203m"
azul = "\033[38;5;27m"
############################

aux = 0;
flag = True

jogador = 0 # 0 = X, 1 = O

jogo = [1,2,3,4,5,6,7,8,9]

def clear():
    ''' limpar o terminal '''
    os.system('cls')

clear()

def introducao():
    print("Bem vindo ao jogo da velha!")
    time.sleep(1)
    clear()

introducao()

def tabela():
    '''  '''
    print("{}Tabela{}:\n{} {} {}\n{} {} {}\n{} {} {}".format(vermelho, limpar, jogo[0],jogo[1],jogo[2],jogo[3],jogo[4],jogo[5],jogo[6],jogo[7],jogo[8]))

tabela()

def ganhou(win: str):
    print("\n{}{} ganhou!!!! ueba!\n".format(azul, win))

while flag == True:

    #Determina a jogada do jogador atual
    if jogador == 0:
        jogada = int(input("Escolha uma posição para marcar com {}: ".format("X")))
        jogo[jogada - 1] = "X"
        clear()
        tabela()
        jogador = 1
    elif jogador == 1:
        jogada = int(input("Escolha uma posição para marcar com {}: ".format("O")))
        jogo[jogada - 1] = "O"
        clear()
        tabela()
        jogador = 0

    #Verificar quem ganhou
    
    #horizontal - 1 linha
    if jogo[0] == jogo[1] and jogo[0] == jogo[2]:
        ganhou(jogo[1])
        flag = False
    #horizontal - 2 linha
    if jogo[3] == jogo[4] and jogo[3] == jogo[5]:
        ganhou(jogo[3])
        flag = False
    #horizontal - 3 linha
    if jogo[6] == jogo[7] and jogo[6] == jogo[8]:
        ganhou(jogo[6])
        flag = False

    #vertical - coluna 1
    if jogo[0] == jogo[3] and jogo[0] == jogo[6]:
       ganhou(jogo[0])
       flag = False
    #vertical - coluna 2
    if jogo[1] == jogo[4] and jogo[1] == jogo[7]:
        ganhou(jogo[1])
        flag = False
    #vertical - coluna 3
    if jogo[2] == jogo[5] and jogo[2] == jogo[8]:
        ganhou(jogo[2])
        flag = False
    
    #diagonal - top/bot
    if jogo[0] == jogo[4] and jogo[0] == jogo[8]:
        ganhou(jogo[0])
        flag = False

    #diagonal - bot/top
    if jogo[6] == jogo[4] and jogo[6] == jogo[2]:
        ganhou(jogo[6])
        flag = False
    
    aux += 1
    if(aux == 9 and flag == True):
        print("\n{}Velha!".format(azul))
        flag = False
    
    print(limpar)
        
    
    







