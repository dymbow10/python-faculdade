# -*- coding: cp1252 -*-
nome=raw_input('Insira o nome do produto ').lower()
p=float(raw_input('Insira o pre�o do produto '))
if p <= 0:
    print"T� de sacanagem caba�o?"
    quit()
pmax=p
nmax=''
while nome != 'xxx':
    nome=raw_input('Insira o nome do produto ').lower()
    if nome == 'xxx':
        break
    p=float(raw_input('Insira o pre�o do produto '))
    if p <= 0:
        print"T� de sacanagem caba�o?"
        quit()
    if p > pmax:
        pmax=p
        nmax=nome
print "O produto mais caro � {:1s} e ele custa {:1.2f} reais".format(nmax, pmax)
