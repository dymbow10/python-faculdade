# criar uma matriz mxn

def ler():
    m=int(input("Insira o numero de linhas: "))
    n=int(input("Insira o numero de colunas: "))
    return m, n

def criar(m,n):
    matriz = [None]*m #gera as linhas
    for i in range(m):
        matriz[i] = [None]*n #para cada termo das linhas cria uma coluna
        for j in range(n):
            matriz[i][j] = float(input(f"Insira o termo [{i+1}, {j+1}]: "))
    return matriz

def impr(matriz):
    print('-'*30)
    for i in range(m):
        for j in range(n):
            print(f'[{matriz[i][j]:^5}]', end='')
        print()
    return
#main
m, n = ler()
matriz = criar(m,n)
impr(matriz)
