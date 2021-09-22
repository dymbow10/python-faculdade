#ler uma qtd indeterminada de nomes e gravar em um arquivo
#listar do arquivo os nomes iniciados com a letra 'a'
#mandar mensagem se não houver nenhum nome

def legrava():
    arq=open("/home/ime/Área de Trabalho/nomes.txt","w")
    while True:
        nome=input("Insira um nome: ")
        if nome=='':break
        arq.write(nome+'\n')
    arq.close()
    return

def impr():
    print("\nNomes Gravados\n")
    arq=open("/home/ime/Área de Trabalho/nomes.txt","r")
    nome=arq.readlines()
    print("\nNomes iniciados com a letra A\n")
    cont=0
    for n in nome:
        if n[0].lower()=='a':
            print(f"{n}",end='')
            cont+=1
    if cont==0:
        print("Não tem nomes começados por 'A' bro")
    arq.close()
    return
#main
legrava()
impr()
    
