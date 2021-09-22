'''ler uma qtd indeterminada de valores e calcular
a media dos valores maiores que 5.
validar os dados'''

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
        if a >=5:
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
