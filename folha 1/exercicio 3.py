def ler():  # le o tamanho do comodo
    tam = float(input('Insira o tamanho do comodo em M²: '))
    return tam


def calculo(tam):  # calcula quanto será gasto para pinta-lo
    litros = tam / 3
    latas = litros / 18
    if latas < 1:
        latas = 1
    custo = latas * 80.00
    return latas, custo


def impr(latas, custo):  # imprime as informações p/ usuario
    print("Você usará {:1.1f} latas e gastará {:1.2f} reais".format(latas, custo))
    return


# main
tam = ler()
latas, custo = calculo(tam)
impr(latas, custo)
