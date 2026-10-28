#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 08:28:38 2026

@author: aluno
"""

"""
1 – Desenvolva um algoritmo que leia um ano e informe se ele é bissexto. Um ano é bissexto quando
é divisível por 400 ou quando é divisível por 4, mas não é divisível por 100.
"""
ano=int(input("Ano: "))
print("É bissexto" if ano%4==0 and ano%100!=100 else "Não é bissexto :(")
