# -*- coding: cp1252 -*-
nomes=[]
jcont=0
while True:
    nome=raw_input('Insira um nome ').lower()
    nomes.append(nome)
    if nome == ' ':
        break

for i in nomes:
    if i == 'joão':
        jcont+=1
print 'O nome "João" aparece {:1d} vezes'.format(jcont)
