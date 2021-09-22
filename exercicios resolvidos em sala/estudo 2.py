'''Elabore um programa Python que:
Gere ou atualize um arquivo podendo Incluir, Excluir, Alterar ou Pesquisar.
O arquivo   tem os seguintes campos:
matricula: campo numérico com 11 caracteres
nome:campo alfabético
data de nascimento: no formato ddmmaaaa campo numérico não nulo. Usar 2 caracteres para o dia e para o mes e 4 caracteres para ano.
Estes campos devem ter a digitação validada de acordo com sua natureza.
A inclusão,exclusão ou alteração devem ser validadas se existem ou não  no arquivo, conforme a ação a ser realizada.
Usando pesquisa binária verifique se uma determinada matricula ( a ser lida) se encontra no arquivo.
Caso exista emitir mensagem indicando além da matricula, o nome e a data de nascimento formatadas. Por exemplo:
José da Silva matricula xxx nascido em dd/mm/aaaa existe no arquivo.
O programa deve ter uma função própria  para cada ação -inclusão,exclusão, alteração ou pesquisa binária. Pode usar sort().'''

def legrava():
    print("O flag é um enter vazio!")
    while True:
        try:
            mat = input("Insira a matricula: ")
            if mat == '': return
            if len(mat) != 11: raise
            aux = int(mat)
            nome = input("Insira o nome: ")
            aux2 = nome
            nome = nome.replace(' ', '')
            if not nome.isalpha(): raise
            nome = aux2
            dia = int(input("Insira o dia do seu nascimento: "))
            if len(str(dia)) < 2: dia = '0'+ str(dia)
            elif len(str(dia)) > 2: raise
            mes = int(input("Insira o mês do seu nascimento: "))
            if len(str(mes)) < 2: mes = '0'+ str(mes)
            elif len(str(mes)) > 2: raise
            ano = int(input("Insira o ano do seu nascimento: "))
            if len(str(ano)) != 4: raise
            data = str(dia)+'/'+str(mes)+'/'+str(ano)+'\n'
            arq.write(mat+','+nome+','+data)
        except:
            print("Algo deu errado, reinsira seus dados")

def inclui():
    print("Aqui você inclui dados")
    print('matricula vazia para de inserir!')
    ar=arq.readlines()
    matriculas=[]
    for i in ar:
        i=i.split(',')
        matriculas.append(i[0])
    while True:
        try:
            mat = input("Insira a matricula: ")
            if mat == '': return
            if len(mat) != 11: raise
            elif mat in matriculas: raise
            aux = int(mat)
            nome = input("Insira o nome: ")
            aux2 = nome
            nome = nome.replace(' ', '')
            if not nome.isalpha(): raise
            nome = aux2
            dia = int(input("Insira o dia do seu nascimento: "))
            if len(str(dia)) < 2: dia = '0'+ str(dia)
            elif len(str(dia)) > 2: raise
            mes = int(input("Insira o mês do seu nascimento: "))
            if len(str(mes)) < 2: mes = '0'+ str(mes)
            elif len(str(mes)) > 2: raise
            ano = int(input("Insira o ano do seu nascimento: "))
            if len(str(ano)) != 4: raise
            data = str(dia)+'/'+str(mes)+'/'+str(ano)+'\n'
            dado = mat+','+nome+','+data
            ar.append(dado)
            arq.seek(0)
            arq.truncate()
            for i in ar:
                arq.writelines(i)
        except:
            print("Algo deu errado, reinsira seus dados")

def exclui():
    print("Aqui você exclui seus dados")
    print('matricula vazia para de inserir!')
    ar=arq.readlines()
    matriculas = []
    nomes = []
    datas = []
    for i in ar:
        i = i.split(',')
        matriculas.append(i[0])
        nomes.append(i[1])
        datas.append(i[2])
    while True:
        try:
            mat = input('Insira a matricula: ')
            if mat == '': return
            if len(mat) != 11: raise
            elif mat not in matriculas: raise
            aux = matriculas.index(mat)
            matriculas.pop(aux)
            nomes.pop(aux)
            datas.pop(aux)
            ar=[]
            for i in range(len(matriculas)):
                ar.append(matriculas[i]+','+nomes[i]+','+datas[i])
            arq.seek(0)
            arq.truncate()
            for i in ar:
                arq.writelines(i)
        except:
            print("Algo deu errado, reinsira seus dados")

def altera():
    print("Aqui você altera seus dados")
    print('matricula vazia para de inserir!')
    ar=arq.readlines()
    matriculas = []
    nomes = []
    datas = []
    for i in ar:
        i = i.split(',')
        matriculas.append(i[0])
        nomes.append(i[1])
        datas.append(i[2])
    while True:
        try:
            mat = input('Insira a matricula: ')
            if mat == '': return
            if len(mat) != 11: raise
            elif mat not in matriculas: raise
            aux = matriculas.index(mat)
            nomes.pop(aux)
            datas.pop(aux)
            nome = input("Insira o novo nome: ")
            aux2 = nome
            nome = nome.replace(' ', '')
            nome = aux2
            dia = int(input("Insira o dia do seu nascimento: "))
            if len(str(dia)) < 2: dia = '0'+ str(dia)
            elif len(str(dia)) > 2: raise
            mes = int(input("Insira o mês do seu nascimento: "))
            if len(str(mes)) < 2: mes = '0'+ str(mes)
            elif len(str(mes)) > 2: raise
            ano = int(input("Insira o ano do seu nascimento: "))
            if len(str(ano)) != 4: raise
            data = str(dia)+'/'+str(mes)+'/'+str(ano)+'\n'
            nomes.insert(aux,nome)
            datas.insert(aux,data)
            ar=[]
            for i in range(len(matriculas)):
                ar.append(matriculas[i]+','+nomes[i]+','+datas[i])
            arq.seek(0)
            arq.truncate()
            for i in ar:
                arq.writelines(i)
        except:
            print("Algo deu errado, reinsira seus dados")

def binaria():
    while True:
        try:
            achei=False
            matriculas=[]
            nomes=[]
            datas=[]
            ar=arq.readlines()
            ar.sort()
            for i in ar:
                i=i.split(',')
                matriculas.append(i[0])
                nomes.append(i[1])
                datas.append(i[2])
            mat = input('Insira a matricula a ser buscada: ')
            if len(mat) != 11: raise
            inicio=0
            fim=len(matriculas)
            while inicio != fim and achei == False:
                meio=(inicio+fim)//2
                if matriculas[meio] == mat:
                    achei = True
                elif matriculas[meio] > mat:
                    inicio = meio+1
                else:
                    fim = meio - 1
            if achei:
                aux = matriculas.index(mat)
                data = datas[aux].strip('\n')
                print(f"{nomes[aux]} de matricula {mat} nascido em {data} existe no arquivo")
            else:
                print(f"A matricula {mat} não se existe no arquivo")
            return
        except:
            print("Matricula fora de formatação")

#main
try:
    arq = open("Prova.txt",'a')
except:
    arq = open("Prova.txt",'w')
legrava()
arq.close()
arq = open("Prova.txt",'r+')
esc = input("Gostaria de (I)ncluir, (E)xcluir, (A)lterar ou (P)esquisar ? ").upper()
if esc == 'I': inclui()
elif esc == 'E': exclui()
elif esc == 'A': altera()
elif esc == 'P': binaria()
arq.close()
