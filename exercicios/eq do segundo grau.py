def ler():
    a=int(input("Insira o valor de 'a': "))
    b=int(input("Insira o valor de 'b': "))
    c=int(input("Insira o valor de 'c': "))
    return a,b,c

def calculo(a,b,c):
    raiz1=True
    d=b**2-4*a*c
    for i in range(2):
        if raiz1:
            raiz=(-b+d**1/2)/2*a
            raiz1=False
        else:
            raiz2=(-b-d**1/2)/2*a
    return raiz,raiz2

def impr(raiz,raiz2):
    print (str(raiz)+' '+str(raiz2))
    return

#main

a,b,c=ler()
raiz,raiz2=calculo(a,b,c)
impr(raiz,raiz2)
