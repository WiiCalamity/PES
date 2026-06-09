#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3 – Faça um programa que exiba na tela a contagem iniciando no número 1 e indo até um
número informado pelo usuário. Considere que a contagem pode ser até um número
positivo ou até um número negativo.
"""

num=int(input("num: "))

if num > 0:
    for i in range(1, num+1):
        print("i:", i)
else:
    for i in range(1, num-1, -1):
        print("i:", i)