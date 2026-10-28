#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 5
"""

num=int(input("Número: "))
passo=1 if num>=1 else -1
for i in range(1,num+passo,passo):
        print(i)