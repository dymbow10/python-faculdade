#validar entrada

try:
    a=float(input("Insira um numero: "))
    b=float(input("Insira outro numero: "))
    c=a/b
    print("A divisão entre a e b é "+str(c))

except ZeroDivisionError:
    print('Erro, o denominador é zero')
