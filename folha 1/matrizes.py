'''crie uma matriz 3x3 e preencha com valores lidos, no final, mostre a matriz na tela
 de forma tabular'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(3):  # for loop de inserção
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Insira um valor para [{linha+1}, {coluna+1}]: "))
print('-'*30)
for linha in range(3):  # for loop de apresentação
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
