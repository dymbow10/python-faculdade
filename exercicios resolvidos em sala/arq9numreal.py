# -*- coding: cp1252 -*-
# ler uma quantidade indeterminada de numeros reais para um arquivo
# ler os dados do arquivo e determinar o maior
# validar os dados
def legrava():
    while True:
        try:
            num=raw_input('Digite um numero real ')
            if num=='':break
            num1=float(num)
            arq.write(num+'\n')
        except:
           print('**erro** Digite novamente')
    return
def calc():
    print 'entrei em calc'
    arq.seek(0)
    num=arq.readlines()
    print num
    maior=num[0]
    for i in num:
        if i >maior:
            maior=i
    print maior        
    return maior
def impr(maior):
    print 'entrei em em impr'
    print 'O maior valor é {:>10s}'.format(maior)
    return      
#programa principal
# atenção arq é variável global !
import os
#os.chdir('E:/arquivos/dados')
arq=open('dado1.txt','w+')
legrava()
maior=calc()
print 'maior'+maior
impr(maior)
arq.close()
            
            
