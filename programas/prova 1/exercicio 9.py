while True:
	a=float(input('Insira o lado a '))
	if a <= 0:
		print ('Lado incorreto')
		continue
	b=float(input('Insira o lado b '))
	if b <= 0:
		print ('Lado incorreto')
		continue
	c=float(input('Insira o lado c '))
	if c <= 0:
		print ('Lado incorreto')
		continue
	break
semi_perimetro=(a+b+c)/float(2)
if semi_perimetro > a and semi_perimetro>b and semi_perimetro>c:
	area=(semi_perimetro*(semi_perimetro-a)*(semi_perimetro-b)*(semi_perimetro-c))**(1/float(2))
	print (area)
else:
	print('Triangulo inexistente')
