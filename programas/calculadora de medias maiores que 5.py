n=int(raw_input("De quantos valores é a média? "))
s=cont=0
for i in range(0,n):
    v=float(raw_input("Insira um valor "))
    if v > 5:
        s=s+v
        cont=cont+1
if cont !=0:
    m=s/cont
    print "A media dos valores maiores que 5 é {:1.2f}".format(m)
else:
    print "Não existem valores"
    
