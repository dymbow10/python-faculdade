# -*- coding: cp1252 -*-
n=int(raw_input('Insira seu numero '))
primo=True
for i in range(2,abs(n)):
    if n%i == 0:
        primo=False
if n == 2:
    primo=True

if primo:
    print 'Seu numero é primo'
else:
    print 'Seu numero não é primo'
