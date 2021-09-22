def ler():
    lista=[]
    while True:
        n=input("Insira um numero: ")
        if n=='':break
        lista.append(float(n))
    return lista

def ordena(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista

def binaria(lista):
    achei=False
    valor_proc=float(input("Insira o valor a ser encontrado: "))
    i=0
    f=len(lista)-1
    while i<=f and achei == False:
        m=(i+f)//2
        if valor_proc == lista[m]:
            achei=True
        elif valor_proc < lista[m]:
            f=m-1
        else:
            i=m+1
    return achei, valor_proc

def impr(achei, valor_proc):
    if achei:
        print(f'{valor_proc}, encontrado')
    else:
        print(f'{valor_proc}, não encontrado')
#main
lista=ler()
achei,valor=binaria(lista)
impr(achei,valor)
