 # -*- coding: cp1252 -*-
# arquivo texto gravar uma qtd indeterminada de numeros
# modulo le e grava
def legrava():
 
    arq=open('num1.txt','w') # abre para escrita
    while True:
        num=input('digite o numero  ')
        if num=='': break
        arq.write(num+'\n') #grava um numero por linha
    arq.close() #fecha o arquivo
    return
def impr():
    print ('Numeros gravados')

    arq=open("num1.txt",'r') # abre para leitura
    
    for num1 in arq: # o objeto file é inteiravél
                 print ('{:5.2f}'.format(float(num1)))

    arq.close()
# programa principal
import os
os.chdir ("e:/" ) # diretorio corrente E
legrava()
impr()
    
        
