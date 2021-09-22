def ler():
    s=input("Insira uma frase: ")
    return s

def opera(s):
    s=s.split(" ")
    u=s[-1]
    return u

def impr(s,u):
    print("A última palavra da frase '{:1s}' é {:1s}".format(s,u))
    return

s=ler()
u=opera(s)
impr(s,u)
