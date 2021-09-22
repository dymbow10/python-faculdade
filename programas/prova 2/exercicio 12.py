# -*- coding: cp1252 -*-
frase=raw_input("Insira sua frase ")
palavras=frase.split(' ')
ultima=palavras[-1]
palavrai=''
for i in range(1,(len(ultima)+1)):
    
    palavrai+=ultima[-i]
    
print 'A ultima palavra ao contrario é {:1s}'.format(palavrai)
    
