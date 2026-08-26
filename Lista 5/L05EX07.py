#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7 - Desenha moldura. Construa uma função que desenhe um retângulo usando os
caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas,
sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se
valores fora da faixa forem informados, eles devem ser modificados para valores dentro
da faixa de forma elegante
"""
charVertical="|"
charHorizontal="−"
charCanto="+"
charVazio=" "
charTeste="#"

def desenharRetangulo(linhas=1,colunas=1):
        if linhas>20:
                print("Número de linhas fora da faixa... usando 20.")
                linhas=20
        elif linhas<1:
                print("Número de linhas fora da faixa... usando 1.")
                linhas=1
        if colunas>20:
                print("Número de colunas fora da faixa... usando 20.")
                colunas=20
        elif colunas<1:
                print("Número de colunas fora da faixa... usando 1.")
                colunas=1

        for i in range(linhas):
                if i==0 or i==linhas-1:
                        print(f"{charCanto}{charHorizontal*(colunas-2)}{charCanto}")
                else:
                        print(f"{charVertical}{charVazio*(colunas-2)}{charVertical}")

linhas=int(input("Linhas: "))
colunas=int(input("Colunas: "))
desenharRetangulo(linhas,colunas)
