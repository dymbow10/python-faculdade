''' Crie a função mat_transposta(matriz). A função deve receber uma matriz genérica
bidimensional, de qualquer tamanho (não necessariamente quadrada) e retornar a
matriz transposta, sem alterar a matriz original.
'''

linhas = int(input("Insira o numero de linhas: "))
colunas = int(input("Insira o numero de colunas: "))
matriz = [None] * linhas
for i in range(linhas):
    matriz[i] = [None]* colunas
    for j in range(colunas):
        matriz[i][j]= float(input(f"Insira o elemento {i+1},{j+1}: "))

for i in range(linhas):
    for j in range(colunas):
        print(f"[{matriz[i][j]:^5}]", end='')
    print()
print('\n')

def mat_transposta(matriz):
    for i in range(linhas):
        for j in range(colunas):
            print(f"[{matriz[j][i]:^5}]", end='')
        print()
mat_transposta(matriz)
