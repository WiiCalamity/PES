#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7 – Implemente um programa para calcular sua média final em uma determinada unidade
curricular. O programa deve solicitar ao usuário a quantidade de notas, o valor para cada
uma das notas e exibir, ao final, a média aritmética simples e informar se o(a) estudante
está Aprovado ou Reprovado. Considere que a média mínima para a aprovação é 6.
"""
soma=0
quantDeNotas=int(input("quantDeNotas: "))
for i in range(1, quantDeNotas+1):
    print("Nota",i,":", end=" ")
    nota=float(input())
    soma=float(soma+nota)
    
media=float(soma/quantDeNotas)
print("Média:",media)
if media>=6:
    print("Aprovado.")
else:
    print("Reprovado.")
    