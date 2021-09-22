# -*- coding: cp1252 -*-
#ler uma palavra e a escrever ao contrario
p=raw_input('Insira sua frase ').lower()
palavras=''

for i in range (len(p)):
    if p[i]!=' ':
        palavras +=p[i]

palavrai=palavras[::-1]

if palavrai == palavras:
    print 'sua frase {:1s} é palidroma'.format(p)
else:
    print 'Sua frase {:1s} não é palidroma'.format(p)
    
