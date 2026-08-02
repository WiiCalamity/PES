#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3 – Utilizando como base o exercício anterior, faça com seu programa exiba uma saída
formatada da forma exibida abaixo (abaixo é utilizado com exemplo com 3 notas). Você
deve fazer isso de duas formas: com while e com for.
Exibição com while:
Nota: 9.0
Nota: 7.5
Nota: 8.0
Exibição com for:
Nota: 9.0
Nota: 7.5
Nota: 8.0
"""

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

notas=[]
tamanho=int(input("Quantas notas devem ser digitadas? "))
for i in range(tamanho):
    print("Nota",i+1,":", end=" ")
    notas.append(float(input()))

cls()
print("Notas informadas (for):")
for i in notas:
    print("Nota:",i)

print(" ")

print("Notas informadas (while):")
i=int(0)
while i < tamanho:
    print("Nota:",notas[i])
    i+=1
