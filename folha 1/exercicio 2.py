# -*- coding: cp1252 -*-
def entrada():
    salh=float(input("Quanto você ganha por hora? "))
    horas=float(input("E quantas horas você trabalha esse mês? "))
    return salh,horas

def calculo(salh,horas):
    sal=salh*horas
    ir=sal*0.11
    sall=sal-ir
    inss=sall*0.08
    sall=sall-inss
    sind=sall*0.05
    sall=sall-sind
    return sal,ir,inss,sind,sall

def resultado(sal,inss,sind,sall):
    print ("Seu salario bruto é de {:2.2f} reais".format(sal))
    print ("Você pagou ao INSS {:1.1f} reais".format(inss))
    print ("Você pagou ao sindicato {:1.1f} reais".format(sind))
    print ("Seu salario liquido é de {:1.1f} reais".format(sall))
    return

#main

salh,horas=entrada()
sal,ir,inss,sind,sall=calculo(salh,horas)
resultado(sal,inss,sind,sall)
