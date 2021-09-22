# arquivo texto gravar uma qtd indeterminada de nomes
# modulo le e grava
def legrava():
    import os
    os.chdir ("e:/" ) # diretorio corrente E
    arq=open('nomes1.txt','w') # abre para escrita
    while True:
        nome=input('digite o nome ')
        if nome == '': break
        nome='%30s' %nome # transforma o texto em 30 bytes
        arq.write(nome) #grava um nome
    arq.close() #fecha o arquivo
    return 
def impr():
    print ('Nomes gravados')
    import os
    os.chdir ("e:/ " ) # diretorio corrente E
    arq=open("nomes1.txt",'r') # abre para leitura
    while True:
       nome=arq.read(30)#le 30 bytes
       if nome=='': # se chegou ao final do arquivo
            break
       print (nome)        
    arq.close()
# programa principal
legrava()
impr()
    
        
