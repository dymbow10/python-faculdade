def grava():
 #   import os
#    os.chdir("E:/arquivos/dados")
    arq=open('prog2.txt','w') 
    while True:  
        nome=raw_input('Digite um nome --> ')
        if nome =='':
            break
        idade=raw_input('Digite uma idade --> ')
        sexo=raw_input('Digite o sexo-->  ')
        arq.write(nome+','+idade+','+sexo+'\n') 
    arq.close()
    return
def monta():
#     import os
#     os.chdir("E:/arquivos/dados")
     nomes=[]
     idades=[]
     sexo=[]
     arq=open('prog2.txt','r')
     z=arq.readlines()
#     print z
     for linha in z:
#         print linha
         valores=linha.split(',')
         if valores[2]=='m':
            nomes.append(valores[0])         
            idades.append(valores[1])
     print nomes,idades       
     arq.close()
     return nomes,idades
def ordem(nome,idade):
    n=len(nome)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nome[i]>nome[j]:
                nome[i],nome[j]=nome[j],nome[i]
                idade[i],idade[j]=idade[j],idade[i]
    return  nome,idade
def impr(nomes,idades):
    print nomes
    print idades
    print '\nNomes mais velho\n'
    n=len(nomes)
 #   print('{:^30s}{:^10s}').format(nomes[n],idades[n])
    return
grava()
nomes,idades=monta()
nomes,idades=ordem(nomes,idades)
impr(nomes,idades)              
                                           
              
              
