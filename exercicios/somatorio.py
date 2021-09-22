#somatorio de n termos
s=0
n=int(input("Digite a quantidade de termos "))
for i in range(n):
    x=float(input('Digite um valor '))
    s=s+x

print("O valor da soma é {:1.2f}".format(s))

    
