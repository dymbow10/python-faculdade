'''ler nome e idade de um conjunto de pessoas e determinar a media
das idades. fag é um enter vazio'''
d=s=0
while True:
    nome=input("Insira seu nome: ")
    if nome == '':break
    idade=int(input("Insira sua idade: "))
    if idade < 0:
        print ("Idade incorreta")
        continue
    s+=idade
    d+=1
if d == 0:
    print("Nenhuma pessoa inserida")
else:
    m=float(s)/d
    print (m)
