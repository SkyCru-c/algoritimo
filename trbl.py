import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
numero = 0
for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '
#Aqui você deve imprimir todo o conteúdo da variável memória


while(opcao != 4):
    primeira = 0
    for i in range(0, 20):
        print(memoria[i], end= "|")
    print()

    for i in range(20, 40):
        print(memoria[i], end= "|")
    print()

    for i in range(40, 60):
        print(memoria[i], end= "|")
    print()

    for i in range(60, 80):
        print(memoria[i], end= "|")
    print()

    for i in range(80, 100):
        print(memoria[i], end= "|")

    print()

  

    #print(memoria)
    #Menu do programa
    print("1 - Primeira Escolha", )
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

    if(opcao == 1):
        '''primeira escolha na qual o programa é alocado na primeirra partição grande o o suficiente para acomoda-lo'''
        #Implemente aqui a lógica da primeira escolha
        for i in range(100):
            
            if primeira == 0:
                if  memoria[i] == ' ': #verifica se o local em quetão é um espaço vazio para memoria ser alocada
                    numero += 1 #conta quantas espaços tem na memoria para para verificar se pode ser alocada

                else:
                    if primeira == 0: # verifica se o programa ja alocou um espaço na memoria
                        if numero >= tamanho: # verifica se tem espaço suficinete para a memoria ser alocada 
                            for j in range(i , i - tamanho, -1): #aloca a parte da memoria com a infomação
                                memoria[j - 1] = letra
                                primeira = 1
                
                    numero = 0       
            if i == 99 and primeira == 0: # verifica se ja foi alocada alguma infomação na memoria, caso não ira apresentar uma mensagem de erro
                print("erro: memoria não pode ser alocada, digite novamente ") 
 
    if (opcao == 2):
        '''melhor escolha,  a qal o programa é alocado na menor partiçao com tamanho suficiente para  acomoda-lo'''
        #Implemente aqui a lógica da melhor escolha
        for i in range(100):
            if memoria[i] == ' ': #verifica se o local em quetão é um espaço vazio para memoria ser alocada
                numero += 1  #conta quantas espaços tem na memoria para para verificar se pode ser alocada
        
            else:
                if primeira == 0: #verifica se o programa ja alocou um espaço na memoria
                    if numero == tamanho: #verifica se o programa tem um espaço ferfeito para alocar a informação
                        for j in range(i , i -tamanho, -1): #aloca a parte da memoria com a infomação
                            memoria[j - 1] = letra
                            primeira = 1
                    
                    
                    if i == 99 and primeira == 0: # caso não tenha um espaço perfeito
                        for i in range(100):
                            if numero >= tamanho: # verifica se a memoria tem espaço suficiciente ou ate maior para alocar o programa
                                for j in range(i , i -tamanho, -1): #aloca a parte da memoria com a infomação
                                    memoria[j - 1] = letra
                                    primeira = 1
                    
                    numero = 0
                    if i == 99 and primeira == 0: # verifica se ja foi alocada alguma infomação na memoria, caso não ira apresentar uma mensagem de erro
                        print("erro: memoria não pode ser alocada, digite novamente")
                    
    if(opcao == 3):
        contador = 0 
        mropart = 0
        '''pior escolha, na qual o programa é alocado  na maior partição com tamanho suficiente para acomoda-lo'''
        #Implemente aqui a lógica da pior escolha
        for i in range(100):
            if memoria[i] == ' ':
                numero +=1 
                if numero > mropart: #salva o local da memoria em quastão que tenha mais espaço na memoria
                    mropart = numero
                    posicao = i
            else:

                numero = 0        
        if tamanho<= mropart:
            for j in range(posicao, posicao - tamanho, -1):
                memoria[j - 1] = letra
        else:
            print("erro: memoria não pode ser alocada, digite novamente  ")        

                
    # Aqui você deve imprimir todo o conteúdo da variável memória


