#jogo para adivinhar o numero 'nc'
from random import *

print "Seu objetivo � adivinhar o numero escolhido aleatoriamente pelo computador"\
      " sabendo que ele � inteiro e est� entre 1 e 10"
# define uma fun��o chamada de 'main' que n�o recebe argumentos '()' e � executada ao final do c�digo
def main():
    #define o valor de 'nc' como um inteiro entre 1 e 10
    nc=randint(1,10)
    #come�a o while loop que s� termina quando o jogador acerta o numero 'nc'
    while True:
        np=int(raw_input("Insira seu numero "))
        if np > nc:
            print"Tente um numero menor"
        elif np < nc:
            print"Tente um numero maior"
        elif np == nc:
            print"Parab�ns, voc� venceu!"
            return
        
main()
