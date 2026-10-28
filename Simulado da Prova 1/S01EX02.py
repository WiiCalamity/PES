#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 08:35:29 2026

@author: aluno
"""

""" 
– Elabore um algoritmo que leia 15 números de uma cartela de bingo e armazene-os em uma lista.
Aceite apenas números entre 1 e 75 e não permita valores repetidos. Ao final, ordene a lista e
exiba os números do menor para o maior.
"""
import random # Para testar
cartela=[]
index=0
while index < 15:
        #num=random.randint(0,100)
        num=int(input(f"[{index}]Faça o trabalho tedioso de digitar 15 números a mão [1-75]: "))
        if num in cartela:
                print("Negado. Já está na cartela.")
                continue
        elif num<1 or num>75:
                print("Negado. Fora do intervalo [1-75].")
                continue
        cartela.append(num)
        index+=1
cartela=sorted(cartela)
for num in cartela:
        print(num)
