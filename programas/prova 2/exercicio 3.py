# -*- coding: cp1252 -*-


primeiro=''
nome=raw_input('Digite seu nome completo ')
for i in range (len(nome)):
    if nome[i] == ' ':
        break
    else:
        primeiro+=nome[i]
 
print primeiro[::-1]
