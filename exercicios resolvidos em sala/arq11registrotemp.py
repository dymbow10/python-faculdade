def grava():
    arq=open('prog2.txt','w') 
    while True:  
        nome=raw_input('Digite um nome --> ')
        if nome =='':
            break
        idade=raw_input('Digite uma idade --> ')
        sexo=raw_input('Digite o sexo--> ').lower()
        arq.write(nome+','+idade+','+sexo+','+'\n') 
    arq.close()
    return
def ordem(nome,idade):
    n=len(nome)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if idade[i]>idade[j]:
                nome[i],nome[j]=nome[j],nome[i]
                idade[i],idade[j]=idade[j],idade[i]
    return  nome,idade
def le():
     nomes=[]
     idades=[]
     sexo=[]
     arq=open('prog2.txt','r')
     for linha in arq:
        valores=linha.split(',')
        if valores[2]=='m':
            nomes.append(valores[0])         
            idades.append(valores[1])
     arq.close()
     return nomes,idades
def impr(nomes,idades):
        
        print "\n\nHomem mais velho {:30s} com {:5s} anos".format(nomes[-1],idades[-1])
        return
grava()
nomes,idades=le()
nomes,idades=ordem(nomes,idades)
impr(nomes,idades)              
                                           
              
              
