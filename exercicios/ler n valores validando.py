#elabore um programa que leia n valores e faça a média
#flag é 0

def ler():
    while True:
        try:
            a=float(input("Insira um valor: "))
            return a
        except:
            print("Use numeros")

def soma():
    soma=cont=media=0
    while True:
        a=ler()
        if a==0:break
        soma+=a
        cont+=1
    erro=False
    try:
        media=soma/cont
    except Exception:
        print("ERRO DIVISÃO POR ZERO!!!")
        erro=True
    return media,erro

def impr(media,erro):
    if erro:
        print("")
    else:
        print("A media é {:1.2f}".format(media))
    return

media,erro=soma()
impr(media,erro)
