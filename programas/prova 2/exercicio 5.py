# -*- coding: cp1252 -*-
info=[]
while True:
    while True:
        nome=raw_input('Insira seu nome ')
        if len(nome) < 3:
            print 'Nome fora de formata��o!'
            continue
        else:
            info.append(nome)
            break
    while True:
        age=int(raw_input('Insira sua idade '))
        if age < 0 or age > 150:
            print 'Idade impossivel!'
            continue
        else:
            info.append(age)
            break
    while True:
        sal=float(raw_input("Insira seu salario "))
        if sal <= 0:
            print 'Salario incorreto'
            continue
        else:
            info.append(sal)
            break
    while True:
        sex=raw_input("Insira seu sexo (M/F) ")
        if sex.lower() != 'm' and sex.lower() != 'f':
            print 'Sexo fora de forata��o'
            continue
        else:
            info.append(sex)
            break
    while True:
        estado=['s',',c','v','d']
        civil=raw_input('Insira seu estado civil: solteiro(a); casado(a); viuvo(a) ou divorciado(a)\n (S/C/V/D) ').lower()
        if civil not in estado:
            print 'Estado civil incorreto'
            continue
        else:
            info.append(civil)
            break
    resp=raw_input('Suas informa��es ' +str(info)+ ' est�o corretas? (S/N)').lower()
    if resp == 'n':
        print 'Retornando ao inicio'
        continue
    elif resp == 's':
        break
    else:
        print 'bem que me avisaram que �suario � merda...'
        quit()
print 'Informa��es validadas'
                
