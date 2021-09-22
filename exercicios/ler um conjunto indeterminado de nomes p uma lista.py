#ler um conjunto indeterminado de nomes p/uma lista

def ler():
    lista=[]
    while True:
        a=input("Insira um nome bro: ")
        if a =='':break
        else:
            lista.append(a)
    return lista

def impr(lista):
    for i in lista:
        print (i)
    return

# main

x=ler()
impr(x)
