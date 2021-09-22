nomes=[]
datas=[]
reg=[]
def ler():
    while True:
        try:
            nome=raw_input("Insira um nome: ")
            if nome == '':
                break
            elif nome.isdigit==True:
                raise
            else:
                nomes.append(nome)
        except:
            print "Insira o nome novamente"
    return

def gera(nomes):
    for i in range(len(nomes)):
        dia=randint(1,31)
        mes=randint(1,12)
        ano=randint(2000,2018)
        data=date(ano,mes,dia)
        data=str(data.strftime("%d/%m/%Y"))
        datas.append(data)
        reg.append(datas[i]+' '+nomes[i])
    return

def bubble(reg):
    for j in range(len(reg)-1):
        for i in range(len(reg)-1-j):
            if reg[i]>reg[i+1]:
                reg[i],reg[i+1]=reg[i+1],reg[i]
    print reg
    return
from random import *
from datetime import *
ler()
gera(nomes)
bubble(reg)
