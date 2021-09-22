cont=contn=0
frase=raw_input('Insira sua frase ').lower()
frase=frase.split(" ")
frase1=frase[1]
print frase
print frase1
vogais=['a','i','o','e','u']
for i in range (len(frase1)):
    if frase1[i] not in vogais:
        contn+=1
    else:
        cont+=1
print cont
