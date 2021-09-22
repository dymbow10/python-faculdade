#validar entrada
#a deve ser maior que 10

try:
    a=float(input("Insira um numero: "))
    if a<10:raise
    b=float(input("Insira outro numero: "))
    print("A divisão é {0:1.2f}".format(a/b))
except Exception: #generaliza o tipo de erro
    print("Dado errado")
finally:
    print("Processo encerrado")
