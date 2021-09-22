''' Crie a função multiplica_matriz(mat1, mat2) que deve retornar o produto de duas
matrizes bidimensionais genéricas, sem alterar as matrizes originais. A função deve
imprimir uma mensagem de erro e retornar um vetor vazio ([]) caso não for possível
realizar o produto das duas matrizes.'''


linhas = int(input("Insira o numero de linhas: "))
colunas = int(input("Insira o numero de colunas: "))
matriz = [None] * linhas
for i in range(linhas):
    matriz[i] = [None]* colunas
    for j in range(colunas):
        matriz[i][j]= float(input(f"Insira o elemento {i+1},{j+1}: "))

linhas2 = int(input("Insira o numero de linhas: "))
colunas2 = int(input("Insira o numero de colunas: "))
matriz2 = [None] * linhas2
for i in range(linhas2):
    matriz2[i] = [None]* colunas2
    for j in range(colunas2):
        matriz2[i][j]= float(input(f"Insira o elemento {i+1},{j+1}: "))

print("Matriz 1")
for i in range(linhas):
    for j in range(colunas):
        print(f"[{matriz[i][j]:^5}]", end='')
    print()
print('\n')

print("Matriz 2")
for i in range(linhas2):
    for j in range(colunas2):
        print(f"[{matriz2[i][j]:^5}]", end='')
    print()

def multiplica_matriz(matriz,matriz2):
    try:
        if colunas != linhas2: raise
        matriz_resultado = [0] * linhas
        for i in range (linhas):
            matriz_resultado[i] = [0] * colunas2

        for i in range(len(matriz)):
            for j in range(len(matriz2[0])):
                for k in range(len(matriz2)):
                    matriz_resultado[i][j] += matriz[i][k] * matriz2[k][j]

        print("Resultado")

        for i in range(linhas):
            for j in range(colunas2):
                print(f"[{matriz_resultado[i][j]:^5}]", end='')
            print()
    except:
        print("Erro")
        print("Resultado = []")
        return

multiplica_matriz(matriz,matriz2)
