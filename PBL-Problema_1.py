#/*******************************************************************************
#Autor: João Marcus Ribeiro da Silva
#Componente Curricular: MI-Algoritmos I
#Concluido em: 27/08/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

#Variáveis utilizadas:
#P_facil = 0
#P_media = 0
#P_dificil = 0
#equipe = " "
#num_faceis = 0
#num_medias = 0
#num_dificeis = 0
#minuto = 0
#min = 0
#Minutos = 0
#resto = 0
#s = 0
#segundos = 0
#Tmp_equipe_1 = 0
#Tmp_equipe_2 = 0
#Tmp_equipe_3 = 0
#Tmp_equipe_4 = 0
#Tmp_equipe_5 = 0
#Dificil_1 = 0
#Dificil_2 = 0
#Dificil_3 = 0
#Dificil_4 = 0
#Dificil_5 = 0
#equipe_1 = 0
#equipe_2 = 0
#equipe_3 = 0
#equipe_4 = 0
#equipe_5 = 0
#Pontuacao_1 = 0
#Pontuacao_2 = 0
#Pontuacao_3 = 0
#Pontuacao_4 = 0
#Pontuacao_5 = 0
#Média_Total = 0
#Eq_Dificil = " "
#Eq_Dificil = 0
#Valor_primeiro = Pontuacao_1   
#Valor_segundo = Pontuacao_2
#Valor_terceiro = Pontuacao_3
#Valor_quarto = Pontuacao_4
#Valor_quinta = Pontuacao_5  
#Posicao_1 = " "
#Posicao_2= " "
#Posicao_3 = " "
#Posicao_4 = " "
#Posicao_5 = " "
#P_Tempo= " "
#S_Tempo= " "
#T_Tempo= " "
#Q_Tempo= " "
#Qui_Tempo= " "
#D_primeiro= " "
#D_segundo= " "
#D_terceiro= " "
#D_quarto= " "
#D_quinto= " "

#Bloco para informações do valor do peso dos problemas.
print(f"\033[34m°Bem-vindo, informe o peso das dificuldades!")
print(f"\033[37m_"*100)
P_facil=int(input("Digite o peso dos problemas fáceis: "))
P_media=int(input("Digite o peso dos problemas médias: "))
P_dificil=int(input("Digite o peso dos problemas difíceis: "))
print(f"_"*100)
#Utilizando laço de repetição para a entrada de informações do código, O usuário irá informar o nome das equipes e a quantidade de cada problema.
for i in range(1,6):
    #Nome das equipes.
    print(f"\033[34m°Nome da {i}º equipe!")
    equipe=(input(f"\033[37m Digite o nome da {i}º equipe: "))
    print(f"_"*100)

#Bloco utilizado para coletar informações da quantidade de acertos.
    print(f"\033[34m°Quantidade de Resoluções!")
    num_faceis=int(input(f"\033[37mInforme quantas resoluções a {i}º equipe conseguiu nos problemas fáceis: "))
    num_medias=int(input(f"Informe quantas resoluções a {i}º equipe conseguiu nos problemas médias: "))
    num_dificeis=int(input(f"Informe quantas resoluções a {i}º equipe conseguiu nos problemas difíceis: "))
    print(f"_"*100)

#Bloco utilizado para coletar informações do TEMPO.
    print(f"\033[34m°Tempo da {i}º equipe!")
    minuto=int(input(f"\033[37mInforme em quantos minutos a {i}º equipe  levou (SEM OS SEGUNDOS): "))
    s=int(input(f"Informe em quantos segundos a {i}º equipe  levou: ")) 
    print(f"_"*100)

    #Calculo do tempo em minutos
    segundos = s % 60
    min = 0
    resto = s-segundos
    if resto>= 60:
        min+=1
        resto = segundos
    else:
        min=0
    Minutos = minuto+min
    tempo = (Minutos*60) + segundos
    
#A cada nome de equipe e tempo informado acima, as variáveis serão substituidos para as próximas impressões.    

    #Pontuação Equipe 01.
    if i==1:
        # O "i" é atualizado, assim as variáveis acima são substituidas pelas de baixo.
        Pontuacao_1 = ((P_facil *num_faceis) + (P_media * num_medias) + (P_dificil * num_dificeis))
        Dificil_1=num_dificeis
        Tmp_equipe_1= tempo
        equipe_1 = equipe
        Minutos1=Minutos
        segundos1=segundos

    #Pontuação Equipe 02.
    elif i==2:
        Pontuacao_2 = ((P_facil *num_faceis) + (P_media * num_medias) + (P_dificil * num_dificeis))
        Dificil_2=num_dificeis
        Tmp_equipe_2= tempo
        equipe_2 = equipe 
        Minutos2=Minutos
        segundos2=segundos

    #Pontuação Equipe 03.
    elif i==3:
        Pontuacao_3 = ((P_facil *num_faceis) + (P_media * num_medias) + (P_dificil * num_dificeis))
        Dificil_3=num_dificeis
        Tmp_equipe_3= tempo
        equipe_3 = equipe
        Minutos3=Minutos
        segundos3=segundos

    #Pontuação Equipe 04.
    elif i==4:
        Pontuacao_4 = ((P_facil *num_faceis) + (P_media * num_medias) + (P_dificil * num_dificeis))
        Dificil_4=num_dificeis
        Tmp_equipe_4= tempo
        equipe_4 = equipe
        Minutos4=Minutos
        segundos4=segundos

    #Pontuação Equipe 05.
    elif i==5:
        Pontuacao_5 = ((P_facil *num_faceis) + (P_media * num_medias) + (P_dificil * num_dificeis))
        Dificil_5=num_dificeis
        Tmp_equipe_5= tempo
        equipe_5 = equipe
        Minutos5=Minutos
        segundos5=segundos

#Bloco de variáveis atribuidas para atualizar valores e suas posições posteriormente.   
Valor_primeiro = Pontuacao_1   
Valor_segundo = Pontuacao_2
Valor_terceiro = Pontuacao_3
Valor_quarto = Pontuacao_4
Valor_quinta = Pontuacao_5  

Posicao_1 = equipe_1
Posicao_2= equipe_2
Posicao_3 = equipe_3
Posicao_4 = equipe_4
Posicao_5 = equipe_5

P_Tempo=Tmp_equipe_1
S_Tempo= Tmp_equipe_2
T_Tempo = Tmp_equipe_3
Q_Tempo = Tmp_equipe_4
Qui_Tempo = Tmp_equipe_5

D_primeiro=Dificil_1
D_segundo=Dificil_2
D_terceiro=Dificil_3
D_quarto=Dificil_4
D_quinto=Dificil_5

#Bloco que atualiza a posição "1º, 2º, 3º, 4º e 5º" do Ranking das Equipes.
for _ in range(0,5):
    #Primeiro Lugar
    if Valor_primeiro < Valor_segundo or Valor_primeiro == Valor_segundo and D_primeiro < D_segundo or D_primeiro == D_segundo and P_Tempo > S_Tempo:
        Valor_primeiro, Valor_segundo = Valor_segundo, Valor_primeiro
        D_primeiro, D_segundo = D_segundo, D_primeiro
        P_Tempo, S_Tempo = S_Tempo, P_Tempo
        Posicao_1, Posicao_2 = Posicao_2, Posicao_1

    if Valor_primeiro < Valor_terceiro or Valor_primeiro == Valor_terceiro and D_primeiro < D_terceiro or D_primeiro == D_terceiro and P_Tempo > T_Tempo:
        Valor_primeiro, Valor_terceiro = Valor_terceiro, Valor_primeiro
        D_primeiro, D_terceiro = D_terceiro, D_primeiro
        P_Tempo, T_Tempo = T_Tempo, P_Tempo
        Posicao_1, Posicao_3 = Posicao_3, Posicao_1

    if Valor_primeiro < Valor_quarto or Valor_primeiro == Valor_quarto and D_primeiro < D_quarto or D_primeiro == D_quarto and P_Tempo > Q_Tempo:
        Valor_primeiro, Valor_quarto = Valor_quarto, Valor_primeiro
        D_primeiro, D_quarto = D_quarto, D_primeiro
        P_Tempo, Q_Tempo = Q_Tempo, P_Tempo
        Posicao_1, Posicao_4 = Posicao_4, Posicao_1

    if Valor_primeiro < Valor_quinta or Valor_primeiro == Valor_quinta and D_primeiro < D_quinto or D_primeiro == D_quinto and P_Tempo > Qui_Tempo:
        Valor_primeiro, Valor_quinta = Valor_quinta, Valor_primeiro
        D_primeiro, D_quinto = D_quinto, D_primeiro
        P_Tempo, Qui_Tempo = Qui_Tempo, P_Tempo
        Posicao_1, Posicao_5 = Posicao_5, Posicao_1
    #Segundo Lugar
    if Valor_segundo > Valor_primeiro or Valor_segundo == Valor_primeiro and D_segundo < D_primeiro or D_segundo == D_primeiro and S_Tempo < P_Tempo:
        Valor_segundo, Valor_primeiro = Valor_primeiro, Valor_segundo
        D_segundo, D_primeiro = D_primeiro, D_segundo
        S_Tempo, P_Tempo = P_Tempo, S_Tempo 
        Posicao_2, Posicao_1 = Posicao_1, Posicao_2

    if Valor_segundo < Valor_terceiro or Valor_segundo == Valor_terceiro and D_segundo < D_terceiro or D_segundo == D_terceiro and S_Tempo > T_Tempo:
        Valor_segundo, Valor_terceiro = Valor_terceiro, Valor_segundo
        D_segundo, D_terceiro = D_terceiro, D_segundo
        S_Tempo, T_Tempo = T_Tempo, S_Tempo
        Posicao_2, Posicao_3 = Posicao_3, Posicao_2

    if Valor_segundo < Valor_quarto or Valor_segundo == Valor_quarto and D_segundo < D_quarto or D_segundo == D_quarto and S_Tempo > Q_Tempo:
        Valor_segundo, Valor_quarto = Valor_quarto, Valor_segundo
        D_segundo, D_quarto = D_quarto, D_segundo
        S_Tempo, Q_Tempo = Q_Tempo, S_Tempo
        Posicao_2, Posicao_4 = Posicao_4, Posicao_2

    if Valor_segundo < Valor_quinta or Valor_segundo == Valor_quinta and D_segundo < D_quinto or D_segundo == D_quinto and S_Tempo > Qui_Tempo:
        Valor_segundo, Valor_quinta = Valor_quinta, Valor_segundo
        D_segundo, D_quinto = D_quinto, D_segundo
        S_Tempo, Qui_Tempo = Qui_Tempo, S_Tempo
        Posicao_2, Posicao_5 = Posicao_5, Posicao_2

    #Terceiro Lugar
    if Valor_terceiro > Valor_primeiro or Valor_terceiro == Valor_primeiro and D_terceiro < D_primeiro or D_terceiro == D_primeiro and T_Tempo < P_Tempo:
        Valor_terceiro, Valor_primeiro = Valor_primeiro, Valor_terceiro
        D_terceiro, D_primeiro = D_primeiro, D_terceiro
        T_Tempo, P_Tempo = P_Tempo, T_Tempo
        Posicao_3, Posicao_1 = Posicao_1, Posicao_3

    if Valor_terceiro > Valor_segundo or Valor_terceiro == Valor_segundo and D_terceiro < D_segundo or D_terceiro == D_segundo and T_Tempo < S_Tempo:
        Valor_terceiro, Valor_segundo = Valor_segundo, Valor_terceiro
        D_terceiro, D_segundo = D_segundo, D_terceiro
        T_Tempo, S_Tempo = S_Tempo, T_Tempo
        Posicao_3, Posicao_2 = Posicao_2, Posicao_3

    if Valor_terceiro < Valor_quarto or Valor_terceiro == Valor_quarto and D_terceiro < D_quarto or D_terceiro == D_quarto and T_Tempo > Q_Tempo:
        Valor_terceiro, Valor_quarto = Valor_quarto, Valor_terceiro
        D_terceiro, D_quarto = D_quarto, D_terceiro
        T_Tempo, Q_Tempo = Q_Tempo, T_Tempo
        Posicao_3, Posicao_4 = Posicao_4, Posicao_3

    if Valor_terceiro < Valor_quinta or Valor_terceiro == Valor_quinta and D_terceiro < D_quinto or D_terceiro == D_quinto and T_Tempo > Qui_Tempo:
        Valor_terceiro, Valor_quinta = Valor_quinta, Valor_terceiro
        D_terceiro, D_quinto = D_quinto, D_terceiro
        T_Tempo, Qui_Tempo = Qui_Tempo, T_Tempo
        Posicao_3, Posicao_5 = Posicao_5, Posicao_3

    #Quarto Lugar
    if Valor_quarto > Valor_primeiro or Valor_quarto == Valor_primeiro and D_quarto < D_primeiro or D_quarto == D_primeiro and Q_Tempo < P_Tempo:
        Valor_quinta, Valor_primeiro = Valor_primeiro, Valor_quinta
        D_quarto, D_primeiro = D_primeiro, D_quarto
        Q_Tempo, P_Tempo = P_Tempo, Q_Tempo
        Posicao_4, Posicao_1 = Posicao_1, Posicao_4

    if Valor_quarto > Valor_segundo or Valor_quarto == Valor_segundo and D_quarto < D_segundo or D_quarto == D_segundo and Q_Tempo < S_Tempo:
        Valor_quarto, Valor_segundo = Valor_segundo, Valor_quarto
        D_quarto, D_segundo = D_segundo, D_quarto
        Q_Tempo, S_Tempo = S_Tempo, Q_Tempo
        Posicao_4, Posicao_2 = Posicao_2, Posicao_4

    if Valor_quarto > Valor_terceiro or Valor_quarto == Valor_terceiro and D_quarto < D_terceiro or D_quarto == D_terceiro and Q_Tempo < T_Tempo:
        Valor_quarto, Valor_terceiro = Valor_terceiro, Valor_quarto
        D_quarto, D_terceiro = D_terceiro, D_quarto
        Q_Tempo, T_Tempo = T_Tempo, Q_Tempo
        Posicao_4, Posicao_3 = Posicao_3, Posicao_4

    if Valor_quarto < Valor_quinta or Valor_quarto == Valor_quinta and D_quarto < D_quinto or D_quarto == D_quinto and Q_Tempo > Qui_Tempo:
        Valor_quarto, Valor_quinta = Valor_quinta, Valor_quarto
        D_quarto, D_quinto = D_quinto, D_quarto
        Q_Tempo, Qui_Tempo = Qui_Tempo, Q_Tempo
        Posicao_4, Posicao_5 = Posicao_5, Posicao_4
    #Quinto Lugar
    if Valor_quinta > Valor_primeiro or Valor_quinta == Valor_primeiro and D_quinto < D_primeiro or D_quinto == D_primeiro and Qui_Tempo < P_Tempo:
        Valor_quinta, Valor_primeiro = Valor_primeiro, Valor_quinta
        D_quinto, D_primeiro = D_primeiro, D_quinto
        Qui_Tempo, P_Tempo = P_Tempo, Qui_Tempo
        Posicao_5, Posicao_1 = Posicao_1, Posicao_5

    if Valor_quinta > Valor_segundo or Valor_quinta == Valor_segundo and D_quinto < D_segundo or D_quinto == D_segundo and Qui_Tempo < S_Tempo:
        Valor_quinta, Valor_segundo = Valor_segundo, Valor_quinta
        D_quinto, D_segundo = D_segundo, D_quinto
        Qui_Tempo, S_Tempo = S_Tempo, Qui_Tempo 
        Posicao_5, Posicao_2 = Posicao_2, Posicao_5

    if Valor_quinta > Valor_terceiro or Valor_quinta == Valor_terceiro and D_quinto < D_terceiro or D_quinto == D_terceiro and Qui_Tempo < T_Tempo:
        Valor_quinta, Valor_terceiro = Valor_terceiro, Valor_quinta
        D_quinto, D_terceiro = D_terceiro, D_quinto
        Qui_Tempo, T_Tempo = T_Tempo, Qui_Tempo 
        Posicao_5, Posicao_3 = Posicao_3, Posicao_5

    if Valor_quinta > Valor_quarto or Valor_quinta == Valor_quarto and D_quinto < D_quarto or D_quinto == D_quarto and Qui_Tempo < Q_Tempo:
        Valor_quinta, Valor_quarto = Valor_quarto, Valor_quinta
        D_quinto, D_quarto = D_quarto, D_quinto
        Qui_Tempo, Q_Tempo = Q_Tempo, Qui_Tempo 
        Posicao_5, Posicao_4 = Posicao_4, Posicao_5

#Bloco utilizado para comparar a quantidade de problemas resolvidos e a equipe responsável.
Eq_Dificil=equipe_1
maior_Dificil=Dificil_1

for x in range(5):
    
    if maior_Dificil < Dificil_2:
        maior_Dificil = Dificil_2
        Eq_Dificil = equipe_2
    if maior_Dificil < Dificil_3:
        maior_Dificil = Dificil_3
        Eq_Dificil = equipe_3
    if maior_Dificil < Dificil_4:
        maior_Dificil = Dificil_4
        Eq_Dificil = equipe_4
    if maior_Dificil < Dificil_5:
        maior_Dificil = Dificil_5
        Eq_Dificil = equipe_5

#Média Total das Equipes:
Média_Total= (Pontuacao_1 + Pontuacao_2 + Pontuacao_3 + Pontuacao_4 + Pontuacao_5) / 5

#Bloco utilizado para imprimir o Ranking e os resultados.
print("\033[34m°Ranking das Equipes:")
print(f"\033[37m_"*150)
print(f"\033[32m|1º Lugar: {Posicao_1} com {Valor_primeiro} pontos, resolvendo {D_primeiro} problemas difíceis em {P_Tempo} segundos.")
print(f"\033[33m|2º Lugar: {Posicao_2} com {Valor_segundo} pontos, resolvendo {D_segundo} problemas difíceis em {S_Tempo} segundos.")
print(f"\033[33m|3º Lugar: {Posicao_3} com {Valor_terceiro} pontos, resolvendo {D_terceiro} problemas difíceis em {T_Tempo} segundos.")
print(f"\033[33m|4º Lugar: {Posicao_4} com {Valor_quarto} pontos, resolvendo {D_quarto}  problemas difíceis em {Q_Tempo} segundos.")
print(f"\033[31m|5º Lugar: {Posicao_5} com {Valor_quinta} pontos, resolvendo {D_quinto}  problemas difíceis em {Qui_Tempo} segundos.")
print(f"\033[37m_"*150)

#Impressão Equipe vencedora
print(f"\033[32m|A equipe vencedora foi {Posicao_1}, resolvendo os problemas em {P_Tempo} segundos.")
print(f"\033[37m_"*150)

# Equipe com maio número de problemas difíceis resolvidos
print (f"\033[34m|A equipe que conseguiu resolver a maior quantidade de problemas difíceis foi {Eq_Dificil} com {maior_Dificil} resoluções.")
print(f"\033[37m_"*150)

#Impressão Média Total
print(f"\033[34m|A média total das equipes foi de : {Média_Total} pontos.")
print(f"\033[37m_"*150)

#Bloco que imprime a ordem inserida pelo usuário
print(f"\033[34m°Ordem inserida pelo usuário:")
print(f"\033[37m|A equipe {equipe_1} conseguiu {Pontuacao_1} pontos, resolvendo {Dificil_1} problemas difíceis em {Minutos1}:{segundos1} minutos.\t")
print(f"|A equipe {equipe_2} conseguiu {Pontuacao_2} pontos, resolvendo {Dificil_2} problemas difíceis em {Minutos2}:{segundos2} minutos.\t")
print(f"|A equipe {equipe_3} conseguiu {Pontuacao_3} pontos, resolvendo {Dificil_3} problemas difíceis em {Minutos3}:{segundos3} minutos.\t")
print(f"|A equipe {equipe_4} conseguiu {Pontuacao_4} pontos, resovendo {Dificil_4} problemas difíceis em {Minutos4}:{segundos4} minutos.\t")
print(f"|A equipe {equipe_5} conseguiu {Pontuacao_5} pontos, resolvendo {Dificil_5} problemas difíceis em {Minutos5}:{segundos5:} minutos.\t")
print(f"\033[37m_"*150)