# -*- coding: cp1252 -*-
n=count=0
while True:
    o=raw_input('Voc� est� satisfeito(a) com o produto? (S/N) ').lower()
    if o != 's' and o != 'n' and o != 'f':
        print'Opini�o fora de formata��o'
    if o=='f':
        break
    elif o=='n':
        n+=1
        count+=1
    elif o=='s':
        count+=1

print n, count
p=(n/float(count))*100
print p

print 'A porcentagem de pessoas insatisfeitas � {:1.2f}% e o n�mero de entrevistados foi {:1d}'.format(p,count)
