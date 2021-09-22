# -*- coding: cp1252 -*-
a=raw_input('Insira sua frase ').lower()
b=raw_input('Insira uma outra frase ').lower()
l1=[]
l2=[]

for i in range (len(a)):
    if a[i] != ' ':
        l1+=a[i]

for i in range (len(b)):
    if b[i] != ' ':
        l2+=b[i]


print 'O comprimento da primeira frase é ' + str(len(a))
print 'O comprimento da segunda frase é ' + str(len(b))

if l1==l2:
    print 'As frases são iguais'
print l1,l2
