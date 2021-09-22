#variaveis são determinadas
cont=0
soma=0
cf=0
cm=0
#as primeiras questões são fora do loop para a definição do idmin e do idmax
s=raw_input('Qual seu sexo (M/F)? ').lower()
if s!= 'm' and s!= 'f':
    print "sexo incorreto!"
    quit()
        
age=int(raw_input("Qual a sua idade? "))
#define as variaveis idmin e idmax
idmax=age
idmin=age
if age < 1 or age > 100:
    print "Idade incorreta!"
    quit()

sal=float(raw_input("Quanto voce ganha? "))
soma+=sal

if s == 'f' and sal >= 1000:
        cont=cont+1
#faz a contagem das mulheres e dos homens   
if s =='f':
    cf=cf+1
else:
    cm=cm+1

for i in range(0,2):
    s=raw_input('Qual seu sexo (M/F)? ').lower()
    
    if s!= 'm' and s!= 'f':
        print "sexo incorreto!"
        quit()

    age=int(raw_input("Qual a sua idade? "))
        
    if age < 1 or age > 100:
        print "Idade incorreta!"
        quit()

    if age > idmax:
        idmax=age
    elif age < idmin:
        idmin=age

    sal=float(raw_input("Quanto voce ganha? "))

    soma+=sal

    if s == 'f' and sal >= 1000:
        cont=cont+1
    
    if s =='f':
        cf=cf+1
    else:
        cm=cm+1

m=soma/3

print 'A media dos salarios eh {:1.2f}'.format(m)
print 'O numero de mulheres que recebem mais que R$1000 eh {:1d}'.format(cont)
print 'O mais jovem tem {:1d} anos e o mais velho tem {:1d} anos'.format(idmin,idmax)
print 'Existem {:1d} homens e {:1d} mulheres'.format(cm,cf)




















