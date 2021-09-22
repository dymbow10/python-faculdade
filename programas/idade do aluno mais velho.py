#nome do aluno mais velho
idadev=-1
nomev=''
while True:
    nome=raw_input('Digite o nome ').lower()
    if nome == 'pare':
        break
    idade=int(raw_input('Digite a sua idade '))
    if idade > 100:
        print 'Ah ta com certeza'
        break
    elif idade > idadev:
        idadev = idade
        nomev = nome
    
print 'Nome da pessoa mais velha eh {:1s} com {:1d} anos'.format(nomev,idadev)
