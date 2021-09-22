#jogo para adivinhar o numero 'nc'
from random import *

print "Seu objetivo é adivinhar o numero escolhido aleatoriamente pelo computador"\
      " sabendo que ele é inteiro e está entre 1 e 10"
# define uma função chamada de 'main' que não recebe argumentos '()' e é executada ao final do código
def main():
    #define o valor de 'nc' como um inteiro entre 1 e 10
    nc=randint(1,10)
    #começa o while loop que só termina quando o jogador acerta o numero 'nc'
    while True:
        np=int(raw_input("Insira seu numero "))
        if np > nc:
            print"Tente um numero menor"
        elif np < nc:
            print"Tente um numero maior"
        elif np == nc:
            print"Parabéns, você venceu!"
            return
        
main()
