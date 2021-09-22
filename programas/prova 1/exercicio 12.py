# -*- coding: cp1252 -*-
maior=seg_maior=qtd_maior=qtd_seg_maior=0
while True:
    nome=raw_input('Insira seu primeiro nome ')
    if nome.isalpha()==False:
        print 'Nome inválido'
        continue
    while True:
            try:   
                altura=float(raw_input('Insira sua altura em metros '))
                if altura < 0 or altura > 2:
                    raise
                break
            except:
                print'ERRO, DIGITE NOVAMENTE'
    print nome, altura
    if altura == maior:
        qtd_maior+=1
    elif altura > maior:
        seg_maior=maior
        qtd_seg_maior=qtd_maior
        maior=altura
        qtd_maior=1
    elif altura == seg_maior:
        qtd_seg_maior+=1
    elif altura > seg_maior:
        seg_maior=altura
        qtd_seg_maior=1
    if nome.lower()=='maria':
        break
print '''A maior altura é {:1.2f}, a segunda maior altura é {:1.2f}
a quantidade de pessoas com a maior altura é {:1d} e a quantidade de pessoas 
com a segunda maior altura é {:1d}'''.format(maior, seg_maior, qtd_maior, qtd_seg_maior)
