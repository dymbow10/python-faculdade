#Frase palindroma sem [::-1]

def ler():
    a=input("Insira sua frase: ")
    return a

def check(a):
    b=''
    a=a.replace(' ','')
    for i in range(1,len(a)+1):
        b+=a[-i]
    return a,b

def impr(a,b):
    print(a)
    print(b)
    if a==b:
        print("É palindromo")
    else:
        print("Não é palindroma")
    return

#main

a=ler()
a,b=check(a)
impr(a,b)
    
