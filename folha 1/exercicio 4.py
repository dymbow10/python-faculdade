def ola():
    print("Bem vindo ao software de cálculo de reajuste de salários")
    return

def entrada():
    sal=float(input("Por favor insira o salário do colaborador: "))
    if sal <= 0:
        print("Valor incorreto")
        quit()
    return sal

def reajuste(sal):
    g1=g2=g3=g4=False
    if sal <= 280:
        aumento = sal * 0.20
        sal_a = sal + aumento
        g1=True
    elif sal > 280 and sal < 700:
        aumento = sal * 0.15
        sal_a = sal + aumento
        g2=True
    elif sal > 700 and sal < 1500:
        aumento = sal * 0.10
        sal_a = sal + aumento
        g3=True
    else:
        aumento = sal * 0.05
        sal_a = sal + aumento
        g4=True
    return sal_a, aumento, g1, g2, g3, g4

def impr(sal, sal_a, aumento, g1, g2, g3, g4):
    if g1:
        print("O aumento foi de 20%")
    elif g2:
        print("O aumento foi de 15%")
    elif g3:
        print("O aumento foi de 10%")
    else:
        print("O aumento foi de 5%")
    print("O salário antes do reajuste era {:1.2f} reais".format(sal))
    print("O valor do aumento foi de {:1.2f} reais".format(aumento))
    print("O novo salário é {:1.2f} reais".format(sal_a))
    return

#main

ola()
sal=entrada()
sal_a, aumento, g1, g2, g3, g4=reajuste(sal)
impr(sal, sal_a, aumento, g1, g2, g3, g4)
