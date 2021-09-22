p=input('Digite sua mensagem ')
codif=''
for i in range (0,len(p)):
    letra=p[i]
    cod=ord(letra)
    cod1=chr(cod+1)
    codif+=cod1
codif1=codif[::-1]
print ('mensagem original--> ',p,' codificada--> ',codif,' mais codificada ainda--> ',codif1)
