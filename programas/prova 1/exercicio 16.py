# -*- coding: cp1252 -*-
numero=int(raw_input('Insira seu n�mero '))
divisores=[]
soma=0
for i in range(1,numero):
	if numero%i==0:
		divisores.append(i)

for i in divisores:
	soma+=i

if soma == numero:
	print'seu n�mero � perfeito'
else:
	print'Seu n�mero n�o � perfeito'
