def grava():
    arq=open('prog2.txt','w') 
    while True:  
        nome=raw_input('Digite um nome --> ')
        if nome =='':
            break
        idade=raw_input('Digite uma idade --> ')
        arq.write(nome+','+idade+'\n') 
    arq.close()
    return
def ordem(nome,idade):
    n=len(nome)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nome[i]>nome[j]:
                nome[i],nome[j]=nome[j],nome[i]
                idade[i],idade[j]=idade[j],idade[i]
    return  nome,idade
def le():
     nomes=[]
     idades=[]
     arq=open('prog2.txt','r')
     for linha in arq:
        valores=linha.split(',') 
        nomes.append(valores[0])         
        idades.append(valores[1])                            
     arq.close()
     return nomes,idades
def impr(nomes,idades):
        print '\nNomes ordenados\n'
        n=len(nomes)
        for i in range(n):
              print('{:^30s}{:^10s}').format(nomes[i],idades[i])
        return
grava()
nomes,idades=le()
nomes,idades=ordem(nomes,idades)
impr(nomes,idades)              
                                           
              
              
