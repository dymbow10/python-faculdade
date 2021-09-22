'''Fazer uma matriz mxn e printar em forma tabular'''
def ler():
    linha=int(input("Insira o numero de linhas: "))
    coluna=int(input("Insira o numero de colunas: "))
    return linha,coluna

def cria(linha,coluna):
    matriz=[None]*linha
    for i in range(linha):
        matriz[i] = [None]*coluna
        for j in range(coluna):
            matriz[i][j] = float(input(f'Insira o valor para [{i+1}, {j+1}]: '))
    return matriz

def impr(matriz, linha, coluna):
    print("-"*15+"Matriz"+'-'*15)
    for i in range(linha):
        for j in range(coluna):
            print(f"[{matriz[i][j]:^5}]", end='')
        print()
    return
#main
m,n=ler()
matriz=cria(m,n)
impr(matriz,m,n)
