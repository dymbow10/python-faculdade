ano=[]
mes=[]
dia=[]
while True:
    try:
        data=int(raw_input("Insira sua data de nascimento separada por '/' "))
        if data == '':
            break

        elif data.isdigit() == True:
            separado = data.split('/')
            dia.append(separado[0])
            mes.append(separado[1])
            ano.append(separado[2])


    except:
        print "Dados mal inseridos"

print dia, mes, ano
print data.isdigit()

