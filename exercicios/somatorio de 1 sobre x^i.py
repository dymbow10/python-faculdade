#somatorio de 1/x**i
s=0
n=int(input("Insira a quantidade de termos: "))
x=float(input("Digite um valor: "))
for i in range(n):    
    s+=1/x**i
print("A soma é {:1.2f}".format(s))

    
