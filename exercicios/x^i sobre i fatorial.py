#somatorio de x**i/i!
from math import *
s=0
n=int(input("Insira a quantidade de termos: "))
x=float(input("Digite um valor: "))
for i in range(1,n+1):
    s+=x**i/factorial(i)
print("A soma é {:1.2f}".format(s))
