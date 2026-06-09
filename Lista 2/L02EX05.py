#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5 – Faça um programa que exiba na tela a tabuada de um número informado pelo
usuário. Vamos supor que o número informado seja o 2, então o programa deve exibir o
seguinte resultado na tela:
"""

num=int(input("num: "))

print("Tabuada do",num,":")
for i in range(1, 11):
    print(num, "x", i, "=", num*i)