#encriptar uma mensagem trocando uma letra
#pela letra seguinte

m=input("Insira sua mensagem: ")
crip=''
for i in range(len(m)):
    letra=m[i]
    cod=ord(letra)
    cod1=chr(cod+1)
    crip+=cod1

print("mensagem original:" ,m, " mensagem criptografada:",crip)
