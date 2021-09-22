 # arquivo texto gravar uma qtd indeterminada de nomes
# alterar o terceiro nome
# modulo le e grava
def legrava():
    import os
    os.chdir ("e:/" ) # diretorio corrente 
    arq=open('nomes1.txt','w') # abre para escrita
    while True:
        nome=raw_input('digite o nome ')
        if nome.lower() == '': break
        nome='%30s' %nome # transforma o texto em 30 bytes
        arq.write(nome) #grava um nome
    arq.close() #fecha o arquivo
    return 
def altera():
    print '\nAltera o 3o. Nome gravado\n'
    import os
    os.chdir ("e:/ " ) # diretorio corrente 
    arq=open("nomes1.txt",'r+') # abre para leitura
    arq.seek(60) # pula 60 bytes
    nome=arq.read(30) # le 30 bytes
    print nome #imprime o terceiro nome
    arq.seek(60) # volta para antes
    nome=raw_input('digite o nome ')
    nome='%30s' %nome
    arq.write(nome) # escreve o terceiro nome
    arq.seek(60)#volta
    nome2=arq.read(30) #le o 3o. nome
    print '\n verifica nome alterado--> '+nome2
    arq.close()
    return
def impr():
    import os
    os.chdir ("e:/ " ) # diretorio corrente
    arq=open("nomes1.txt",'r') # abre para leitura
    print '\nLista arquivo com o 3o. Nome alterado\n'
    while True:
        z=arq.read(30)
        if z=='':break
        print z+'\n'
    arq.close()
    return 

# programa principal
legrava()
altera()
impr()
    
        
