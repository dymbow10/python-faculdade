#calcular a media de n valores lidos usando while
n=int(raw_input("Digite o denominador "))
if n == 0:
    print "Ta querendo ferrar comigo po?"
    quit()
soma=i=0
while i<abs(n):
    x=float(raw_input('Insira um numero '))
    soma+=x
    i=i+1
m=soma/n
print'A media de seus valores eh {:1.2f}'.format(m)
