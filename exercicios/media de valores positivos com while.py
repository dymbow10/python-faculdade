#media de um conjunto de valores positivos
#flag é um valor negativo

s=d=0
while True:
    n=float(input("Insira um valor: "))
    if n<0:break
    s+=n
    d+=1
if d==0:
    print ("Denominador é 0")
else:
    m=s/d
    print('A média é '+str(m))
