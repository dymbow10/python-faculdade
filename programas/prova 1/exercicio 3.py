# -*- coding: cp1252 -*-
nome=raw_input('Insira o nome do produto ').lower()
p=float(raw_input('Insira o preço do produto '))
if p <= 0:
    print"Tá de sacanagem cabaço?"
    quit()
pmax=p
nmax=''
while nome != 'xxx':
    nome=raw_input('Insira o nome do produto ').lower()
    if nome == 'xxx':
        break
    p=float(raw_input('Insira o preço do produto '))
    if p <= 0:
        print"Tá de sacanagem cabaço?"
        quit()
    if p > pmax:
        pmax=p
        nmax=nome
print "O produto mais caro é {:1s} e ele custa {:1.2f} reais".format(nmax, pmax)
