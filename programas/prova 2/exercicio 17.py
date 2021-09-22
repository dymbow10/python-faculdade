frase=raw_input('Insira sua frase ')
frase_ = frase.split(' ')
frasec=frase.split(',')
palcont=0
ban=[' ',',']
for i in frase_:
    if len(frase_) !=1:
        palcont+=1

for i in frasec:
    if len(frasec) !=1:
        palcont +=1

print palcont
print frase_
print frasec
