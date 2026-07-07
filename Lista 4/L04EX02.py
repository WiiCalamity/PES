#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2 – Crie um programa que registrará as notas de um estudante. O programa deve
perguntar ao usuário quantas notas devem ser digitadas e, em seguida, fazer a leitura das
notas e, ao final, exibir todas as notas digitadas na tela.
"""
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

notas=[]
tamanho=int(input("Quantas notas devem ser digitadas? "))
for i in range(tamanho):
    print("Nota",i+1,":", end=" ")
    notas.append(input())

cls()
print("Notas informadas:")
for i in range(tamanho):
    print(">",notas[i])    