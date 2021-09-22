def ler():
    st1=input("Insira sua string 1: ")
    st2=input("Insira sua string 2: ")
    return st1,st2

def resolve(st1,st2):
    print(st1,len(st1))
    print(st2,len(st2))

    if len(st1)==len(st2):
        print('As strings tem o mesmo comprimento')
    else:
        print('As strings não tem o mesmo comprimento')

    if st1==st2:
        print("As strings são iguais")
    else:
        print("As strings são diferentes")
    return

st1,st2=ler()
resolve(st1,st2)
