#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:20:10 2026

@author: aluno
"""

"""
4 – Desenvolva um algoritmo com uma função que receba uma lista numérica e retorne o
resultado da soma de todos os elementos dela. Seu programa principal deve solicitar 4
números ao usuário, chamar a função e exibir o resultado da soma na tela.
"""

num=[]

def somarNumeros(lista):
        resultado=float(0)
        for i in range(len(lista)):
                resultado+=lista[i]
        print(resultado)

for i in range(4):
        num.append(float(input(f"Número {i+1}: " )))
somarNumeros(num)
        
        