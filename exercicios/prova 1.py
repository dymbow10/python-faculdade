def ler():
    s=input("Insira sua frase: ")
    s=s.replace(' ','')
    return s

def opera(s):
    inv=''
    for i in range(1,len(s)+1):
        inv+=s[-i]
    if s==inv:
        print("É palindromo")
    else:
        print("Não é palindromo")

# main

s=ler()
opera(s)
        
#matheus sales de oliveira
#201810034911
