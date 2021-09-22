# -*- coding: utf-8 -*-
#ler idade e sexo(M/F)
#determinar a media de idade dos homens
#flag idade negativa
soma=qtd=0
while True:
    idade=int(raw_input('Digite a idade '))
    if idade<0:
        break
    sex=raw_input('Qual seu sexo (M/F)').lower()
    if sex =='m'or sex=='f':
    
        if sex == 'm':
            soma+=idade
            qtd+=1
    else:
        print 'Sexo nao categorizado'
if qtd == 0:
    print 'não existem homens'
else:
    media=soma/qtd
    print 'media de idade dos homens {:2.1f}'.format(media)
    
