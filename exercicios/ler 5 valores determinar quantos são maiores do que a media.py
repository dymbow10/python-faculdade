'''ler 5 valores determinar quantos são maiores do que a media'''

def ler():
    lista=[None]*5
    print (lista)
    total=cont=0
    for i in range(5):
        n=float(input("Insira um numero: "))
        lista[i]=n
        total+=n
    print (lista)
    media=total/5

    for j in lista:
        if j > media:
            print(j)
    return

ler()
