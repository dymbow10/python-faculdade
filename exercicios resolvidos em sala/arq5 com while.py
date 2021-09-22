# arquivo texto gravar uma qtd indeterminada de nomes
# modulo le e grava
def legrava():
    import os
    os.chdir ("E:/" ) # diretorio corrente E
    arq=open('nomes1.txt','w') # abre para escrita
    while True:
        nome=raw_input('digite o nome ')
        if nome.lower() == 'pare': break
        arq.write(nome+'\n') #grava um nome por linha
    arq.close() #fecha o arquivo
    return
def impr():
    print 'Nomes gravados'
    import os
    os.chdir ("E:/ " ) # diretorio corrente E
    arq=open("nomes1.txt",'r') # abre para leitura
    while True:
        nome=arq.readline()
        if nome=='':
            break
        print nome
    arq.close()
# programa principal
legrava()
impr()
    
        
