# -*- coding: cp1252 -*-
def saudacao():
    print ("Seja bem vindo ao seu programa, Jo�o")
    peso=float(input("Por favor insira o peso de sua pesca de hoje em quilos: "))
    return peso

def taxa(peso):
    if peso > 50:
        excesso = peso-50
    multa=excesso*4
    return excesso,multa

def resultado(excesso,multa):
    print('Jo�o, sua pesca excedente foi de {:1.1f} quilos e voc� pagar� {:2.2f} reais de multa'.format(excesso,multa))
    return

#main

peso=saudacao()
excesso,multa=taxa(peso)
resultado(excesso,multa)
