'''exemplo com dois arquivos tipo csv (comma separated values).
O primeiro arq1 (mestre) contém matricula e nome.
O segundo arq2 contém matricula, nome da disciplina cursada e a nota obtida.
Observe que os arquivos não estão ordenados, o que obriga para cada registro (ou seja de cada aluno)
do arquivo mestre a leitura do arquivo de transações.
A correlação é realizada a partir da matricula.
Por simplicidade no programa, as informações não foram validadas.
O relatorio emitido contém, para cada aluno, as disciplinas cursadas e as notas obtidas.'''
def legrava1():
    # este módulo é para criar o arquivo 1, mestre
    print('{:*^30}'.format('Cadastro de alunos'))
    print('pressione enter para encerrar')
    while True:
        mat=input('Digite a matricula ')
        if mat == '':
            arq1.write('*'+','+',')
            return
        nome=str(input('Digite o nome '))
        a=mat+','+nome+'\n'
        arq1.write(a) #grava
    return
def legrava2():
    lista=[]
    # este módulo é para criar o arquivo 2, transações
    print ('{:*^30}'.format('Disciplinas Cursadas'))
    while True:
        mat=input('Digite a matricula: ')
        if mat == '':
            arq2.write('*'+','+',')
            return
        desc=input('Digite a disciplina: ')
        nota=input('Digite a nota: ')
        lista.append(mat+','+desc+','+nota+'\n')
        lista.sort()
        for i in range(len(lista)):
            arq2.write(lista[i]) #grava um registro
    return 
def impr():
    arq1.seek(0)
    arq2.seek(0)
    print() # muda de linha
    print('{:*^30}'.format('Histórico Escolar'))
    while True:        
        mat = arq1.readline() # le um registro
        valor1 = mat.split(',')
        matr1 = valor1[0]
        nome=valor1[1]    
        if matr1=='*':  return
        arq2.seek(1) # mantem a posição relativa do arquivo 2
        print (' \nMatricula: {:4s}  Nome:  {:30s}  '.format(matr1,nome))
        # percorre o arq2 e seleciona os de mesma matricula
        while True:
            mat2=arq2.readline()
            valor2=mat2.split(',') 
            matr2=valor2[0]
            desc= valor2[1]
            nota=valor2[2] 
            if matr2=='*':
                break # retorna para o while externo 
            if matr2==matr1: #<-- se a matricula de arq2 for igual a de arq1
                nota=float(nota)
                print ('{:1s}     {:5.1f}'.format(desc,nota))
         
    arq1.close()
    arq2.close()
# programa principal
arq1=open('arq1.txt','w+')
arq2=open('arq2.txt','w+')      
legrava1()
legrava2()
impr()
arq1.close()
arq2.close()
