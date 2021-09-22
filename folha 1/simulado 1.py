def ler():
    n=int(input("Insira seu numero: "))
    return n
def teste(n):
    if n < 0:
        print ("O numero inserido é menor que 0")
        quit()
    return

def calc(n):
    igual=False
    for i in range(2,n):
        teste=(i-1)*i*(i+1)
        if teste == n:
            igual=True
            break
    return igual

def impr(igual,n):
    if igual:
        print("O numero {:1d} é triangular".format(n))
    else:
        print("O numero {:1d} não é triangular".format(n))
    return

n=ler()
teste(n)
igual=calc(n)
impr(igual,n)
