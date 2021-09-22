# -*- coding: cp1252 -*-
contb=contv=0
string=raw_input("Digite sua frase ").lower()
vogais=['a','e','i','o','u']
for i in range(len(string)):
    if string[i]==' ':
        contb+=1
    elif string[i] in vogais:
        contv+=1
print 'Sua frase tem {:1d} vogais e {:1d} espaços em branco'.format(contv,contb)
