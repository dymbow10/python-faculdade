# -*- coding: cp1252 -*-
count=countn=countm=counts=0
for i in range(0,10):
    sex=raw_input("Insira seu sexo (M/F) ").lower()
    if sex != 'm' and sex != 'f':
        print 'Sexo inv�lido'
    op=raw_input("Insira sua opini�o (S/N) ").lower()
    if op == 'n' and sex == 'm':
        countm+=1
        countn+=1
        count+=1
    elif op == 'n':
        countn+=1
        count+=1
    elif op == 's':
        counts+=1
        count+=1
    else:
        print'Opini�o mal formatada'
porc=(countm/float(count))*100

print'A quantidade de pessoas que disseram sim foi {:1d}'.format(counts)
print'A quantidade de pessoas que disseram n�o foi {:1d}'.format(countn)
print'A porcentagem de pessoas do sexo masculino que disseram n�o foi {:1.1f}%'.format(porc)
    
