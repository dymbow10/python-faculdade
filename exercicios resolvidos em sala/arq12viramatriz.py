# -*- coding: UTF-8 -*-
# ler uma quantidade indeterminada de numeros inteiros para um arquivo
# ler os dados do arquivo para uma matriz quadrada de mxm
# exibir sob a forma de tabela
# validar os dados
def legrava():
    while True:
        try:
            num=input('Digite um numero inteiro: ')
            if num=='':break
            arq.write(num+'\n')
        except:
           print('**erro** Digite novamente')
    return
def lematriz():
    arq.seek(0)
    m=int(input('Digite m: ')) #qtd linhas
    a=[None]*m #cria uma linha com m valores
    for i in range(m):
        a[i]=[None]*m #para cada m cria uma coluna com m valores
        for j in range(m):
            a[i][j]=int(arq.readline())
    return  a,m
def impr(a,m):
     print('\n{:*^30}\n'.format('Matriz Lida'))
     for i in range(m):
         for j in range(m):
             print('{:12d}'.format(a[i][j]), end='')
         print()
     return     
       
#programa principal
# atenção arq é variável global !
arq=open('dado1.txt','w+')
legrava()
a,m=lematriz()
impr(a,m)
arq.close()            
            
