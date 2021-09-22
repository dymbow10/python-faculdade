# -*- coding: cp1252 -*-
#Ler nomes que serão associados a uma data entre 01/01/1970 e 5/7/2018 gerada
#aleatoriamente. Validar a data, se for invalida gerar nova data.
#Gravar em um arquivo, listar o arquivo ordenado por nomes

nomes=[]
datas=[]
reg=[]
from random import *
from datetime import *

def le():
    while True:
        nome=raw_input('Insira um nome ')
        if nome == '':
            break
        else:
            nomes.append(nome)
    return nome

def gera():
    for i in range(len(nomes)):
        dia=randint(1,31)
        mes=randint(1,12)
        ano=randint(1970,2018)
        data=date(ano,mes,dia)
        data=str(data.strftime("%d/%m/%Y"))
        datas.append(data)
        reg.append(nomes[i]+' nascido(a) em '+datas[i])
    reg.sort()
    for i in range(len(reg)):
        arq.write(reg[i]+'\n')

    return


try:
    arq=open('C:\Users\Matheus\Desktop\Listagem.xlsx','a+')
except:
    arq=open('C:\Users\Matheus\Desktop\Listagem.xlsx','w+')
le()
gera()
print nomes, datas, reg
arq.close()
    
