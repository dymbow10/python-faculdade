def ler():
    nomes=[]
    while True:
        nom=input("Insira um nome ")
        if nom=='':return nomes
        nomes.append(nom)

def ordem(nomes):
    tam=len(nomes)
    for i in range(tam-1):
        for j in range(i+1,tam):
            if nomes[i]>nomes[j]:
                nomes[i],nomes[j]=nomes[j],nomes[i]
    return nomes

def impr(nomes):
    print("Nomes ordenados ")
    for i in nomes:
        print(i)
    return

#main
nomes=ler()
ordem(nomes)
impr(nomes)
