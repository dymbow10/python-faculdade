#achar aposição de um caractere numa string
def ler():
    frase=input("Insira sua frase bro: ")
    l=input('Insira a letra a ser procurada: ')
    return frase,l

def procura(frase,l):
    achei=False
    for i in range(len(frase)):
        if l == frase[i]:
            print("Caractere encontrado na posição {:1d}".format(i))
            achei=True
            break
    return achei

def impr(achei):
    if not achei:
        print ("Não encontrado")
#main
frase,l=ler()
achei=procura(frase,l)
impr(achei)

