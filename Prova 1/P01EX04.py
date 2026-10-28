#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 4
"""

num=int(input("Número: "))
print(f"\nTABUADA DO NÚMERO {num}")
for multiplicador in range(1,11):
        print(f"{num} x {multiplicador} = {num*multiplicador}")
