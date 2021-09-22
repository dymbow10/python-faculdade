frase=raw_input('Insira sua frase ')
palavra=''
palavrai=''
for i in range (len(frase)):
    if frase[i] == ' ':
        palavra=frase[i::]
        for i in range(1,len(palavra)):
            palavrai+=palavra[-i]
            if palavra[i] == ' ':
                break
            
print palavrai
