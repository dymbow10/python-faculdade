''' este programa tem funções adicionais que estão comentadas. Para usa-las apague o
# antes das mesmas no main, não use mais de um algoritmo de busca ao mesmo tempo pois isso é ineficiente'''

def ler():
    nomes = []
    while True:
        nome=input("Insira um nome: ")
        if nome == '':
            return nomes
        else:
            nomes.append(nome)

def bubble(nomes):
    print(nomes)
    for i in range(len(nomes)-1):
        for j in range(i+1,len(nomes)):
            if nomes[i] > nomes[j]:
                nomes[i], nomes[j] = nomes[j], nomes[i]
    print(nomes)
    return nomes

def quick(nomes):
    print(nomes)
    troca = True
    tam = len(nomes)-1
    while tam > 0 and troca:
        troca = False
        for i in range(tam):
            if nomes[i] > nomes[i+1]:
                nomes[i],nomes[i+1] = nomes[i+1],nomes[i]
                troca = True
        tam -= 1
    print(nomes)
    return nomes

def sequencial(nomes):
    achei = False
    nome_proc = input("Insira o nome a ser buscado: ")
    for nome in nomes:
        if nome == nome_proc:
            achei = True
    return achei

def binaria(nomes):
    achei = False
    nome_proc = input("Insira o nome a ser buscado: ")
    ini = 0
    fim = len(nomes)-1
    while ini < fim and achei == False:
        meio = (ini+fim)//2
        if nome_proc == nomes[meio]:
            achei = True
        elif nome_proc < nomes[meio]:
            fim = meio-1
        else:
            ini = meio+1
    return achei

def impr(achei):
    if achei:
        print("Nome encontrado")
    else:
        print("Nome não encontrado")
    return

# main

nomes = ler()
#nomes = bubble(nomes)
nomes = quick(nomes)
#achei = sequencial(nomes)
achei = binaria(nomes)
impr(achei)
