#/*******************************************************************************
#Autor: João Marcus Ribeiro da Silva
#Componente Curricular: MI-Algoritmos I
#Concluido em: 26/10/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/
#Sistema operacional utilizado= Windows / "os.system("cls")

#Bibliotecas utilizadas:
import random #biblioteca já é do python
import time #biblioteca já é do python
import os #biblioteca já é do python
import keyboard #Necessita de instalação, "pip install keyboard" (no terminal)
import numpy as np #Necessita de instalação, "pip install numpy" (no terminal)

# Função que imprime a o tabuleiro: 
def imprimirMatriz(tabuleiro,Pontuação,jogador):

    #Imprime o tabuleiro.
    for l in range(len(tabuleiro)):
        for c in range (len(tabuleiro[0])):
            print(tabuleiro[l][c], end="")
        print("")
    #Imprime a pontuação e o nome do jogador embaixo do tabuleiro.
    print(f"Pontuação: {Pontuação}\t{"Player:\033[037m"}{jogador}")

# Função que escolhe a peça no início do tabuleiro.
def escolherForma(formas):
    #Escolhe as peças aleatoriamente.
    Formato=random.choice(formas)
    return Formato
    #peca_I, peca_T, peca_J, peca_L, peca_O, peca_S, peca_Z,bomba

# Função que posiciona uma peça no tabuleiro.
def ColocarPeca(matriz, peca, coluna, nova_linha):

    #Verifica o formato da peca.
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            #Insere de acordo com o formato verificado.
            if peca[l][c] == "🟪":
                matriz[nova_linha+l][coluna+c]="🟪"
            if peca[l][c]=="💣":
               matriz[nova_linha+l][coluna+c]="💣" 
    
    return matriz,nova_linha

#Função de movimentação:
def movimentar(matriz,peca,coluna, nova_linha):

    #Se o usuário apertar a tecla "-->" (seta para direita).
    if keyboard.is_pressed("right"):
        # Verifica se pode mover para a direita.
        if Verificar(matriz,peca,coluna+1, nova_linha) and coluna<11-len(peca[0]):
            #Adiciona +1 na coluna movendo a peça para direita.
            coluna += 1

    #Se o usuário apertar a tecla "<--" (seta para esquerda).
    elif keyboard.is_pressed("left"):
        # Verifica se pode mover para a esquerda.
        if Verificar(matriz,peca,coluna-1, nova_linha) and coluna>1:
            #Subtrai -1 na coluna movendo a peça para esquerda.
            coluna -= 1
     
    return coluna

#Função de girar
def girar(matriz,peca,coluna, nova_linha):
    #Se o usuário apertar a tecla "^" (seta para cima).
    #                              |
    if keyboard.is_pressed("up"):

        #Gira a peça em 90° no sentido anti-horário. 
        giro_peca = np.rot90(peca, k=1, axes=(0,1))
        #Chama a função de verificação, para identificar se pode ou não girar a peça.
        if Verificar(matriz,giro_peca,coluna, nova_linha):
            #Atualiza a variável peça já girada
            peca=giro_peca
            return peca
        
    return peca

#Função de explosão da bomba:
def Bomba (matriz,peca,coluna,nova_linha,Pontuação,jogador):
    #Percorre pelo tamanho da bomba
    for i in range(len(peca)):
        for j in range (len(peca[0])):
            if peca[i][j]=="💣":
                for c in range(-1,2):
                    #Verifica o alcance da explosão, evitando passar do limite do tabuleiro
                    if matriz[nova_linha][coluna+c]!="💥" and matriz[nova_linha][coluna+c] !="|":
                        for l in range(-1,2):

                            if nova_linha!=0:
                                #Verifica se a posição da bomba está no limite de linhas do tabuleiro 
                                if nova_linha+1<len(matriz):
                                    matriz[nova_linha+l][coluna+c]="💥" #Substitui os valores
                            #Mini bloco que evita a explosão no início do tabuleiro, para que o alcance não chegue ao final 
                                elif l<1:
                                    matriz[nova_linha+l][coluna+c]="💥" #Substitui os valores
                            else:
                                if l>-1:
                                    matriz[nova_linha+l][coluna+c]="💥" #Substitui os valores
                #Mostra a área explodida da bomba       
                imprimirMatriz(matriz,Pontuação,jogador)
                time.sleep(0.2)
                os.system("cls")
                #Preenche todos os espaços explodidos pelo fundo do tabuleiro
                for l in range (len(matriz)):
                    for c in range(len(matriz[0])):
                        if matriz[l][c]=="💥":
                            matriz[l][c]="⬛"
                #Mostra a atualização do tabuleiro após a explosão               
                imprimirMatriz(matriz,Pontuação,jogador)
                time.sleep(0.2)
                os.system("cls")

#Função que verifica a maioria das interações entre as peças e o tabuleiro              
def Verificar(matriz,peca,coluna, nova_linha):
    
    for l in range(len(peca)):
        descer=True
        for c in range(len(peca[l])):
            if peca[l][c]!="⬛":
                #Verifica se é a última linha do tabuleiro
                if nova_linha+l+1>=len(matriz):
                    return False

                #Verifica se é a última linha da peca
                if l+1<len(peca):

                    #Verifica se abaixo da bloco preenchido tem outro bloco da própria peça
                    if peca[l+1][c]!="🟪":
                        #Se não houver bloco, a variável descer armazena o valor e aguarda a próxima verificação
                        descer=True
                    #Se houver, descer armazena False, e aguarda a próxima verificação    
                    else:
                        descer=False
                # Verifica se o bloco abaixo do observado abaixo não está preenchido
                if matriz[nova_linha + l + 1][coluna + c] !="⬛" and descer: 
                    return False
                
    return True

#Função de apagar peça na posição antiga
def Apagar(matriz,coluna,peca,nova_linha):
    #Verifica onde a peça não fixada está dentro do tabuleiro.
    for l in range(len(peca)):
        for c in range(len(peca[0])):
            #Após encontrar a peça, cada parte dela será substituída.
            if peca[l][c]!="⬛":
                matriz[nova_linha + l][coluna + c] = "⬛"

def gravidade(matriz,peca,coluna, nova_linha,Pontuação,jogador):
    #Esta função agrupa outras funções para simular a gravidade.
    nova_linha=0
    
    #Enquanto a verificação de colisão não for Falsa
    while Verificar(matriz,peca,coluna,nova_linha):
        
        #Chama a função que apaga peça.
        Apagar(matriz,coluna,peca,nova_linha)
        nova_linha += 1

        #Chama as funções responsáveis pelo giro e movimentação das peças.
        peca=girar(matriz,peca,coluna, nova_linha)        
        coluna=movimentar(matriz,peca,coluna, nova_linha)
        
    #Acelera a movimentação se o usuário apertar "seta |"
    #                                                  v

        #Chama funções responsáveis por inserir as peças e mostrar o tabuleiro.
        ColocarPeca(matriz,peca,coluna,nova_linha)   
        imprimirMatriz(matriz,Pontuação,jogador)
        #Retarda o tempo e apaga o terminal.
        tempo=Dificuldade(Pontuação)

        #Acelera a movimentação se o usuário apertar "seta |" (para baixo)
        #                                                  v
        if keyboard.is_pressed("down"):
            #Modifica o tempo conforme o tempo anterior.
            if tempo== 0.5:
                tempo= 0.1
            elif tempo == 0.4:
                tempo= 0.1
            elif tempo== 0.2:
                tempo= 0.08
            elif tempo<0.2:
                tempo=0
            time.sleep(tempo)
        #Se a tecla não for apertada o tempo continua sendo o mesmo
        else:
            time.sleep(tempo)
         
        os.system("cls")
    #Chama a função da explosão da bomba se a Verificação for Falsa, ela está no final pois só será acionada quando ela parar.         
    Bomba(matriz,peca,coluna,nova_linha,Pontuação,jogador)

#Função que apaga linha e insere linha e atribui pontuação do jogador     
def apagarLinha (matriz,Pontuação):
    remover_L=0
    Pontos=0
    #Verifica a matriz para achar as linhas completas
    for l in range (len(matriz)):
        linha=0
        for c in range(len(matriz[0])):
            if matriz[l][c]=="🟪":
                linha+=1
        #Apaga e insere nova(s) linha(s)
        if linha==10:    
            matriz.pop(l)
            matriz.insert(0,["|", "⬛", "⬛", "⬛","⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "|"])
            remover_L+=1

    #Pontuação de acordo com o número de linhas excluídas
    Pontos=(100*remover_L)
    #Pontos são dobrados se forem removidas mais de uma linha
    if remover_L>1:
        Pontuação+=Pontos*2
    else:
        Pontuação+=Pontos

    return Pontuação 

#Função que altera a dificuldade de acordo com os pontos do jogador
def Dificuldade(Pontuação):

    #Entre 200 e 500 pontos:
    if 200<=Pontuação<=500:
        tempo=0.4
    #Entre 600 e 800 pontos:
    elif 600<=Pontuação<=800:
        tempo=0.2
    #Com mais de 1000 pontos:
    elif Pontuação>=1000:
        tempo=0.05
    #Menos de 200:
    else:
        tempo=0.5

    return tempo

def InicioJogo(Título):

    #Laço que imprime o título (TETRIS)
    for l in Título:
        print(f"{l}\033[34m")
        time.sleep(0.5)
    print()
    #Informações do jogador e início de jogo
    jogador=input(f"Ｄｉｇｉｔｅ ｓｅｕ ｎｏｍｅ：")
    print(f"\t🇧 🇪 🇲 - 🇻 🇮 🇳 🇩 🇴 ! \n{"\t🇩 🇮 🇻 🇮 🇷 🇹 🇦 - 🇸 🇪 !"}\n{"\t\t⏳\033[037m"}",end="")
    time.sleep(3)
    os.system("cls")

    return jogador

def Tutorial(Título):
    #Imprime o título (TUTORIAL)
    for l in Título:
        print(f"{l}\033[34m")
    print()
    #Informações sobre os botões
    print("Ｐａｒａ ｊｏｇａｒ ｕｔｉｌｉｚｅ ａｓ ｓｅｇｕｉｎｔｅｓ ｔｅｃｌａｓ：\n")
    print(f"{"⬆️  - 𝙋𝙖𝙧𝙖 𝙜𝙞𝙧𝙖𝙧":>36}\n{"𝙋𝙖𝙧𝙖 𝙚𝙨𝙦𝙪𝙚𝙧𝙙𝙖 -  ⬅️  ⬇️  ➡️  - 𝙋𝙖𝙧𝙖 𝙙𝙞𝙧𝙚𝙞𝙩𝙖"}")
    print(f"{"|-𝙋𝙖𝙧𝙖 𝙖𝙘𝙚𝙡𝙚𝙧𝙖𝙧":>36}\n\n{"\033[37m★ Forme linhas horizontais para adquirir pontos"}\n{"★ Não deixe as peças tocarem o topo "}\n{"★ A dificuldade é aumentada junto com a pontuação"}\n\n")
    print("=-"*15,end="")
    print("ATENÇÃO",end="")
    print("=-"*15)
    print(f"{"A bomba |💣| destrói uma área de 3x3 blocos."}\n\n{"🇨 🇦 🇷 🇷 🇪 🇬 🇦 🇳 🇩 🇴 ⏳\033[37m"}")
    time.sleep(10)
    os.system("cls")
    
def FimDeJogo(Título,Pontuação,jogador):
    
    #Laço que imprime o título (GAME-OVER)
        for l in Título:
            print(f"{l}\033[34m")
            time.sleep(0.5)

        #Espécie de um cronômetro utilizando loop
        verif=True
        i=0
        while verif:
            if i>0:
                for l in Título:
                    print(f"{l}\033[34m")

            #Impressão dos pontos
            print(f"🇯 🇴 🇬 🇦 🇩 🇴 🇷: {jogador} {"\033[037m🇵 🇴 🇳 🇹 🇴 🇸  🇹 🇴 🇹 🇦 🇮 🇸 :":>10}{Pontuação} pontos.\n {"\033[034m 🇳 🇴 🇻 🇴  🇯 🇴 🇬 🇴: SEGURE Tecla (P)"}\t{"🇸 🇦 🇮 🇷: SEGURE Tecla (S)"}")
            i+=1
            #O jogador tem apenas 30 segundos para escolher.
            print(f"ESCOLHA ANTES QUE O CRONÔMETRO CHEGUE A 30s  -> |{i}| segundos\033[37m")
            time.sleep (1)
            os.system("cls")
            
            if i <30:
                #Comando para reiniciar
                if keyboard.is_pressed("p"):
                    os.system("cls")
                    time.sleep(3)
                    os.system("cls")
                    verif=False
                    Game=True
                    return Game
                
                #Comando para finalizar o jogo
                elif keyboard.is_pressed("s"):
                    print("!! 🇯 🇴 🇬 🇴  🇫 🇮 🇳 🇦 🇱 🇮 🇿 🇦 🇩 🇴 !!")
                    verif=False
                    Game=False
                    return Game
                #Se o jogador não escolher, o jogo termina
            else:
                print(" !! Ｊｏｇｏ ｆｉｎａｌｉｚａｄｏ, ｐｏｉｓ ｏ ｔｅｍｐｏ ａｃａｂｏｕ !!")
                verif=False
                Game=False
                return Game
    
#Função principal:
def main():
    #Títulos que serão impressos no início e fim de jogo
    T_Inicio=[" ▀▀█▀▀ █▀▀ ▀▀█▀▀ █▀▀█ ░▀░ █▀▀",
              " ░░█░░ █▀▀ ░░█░░ █▄▄▀ ▀█▀ ▀▀█",
              " ░░▀░░ ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀ ▀▀▀"]
    T_Tutorial= ["▀▀█▀▀ █░░█ ▀▀█▀▀ █▀▀█ █▀▀█ ░▀░ █▀▀█ █░░",
                 "░▒█░░ █░░█ ░░█░░ █░░█ █▄▄▀ ▀█▀ █▄▄█ █░░",
                 "░▒█░░ ░▀▀▀ ░░▀░░ ▀▀▀▀ ▀░▀▀ ▀▀▀ ▀░░▀ ▀▀▀"]
    T_Fim=["█▀▀█ █▀▀█ █▀▄▀█ █▀▀   █▀▀█ ▀█░█▀ █▀▀ █▀▀█",
         "█░▄▄ █▄▄█ █░▀░█ █▀▀   █░░█ ░█▄█░ █▀▀ █▄▄▀",
         "█▄▄█ ▀░░▀ ▀░░░▀ ▀▀▀   ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀"]
    
    #Bloco de peças do jogo:
    peca_I = [["🟪","🟪","🟪","🟪"]]
    peca_T = [["🟪","🟪","🟪"], ["⬛","🟪","⬛"]]
    peca_L = [["⬛","⬛","🟪"], ["🟪","🟪","🟪"]]
    peca_J = [["🟪","⬛","⬛"],["🟪","🟪","🟪"]]
    peca_O = [["🟪","🟪"], ["🟪","🟪"]]
    peca_S = [["⬛","🟪","🟪"], ["🟪","🟪","⬛"]]
    peca_Z = [["🟪","🟪","⬛"], ["⬛","🟪","🟪"]]
    bomba=[["💣"]]
    #Lista com todas as peças
    formas = [peca_I, peca_T, peca_J, peca_L, peca_O, peca_S, peca_Z,peca_I, peca_T, peca_J, peca_L, peca_O, peca_S, peca_Z,bomba]
    
    #Cria o tabuleiro vazio:
    matriz =[["|","⬛", "⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","|"]for l in range(20)]
    
    #Variáveis iniciadas:
    Game_Over=True
    Pontuação=0
    nova_linha=0

    #Exibe o início do jogo.
    jogador=InicioJogo(T_Inicio)
    #Exibe o tutorial
    Tutorial(T_Tutorial)

    #Laço principal:
    while Game_Over==True:
        #Atualiza o formato da peça.
        peca = escolherForma(formas)

        #Cria um limite máximo para a coluna de surgimento.
        limite=11-(len(peca[0]))
        #O surgimento da peça no início do tabuleiro é aleatório.
        coluna = random.randint(1,limite)

        #Chama a função para inserir a peça no tabuleiro.
        ColocarPeca(matriz, peca, coluna,nova_linha)
        #Chama a função para imprimir a matriz.
        imprimirMatriz(matriz,Pontuação,jogador)
        time.sleep(1)
        #Aapaga o terminal.
        os.system("cls")
        
        #Chama a função para simular a gravidade.
        gravidade(matriz, peca, coluna, nova_linha,Pontuação,jogador)

        #Chama a função, reservando o valor atualizado da pontuação.
        Pontuação=apagarLinha(matriz,Pontuação)

        #Verifica se alguma peça fixada encostou no topo do tabuleiro.
        for c in range(len(matriz[0])):
            if matriz[0][c]=="🟪":
                #Imprime e carrega.
                print(f"{"🇨 🇦 🇷 🇷 🇪 🇬 🇦 🇳 🇩 🇴 ⏳":>20}")
                time.sleep(3)
                os.system("cls")

                #Chama a função, reservando o valor retornado.
                Game_Over=FimDeJogo(T_Fim,Pontuação,jogador)

                #Atualiza tabuleiro por um vazio e zera os pontos.
                matriz =[["|", "⬛", "⬛", "⬛","⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "|"]for l in range(20)]
                Pontuação =0
if __name__=="__main__":
    main()                