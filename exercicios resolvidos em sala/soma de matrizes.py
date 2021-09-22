#soma 2 matrizes mXn

def ler():
    linhas = int(input("Insira o numero de linhas: "))
    colunas = int(input("Insira o numero de colunas: "))
    return linhas, colunas

def cria_1(linhas, colunas):
    matriz_1 = [None]*linhas
    for i in range(linhas):
        matriz_1[i] = [None]*colunas
        for j in range(colunas):
            matriz_1[i][j] = float(input(f"Insira o elemento [{i+1}, {j+1}] da matriz 1: "))
    return matriz_1

def cria_2(linhas, colunas):
    matriz_2 = [None]*linhas
    for i in range(linhas):
        matriz_2[i] = [None]*colunas
        for j in range(colunas):
            matriz_2[i][j] = float(input(f"Insira o elemento [{i+1}, {j+1}] da matriz 2: "))
    return matriz_2

def soma(matriz_1, matriz_2,linhas,colunas):
    result = [None]*linhas
    for i in range(linhas):
        result[i] = [None]*colunas
        for j in range(colunas):
            result[i][j] = matriz_1[i][j] + matriz_2 [i][j]
    return result

def impr(matriz_1, matriz_2, result, linhas, colunas):
    print('-'*15 + 'Matriz 1'+'-'*15)
    for i in range(linhas):
        for j in range(colunas):
            print(f"[{matriz_1[i][j]:^5}]", end='')
        print()

    print('-'*15 + 'Matriz 2' + '-'*15)
    for i in range(linhas):
        for j in range(colunas):
            print(f"[{matriz_2[i][j]:^5}]", end='')
        print()

    print('-'*15 + "Resultado" + '-'*15)
    for i in range(linhas):
        for j in range(colunas):
            print(f'[{result[i][j]:^5}]', end='')
        print()
    return

#main
m,n = ler()
matriz_1 = cria_1(m, n)
matriz_2 = cria_2(m, n)
result = soma(matriz_1, matriz_2, m, n)
impr(matriz_1, matriz_2, result, m, n)
