'''Escreva uma função para condensar os elementos de uma lista ordenada L, que
contém inteiros repetidos. Por exemplo, para L = [3, 3, 3, 3, 7, 7, 13, 13, 23], a função
retorna ['3^4', '7^2', '13^2', '23'] (repare que são strings). Note-se que no caso de um
número aparecer uma única vez, não deve haver expoente unitário.
'''

l=[]

while True:
    n = input("Insira um numero: ")
    if n == '': break
    else: l.append(n)
l.sort()
vetor=[]
cont=0
for i in l:
    for j in l:
        if i == j:
            cont += 1
    if cont > 1 and (i+'^'+str(cont)) not in vetor:
        vetor.append(i+'^'+str(cont))
    elif cont == 1 and i not in vetor:
        vetor.append(i)
    cont = 0
vetor.sort()
print(vetor)
