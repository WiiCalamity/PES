#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2 – Crie um programa que leia 4 notas de um(a) determinado(a) estudante. Após a leitura
de todas notas, exiba a média aritmética simples e a situação final (aprovado(a) ou
reprovado(a)).
"""
notas=[0]*4 # Dá erro se eu não declarar a lista
media=float(0)

for i in range(4):
    print("Nota",i+1,":",end=" ")
    notas[i]=float(input())
    media+=notas[i]

media=media/4
if media>=6:
    situacao="Aprovado"
else:
    situacao="Reprovado"

print("Média:",media)
print("Situação:",situacao)