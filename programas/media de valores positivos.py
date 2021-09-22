#determinar a media de uma quantidade de valores lidos positivos
#o flag é um valor negativo
soma=qtd=media=0
while True:
    x=float(raw_input("Insira um valor "))
    if x<0:
        break
    soma+=x
    qtd+=1
if qtd == 0:
    print "NOPE"
else:
    media=soma/qtd
    print "media={:1.2f}".format(media)
