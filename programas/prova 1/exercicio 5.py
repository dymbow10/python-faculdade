# -*- coding: cp1252 -*-
print '''Este programa calcula a soma de todos os valores divisiveis por 4 entre os numeros
inseridos'''
a=int(raw_input('Insira um numero '))
b=int(raw_input('Insira um numero maior que o anterior '))
soma=0
if a>b:
    print 'O valor inserido é menor que o anterior, soma abortada'

for i in range(a+1,b):
    if i%4==0:
        soma+=i
print 'A soma resulta em {:1d}'.format(soma)
