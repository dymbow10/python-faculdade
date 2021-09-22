# -*- coding: cp1252 -*-
dia,mes,ano=map(int,raw_input("Insira sua data de nascimento separada por '/' ").split('/'))
meses=['','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
for i in range(1,13):
    if i == mes:
        print dia, ' de ', meses[i], ' de ', ano


