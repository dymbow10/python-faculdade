def ler():
    nomes=[]
    while True:
        nom=input("Insira um nome ")
        if nom=='':return nomes
        nomes.append(nom)

def quick(nomes):
    troca=True
    tam=len(nomes)-1
    while tam>0 and troca:
        troca = False
        for i in range(tam):
            if nomes[i]>nomes[i+1]:
                nomes[i],nomes[i+1]=nomes[i+1],nomes[i]
                troca=True
        tam-=1
    return nomes

def impr(nomes):
    print("Nomes ordenados ")
    for i in nomes:
        print(i)
    return

#main
nomes=ler()
quick(nomes)
impr(nomes)
