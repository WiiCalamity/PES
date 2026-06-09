#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2 - Faça um programa para escrever a contagem regressiva do lançamento
de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.
"""

import time
import os
def cls(): # https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')

cls()
print("Contagem regressiva!")
time.sleep(2)
cls()
for i in range(10,-1, -1):
    print(i)
    time.sleep(1)
    cls()
print("Fogo!")
time.sleep(1)