#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4 – Implemente um algoritmo que exiba na tela os números pares de 0 até um número
digitado pelo usuário. Dica: você pode utilizar o operador módulo (%) ou contar de 2 em 2.
"""

num=int(input("num: "))

for i in range(2, num+1, 2):
    print("i:", i)