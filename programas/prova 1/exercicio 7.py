# -*- coding: cp1252 -*-
print '''Digite 1 para votar em Jo�o da Silva, 2 para votar em Jos� Ramalho, 3 para votar em Maria Mattos, 4 para votar em Pedro Am�rico, 0 para votar em branco e qualquer outro valor para votar
nulo'''

vmax=win=js=jr=mm=pa=br=null=0

for i in range(0,20000):
    voto=int(raw_input('Digite seu voto '))

    if voto == 1:
        print'Voc� votou em Jo�o da Silva'
        js+=1
    elif voto == 2:
        print'Voc� votou em Jos� Ramalho'
        jr+=1
    elif voto == 3:
        print'Voc� votou em Maria Mattos'
        mm+=1
    elif voto == 4:
        print'Voc� votou em Pedro Am�rico'
        pa+=1
    elif voto == 0:
        print'Voc� votou em branco'
        br+=1
    else:
        print'Voc� votou nulo'
        null+=1

if js>jr and js>mm and js>pa:
    vmax=js
    win='Jo�o da Silva'
elif jr>js and jr>mm and jr>pa:
    vmax=jr
    win='Jos� Ramalho'
elif mm>js and mm>jr and mm>pa:
    vmax=mm
    win='Maria Mattos'
else:
    vmax=pa
    win='Pedro Am�rico'


print'''Os votos em Jo�o da Silva, Jos� Ramalho, Maria Mattos e Pedro Am�rico s�o respectivamente {:1d}, {:1d}, {:1d} e {:1d}'''.format(js,jr,mm,pa)
print'Os votos brancos foram {:1d} e os nulos foram {:1d}'.format(br,null)
print'O vencedor da elei��o foi {:1s} com {:1d} votos'.format(win,vmax)
