# -*- coding: utf-8 -*-
"""
10 - Escreva um programa que leia números inteiros do teclado. O programa deve ler os
números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de
números digitados, assim como a soma e a média aritmética.
"""
# Acredito que o programa deve desconsiderar o 0. O zero é pra encerrar.
quantDeNums=int(-1)
soma=int(0)
num=int(1)

while num!=0:
    num=int(input("num: "))
    quantDeNums+=1
    soma+=num
    
print(" ")
print("quantDeNums:",quantDeNums)
print("soma:",soma)

if quantDeNums==0:
    print("Nenhum número foi digitado. Não há média.")
else:
    media=float(soma/quantDeNums)
    print("media:",media)
    
