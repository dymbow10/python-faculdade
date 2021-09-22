# -*- coding: cp1252 -*-
lista=[9,5,3,18,65,10,72,78,6]
#bubble sort 
def bubble(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1-j):
            if lista[i]>lista[i+1]:
                lista[i],lista[i+1]=lista[i+1],lista[i]

    return
#iterative binary search 
def binary(lista, valor):
    inicio=0
    fim=len(lista)-1

    while inicio <= fim:
        meio=(inicio+fim)//2
        if valor == lista[meio]:
            return True
        elif valor < lista[meio]:
            fim=meio-1
            continue
        elif valor > lista[meio]:
            inicio=meio+1
            continue
    return False


print lista

bubble(lista)
print lista
valor=int(raw_input("Insira o valor a ser procurado "))
binary(lista,valor)
print(binary(lista,valor))
