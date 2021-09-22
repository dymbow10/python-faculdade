# -*- coding: cp1252 -*-
# ler e gravar a data de vencimento, o valor e a descrição de uma qtd indeterminada de faturas
# determinar quais vão vencer nos proximos 10 dias .
def  le():  
    while True:
        try:
            dia=input("Digite o dia do vencimento ")
            if dia=='':                return
            mes=input("Digite o mes de vencimento ")
            ano=input("Digite o ano de vencimento ")
            venc= date(int(ano),int(mes),int(dia))
            if venc<hj:
                raise
            desc=input("Descriçao da mercadoria ")
            valor=input("Valor da mercadoria R$   ")
            reg=ano+','+mes+','+dia+','+desc+','+valor+'\n'
            arq.write(reg)
            print
            print ('*'*60)
        except:
            print ("  digite novamente "   )
def calc():
    arq.seek(0)
    print ('\nFaturas que vencem em 10 dias\n')
    fat=arq.readlines()
    fat.sort()
    for j in fat:
        dado=j.split(',')
        venc=date(int(dado[0]),int(dado[1]),int(dado[2]))
        
        if venc<=(hj+timedelta(days=10)):
            valor=float(dado[4])
            print ('Dia {:2s}/{:2s}/{:4s}      {:<20s}   R${:>5.2f}'.format( dado[2],dado[1],dado[0],dado[3], valor)     ) 
    return
# programa principal
from  datetime import *
hj=date.today()  
try:        
        arq=open('fatura.txt','a+')
except:
        arq=open('fatura.txt','w+')
le()
calc()
arq.close()
