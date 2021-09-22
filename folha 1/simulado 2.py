def ler():
    n=int(input("Insira um numero inteiro não negativo: "))
    if n <= 0:
        print("ERRO")
        quit()
    return n

def calculo(n):
    i=2
    primos=total=0
    while primos < n:
        primo=True

        for j in range(2,i):
            if i % j == 0:
                primo=False
                break
        if primo:
            primos+=1
            total+=i
        i+=1
    return total

def impr(n,total):
    print("A soma dos {:1d} primeiros primos é {:1d}".format(n,total))
    return

n=ler()
total=calculo(n)
impr(n,total)

