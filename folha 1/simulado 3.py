def segmentos_consecutivos  (frase):
    string=''
    k = 0
    for i in range(0,len(frase)):
        if string!=frase[i]:
            k+=1
            string=frase[i]
    return(k)
frase=input('Digite uma frase ')
k=segmentos_consecutivos(frase)
print('Existem {:2d} segmentos consecutivos'.format(k))
