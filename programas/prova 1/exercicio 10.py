# -*- coding: cp1252 -*-
n=int(raw_input("Insira a quantidade de pessoas "))
soma=count=pea=0
for i in range(0,n):
    age=int(raw_input('Digite sua idade '))
    soma+=age
    count+=1
    if age >= 21 and age <= 65:
        pea+=1
    elif age <= 0 or age >= 100:
        print 'Idade incorreta'
        break

media=soma/float(count)
print pea, count
porc=(pea/float(count)*100)
print'A média de idade é {:1.2f} e a porcentagem dos que tem entre 21 e 65 anos é {:1.1f}%'.format(media,porc)

