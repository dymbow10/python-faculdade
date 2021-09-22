# -*- coding: cp1252 -*-
n=int(raw_input("Insira o numero do boi "))
peso=float(raw_input("Insira o peso do boi "))
if peso <= 0 or n <= 0:
    print'Dados invalidos'
pesomax=pesomin=peso
boimax=boimin=n
i=0
while i < 9:
    n=int(raw_input("Insira o numero do boi "))
    peso=float(raw_input("Insira o peso do boi "))
    if peso <= 0 or n <= 0:
        print'Dados invalidos'
        break

    i+=1
    if peso > pesomax:
        pesomax=peso
        boimax=n
    elif peso < pesomin:
        pesomin=peso
        boimin=n

print'O boi mais pesado é o numero {:1d} com {:1.2f} quilos'.format(boimax,pesomax)
print'O boi mais leve é o numero {:1d} com {:1.2f} quilos'.format(boimin,pesomin)
