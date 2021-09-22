# -*- coding: cp1252 -*-
n=count=0
while True:
    o=raw_input('Você está satisfeito(a) com o produto? (S/N) ').lower()
    if o != 's' and o != 'n' and o != 'f':
        print'Opinião fora de formatação'
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

print 'A porcentagem de pessoas insatisfeitas é {:1.2f}% e o número de entrevistados foi {:1d}'.format(p,count)
