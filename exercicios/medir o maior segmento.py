#exibir quantos caracteres tem o maior segmento

def segmentos(frase):
    string=''
    cont=k=0
    maior=1
    for i in range(len(frase)):
        if string!=frase[i]:
            if cont>maior:
                maior=cont
            k+=1
            string=frase[i]
            cont=0
        else:
            cont+=1
            
    return k,maior

frase=input('Digite uma frase: ')
k,maior=segmentos(frase)
print('Existem {:1d} segmentos consecutivos e o maior deles tem {:1d} caractéres'.format(k,maior))
