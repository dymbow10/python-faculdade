def ler():
    s=input("Insira uma frase: ")
    return s

def opera(s):
    k=0
    for i in range(len(s)):
       if s[i] == ' ' or s[i] == ',':
           k+=1
    return k

def impr(s,k):
    print("A frase '{:1s}' tem {:1d} palavras".format(s,k+1))
    return

#main

s=ler()
k=opera(s)
impr(s,k)
