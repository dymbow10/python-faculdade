# -*- coding: cp1252 -*-
print'-'*25
print'Aqui voc� ser� julgado(a)'
print'-'*25

guilty_meter=0
while True:
    a=raw_input('Voc� telefonou para a v�tima? (s/n) ').lower()
    if a != 's' and a != 'n':
        print 'Responda a pergunta'
        continue
    elif a == 's':
        guilty_meter+=1
        break
    else:
        break

while True:
    b=raw_input('Voc� esteve no local do crime? (s/n) ').lower()
    if b != 's' and b != 'n':
        print 'Responda a pergunta'
        continue
    elif b == 's':
        guilty_meter+=1
        break
    else:
        break

while True:
    c=raw_input('Voc� mora perto da v�tima? (s/n) ').lower()
    if c != 's' and c != 'n':
        print 'Responda a pergunta'
        continue
    elif c == 's':
        guilty_meter+=1
        break
    else:
        break

while True:
    d=raw_input('Voc� devia para a v�tima? (s/n) ').lower()
    if d != 's' and d != 'n':
        print 'Responda a pergunta'
        continue
    elif d == 's':
        guilty_meter+=1
        break
    else:
        break

while True:
    e=raw_input('Voc� j� trabalhou com a v�tima? (s/n) ').lower()
    if e != 's' and e != 'n':
        print 'Responda a pergunta'
        continue
    elif e == 's':
        guilty_meter+=1
        break
    else:
        break

if guilty_meter == 5:
    print 'Voc� � o(a) assassino(a) e vai apodrecer na cadeia'
elif guilty_meter == 4 or guilty_meter == 3:
    print 'Voc� � cumplice e vai passar um tempo atr�s das grades'
elif guilty_meter == 2:
    print'Voc� � suspeito(a), estamos de olho em voc�'
else:
    print 'Voc� � inocente, pedimos perd�o pelo incoveniente'












    
