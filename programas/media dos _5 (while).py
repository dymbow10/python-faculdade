# -*- coding: utf-8 -*-
#ler n valores
#calcular com while a media dos valores maiores que 5
n=int(raw_input("Digite de quantos numeros eh a media "))
soma=i=qtd=0

while i<n:
    x=float(raw_input('Insira um valor '))
    i+=1
    if x > 5:
        soma+=x
        qtd+=1
if qtd ==0:
    print "Não existem valores maiores que 5"
else:
    m=soma/qtd

print "Media={:1.2f}".format(m)
