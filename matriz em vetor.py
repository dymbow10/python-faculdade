linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))

matriz = [[0]*colunas]*linhas


vetor = []

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = float(input(f"Insira um valor para {i+1},{j+1}: "))
        vetor.append(matriz[i][j])

print(vetor)
print(len(vetor))
