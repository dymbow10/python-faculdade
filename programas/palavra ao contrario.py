#ler uma palavra e a escrever ao contrario
p=raw_input('Insira sua palavra ')
palavrai=''
for i in range (len(p)):
    palavrai +=p[-(i+1)]
print palavrai
if p == palavrai:
    print 'Eh palidromo'
else:
    print 'Nao eh palidromo'
    
