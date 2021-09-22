# -*- coding: cp1252 -*-
print '''Digite 1 para votar em João da Silva, 2 para votar em José Ramalho, 3 para votar em Maria Mattos, 4 para votar em Pedro Américo, 0 para votar em branco e qualquer outro valor para votar
nulo'''

vmax=win=js=jr=mm=pa=br=null=0

for i in range(0,20000):
    voto=int(raw_input('Digite seu voto '))

    if voto == 1:
        print'Você votou em João da Silva'
        js+=1
    elif voto == 2:
        print'Você votou em José Ramalho'
        jr+=1
    elif voto == 3:
        print'Você votou em Maria Mattos'
        mm+=1
    elif voto == 4:
        print'Você votou em Pedro Américo'
        pa+=1
    elif voto == 0:
        print'Você votou em branco'
        br+=1
    else:
        print'Você votou nulo'
        null+=1

if js>jr and js>mm and js>pa:
    vmax=js
    win='João da Silva'
elif jr>js and jr>mm and jr>pa:
    vmax=jr
    win='José Ramalho'
elif mm>js and mm>jr and mm>pa:
    vmax=mm
    win='Maria Mattos'
else:
    vmax=pa
    win='Pedro Américo'


print'''Os votos em João da Silva, José Ramalho, Maria Mattos e Pedro Américo são respectivamente {:1d}, {:1d}, {:1d} e {:1d}'''.format(js,jr,mm,pa)
print'Os votos brancos foram {:1d} e os nulos foram {:1d}'.format(br,null)
print'O vencedor da eleição foi {:1s} com {:1d} votos'.format(win,vmax)
