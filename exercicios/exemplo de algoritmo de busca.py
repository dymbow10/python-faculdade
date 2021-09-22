def ler():
    nomes=[]
    while True:
        nom=input("Insira um nome ")
        if nom=='':return nomes
        nomes.append(nom)

def lernom():
    nomep=input("Insira o nome a ser procurado ")
    return nomep

def procura(nomes,nomep):
    achei=False
    tam=len(nomes)
    i=0
    while not achei and i < tam:
        if nomes[i]==nomep:
            achei=True
            break
        else:
            i+=1
    return achei

def impr(nomep,achei):
    if achei:
        print("O nome "+nomep+" foi localizado na lista")
    else:
        print("O nome "+nomep+" não foi localizado na lista")
    return

#main
nomes=ler()
nomep=lernom()
achei=procura(nomes,nomep)
impr(nomep,achei)
