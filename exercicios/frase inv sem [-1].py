#ler uma frase e exibi-la invertida
#não pode usar [::-1]

inv=''
n=input("Insira sua frase bro: ")

for i in range(1,len(n)+1):
    inv+=n[-i]

print (inv)
