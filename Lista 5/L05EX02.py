#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:13:15 2026

@author: aluno
"""

"""
2 – Elabore um algoritmo com uma função que retorne se um dado número é par ou
ímpar. Seu programa deve solicitar um número ao usuário, chamar a função e exibir o
resultado na tela.
"""

def parOuImpar(num):
        print("É par!" if num%2==0 else "É ímpar!")

parOuImpar(int(input("Número: ")))