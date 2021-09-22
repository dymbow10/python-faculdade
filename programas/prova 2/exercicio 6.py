# -*- coding: cp1252 -*-
vogais=['a','e','i','o','u','A','E','I','O','U']
contv=0
contc=0
conts=0
frase=raw_input("Insira sua frase ")
if frase == '':
    print 'Se mata lixo'
for i in range (len(frase)):
    if frase[i] in vogais:
        contv+=1
    elif frase[i] == ' ':
        conts+=1

    else:
        contc+=1
        
print frase, contv, contc, conts
print 'A frase tem {:1d} vogais, {:1d} consoantes e {:1d} espaços em branco'.format(contv,contc,conts)
