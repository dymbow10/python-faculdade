#vê se a primeira palavra é prefixo da segunda
def ler():
    s1=input("Insira sua primeira palavra: ")
    s2=input("Insira sua segunda palavra: ")
    return s1,s2

def compara(s1,s2):
    pre=False
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            pre=True
    return pre

def impr(pre):
    print ("{:2s} é prefixo de {:2s}".format(s1,s2))
    return

s1,s2=ler()
if s1>=s2:
    print("Erro")
else:
    pre=compara(s1,s2)
    impr(pre)
            
