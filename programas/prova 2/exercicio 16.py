# -*- coding: cp1252 -*-
print'-'*25
print'Aqui você será julgado(a)'
print'-'*25

guilty_meter=0
while True:
    a=raw_input('Você telefonou para a vítima? (s/n) ').lower()
    if a != 's' and a != 'n':
        print 'Responda a pergunta'
        continue
    elif a == 's':
        guilty_meter+=1
        break
    else:
        break

while True:
    b=raw_input('Você esteve no local do crime? (s/n) ').lower()
    if b != 's' and b != 'n':
        print 'Responda a pergunta'
        continue
    elif b == 's':
        guilty_meter+=1
        break
    else:
        break

while True:
    c=raw_input('Você mora perto da vítima? (s/n) ').lower()
    if c != 's' and c != 'n':
        print 'Responda a pergunta'
        continue
    elif c == 's':
        guilty_meter+=1
        break
    else:
        break

while True:
    d=raw_input('Você devia para a vítima? (s/n) ').lower()
    if d != 's' and d != 'n':
        print 'Responda a pergunta'
        continue
    elif d == 's':
        guilty_meter+=1
        break
    else:
        break

while True:
    e=raw_input('Você já trabalhou com a vítima? (s/n) ').lower()
    if e != 's' and e != 'n':
        print 'Responda a pergunta'
        continue
    elif e == 's':
        guilty_meter+=1
        break
    else:
        break

if guilty_meter == 5:
    print 'Você é o(a) assassino(a) e vai apodrecer na cadeia'
elif guilty_meter == 4 or guilty_meter == 3:
    print 'Você é cumplice e vai passar um tempo atrás das grades'
elif guilty_meter == 2:
    print'Você é suspeito(a), estamos de olho em você'
else:
    print 'Você é inocente, pedimos perdão pelo incoveniente'












    
