# -*- coding: cp1252 -*-
print 'Este programa calcula a soma de todos os numeros entre os inseridos'
a=int(raw_input('Insira um valor '))
b=int(raw_input('Insira um valor maior que o anterior '))
soma=0
if a>b:
    print 'O primeiro valor é maior que o segundo, soma negada'

for i in range(a+1,b):
    soma+=i

print 'A soma dos numeros entre os valores inseridos é {:1d}'.format(soma)
