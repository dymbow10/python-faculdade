# -*- coding: cp1252 -*-
check=['0','1','2','3','4','5','6','7','8','9','-']
n=raw_input('Digite o numero de telefone ')
semtraco=''
for i in range (len(n)):
    if n[i] not in check:
        print 'Não me trolla'
    elif n[i] !='-':
        semtraco+=n[i]
if len(semtraco) == 7:
    print 'Telefone contem apenas 7 digitos, acrescentando o 3 na frente'
    semtraco='3'+semtraco

comtraco=[]
for i in range (len(semtraco)):
    comtraco.append(semtraco[i])

comtraco.insert(4,'-')

formatado=''
for i in range (len(comtraco)):
    formatado+=comtraco[i]
print 'Telefone formatado {:1s}'.format(formatado)
