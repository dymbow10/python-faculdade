def ler():
    nomes=[]
    while True:
        nom=input("Insira um nome ")
        if nom=='':break
        nomes.append(nom)
    return nomes

def pesq_bin(nomes):
    nomes.sort()
    nome_proc=input("Insira o nome a ser buscado ")
    i=0 #inicio
    f=len(nomes) #fim
    achei=False
    while i<f and achei==False:
        m=(i+f)//2 #meio
        if nome_proc == nomes[m]:
            achei=True
        elif nome_proc < nomes [m]:
            f=m-1
        else:
            i=m+1
    return achei,nome_proc

def impr(achei,nome_proc):
    if achei:
        print("O nome {:1s} foi encontrado".format(nome_proc))
    else:
        print("O nome {:1s} não foi encontrado".format(nome_proc))
    return

#main
nomes=ler()
achei,nome_proc=pesq_bin(nomes)
impr(achei,nome_proc)
