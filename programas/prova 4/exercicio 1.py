nomes=[]
datas=[]
reg=[]

#le e valida nomes
def ler():
    while True:
        try:
            nome=raw_input('Insira um nome: ')
            if nome == '': break
            elif nome.isdigit()==True:
                raise
            else:
                nomes.append(nome)
        except:
            print 'Insira novamente'
    return

#gera e valida datas com o datetime
def gerar(nomes):
    for i in range(len(nomes)):
        dia=randint(1,31)
        mes=randint(1,12)
        ano=randint(2000,2018)
        data=date(ano,mes,dia)
        data=str(data.strftime("%d/%m/%Y"))
        datas.append(data)
        reg.append(nomes[i]+' nascido(a) em '+datas[i])
    return


#bubble sort
def bubble(reg):
    for j in range(len(reg)-1):
        for i in range(len(reg)-1-j):
            if reg[i]>reg[i+1]:
                reg[i],reg[i+1]=reg[i+1],reg[i]
    return



from random import *
from datetime import *                 
ler()
gerar(nomes)
print nomes,datas,reg
bubble(reg)
print reg
