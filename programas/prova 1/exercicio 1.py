#flag é a idade negativa
somam=somaf=contm=contf=salmax=0

while True:
    idade=int(input('Insira sua idade '))
    if idade < 0:
        break
    sex=input('Insira seu sexo (M/F) ').lower()
    if sex != 'f' and sex != 'm':
        print ("sexo não categotizado")
        
    sal=float(input('Insira seu salario '))
    if sex == 'f':
        somaf+=sal
        contf+=1
    elif sex =='m':
        somam+=sal
        contm+=1
    if idade < 30 and sal > salmax:
        salmax=sal
        
if contm == 0 or contf == 0:
    print ('Erro')

mediam=somam/contm
mediaf=somaf/contf

print('A media dos salarios dos homens eh {:1.2f} e das mulheres é {:1.2f}'.format(mediam, mediaf))
print ('A pessoa com maior salario e menos de 30 anos recebe {:1.2f}'.format(salmax))

