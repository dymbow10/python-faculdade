print("O programa multiplica X por Y n forma: 'x * y = x vezes Y+Y'")
import os
while True:
    #try: #esta é a região do tratamento de erro, se o usuario não inserir nada, ela vai para o except
        x = int(input("Insira o valor de X: "))
        y = int(input("Insira o valor de Y: "))
        soma = 0 #aqui eu inicializo a variavel soma
        if abs(x) < abs(y) : # se x for menor que y o abaixo é realizado
            if (y > 0 and x > 0) or (y < 0 and x < 0):
                print("oi")
                for i in range(abs(x)): #um for loop que vai de 0 à X
                    soma += abs(y) #a cada iteração y é adicionado à variavel soma
                    print("St="+str(soma)) #depois, printamos a varaivel soma como o pedido
                    #OBS: str(soma) é usado para converter um inteiro em string e tornar possivel a concatenação(tenta tirar, é um bom aprendizado)
                    #OBS2: abs(variavel) é o modulo da variavel

            elif y < 0 or x < 0:
                for i in range(abs(x)):
                    soma -= y
                    print("St="+str(soma))

        else: #elif não foi usado pois o unico outro caso de relevância é o caso y < x
            if (x > 0 and y > 0) or (x < 0 and y < 0):
                for i in range(abs(y)): #racicionio analogo ao de cima
                    soma += abs(x)
                    print("St="+str(soma))
            elif x < 0 or y < 0:
                for i in range(abs(y)):
                    soma -= x
                    print("St="+str(soma))
        print(str(x)+" * "+str(y)+" = "+str(soma))
        os.system("pause")
        break
    #except: #caso o codigo acima dê errado o abaixo ocorre
        print("Erro, por favor reinsira X e Y")
