# -*- coding: cp1252 -*-
sage=cage=0
nomes=[]
maior_nome=''
while True:
    nome=raw_input('Insira seu nome ')
    if nome == '':
        break
    
    nomes.append(nome)
    idade=int(raw_input('E sua idade '))
    if idade < 0 or idade > 100:
        print '¬_¬'
        break
    
    sage+=idade
    cage+=1

for i in range (len(nomes)):
    if len(nomes[i]) > len(maior_nome):
        maior_nome=nomes[i]

print 'A pessoa com maior nome é {:1s} e a media das idades é {:1.1f}'.format(maior_nome,(sage/cage))
