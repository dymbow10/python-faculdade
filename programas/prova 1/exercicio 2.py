
soma=odd=even=0
n=int(input('Insira o valor '))
while abs(n) > 0:
    if n % 2 == 0:
        soma+=n
        even+=1
        n-=1
        
    elif n % 2 != 0:
        odd+=1
        n-=1
        
    
    

m=soma/even

print('Existem {:1d} numeros pares, {:1d} numeros impares e a media dos pares eh {:1.2f}'.format(even, odd, m))
