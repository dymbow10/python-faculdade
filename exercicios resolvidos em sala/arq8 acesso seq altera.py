# -*- coding: cp1252 -*-
# remove uma informação do arquivo
# busca sequencial em arquivo
def grava():
    import os
    os.chdir('e:/arquivos/dados')
    arq=open('prog8.txt','w')     
    while True:  
        nome=raw_input('Digite um nome --> ')
        if nome =='':break
        idade=raw_input('Digite uma idade --> ')
        arq.write(nome+','+idade+'\n')
    arq.close()
    return                           
def procura():
    import os
    os.chdir('e:/arquivos/dados')
    arq=open('prog8.txt','r')     
    auxi=open('baux.txt','w+')
    # procura sequencial em arquivo
    nomep=raw_input('Nome a remover ')
    for i in arq:
        dados=i.split(',')
        if dados[0]!=nomep:
            auxi.write(i) # grava se for diferente    
    arq.close() # fecha arq
    auxi.close() # fecha aux
    os.remove('prog8.txt') #apaga prog8.txt
    os.rename('baux.txt','prog8.txt')#renomeia arquivo   
    return 
def impr():
    import os
    os.chdir('e:/arquivos/dados')
    arq=open('prog8.txt','r')     
    print '\n{:>33s}\n'.format('Arquivo alterado')
    print '{:^30s}{:^10s}\n'.format('Nome','Idade')
    for i in arq:
        dados=i.split(',')            
        print('{:^30s}{:^10s}').format(dados[0],dados[1])
    return

grava()
procura()
impr()
                        
              
              
