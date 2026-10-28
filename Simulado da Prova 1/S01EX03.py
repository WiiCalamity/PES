#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 08:45:49 2026

@author: aluno
"""

"""
3 – Faça um algoritmo que leia o preço de um produto e a quantidade comprada. Calcule o total
da compra e, caso ele seja maior ou igual a R$ 100,00, aplique um desconto de 10%. Ao final,
exiba o valor a ser pago.
"""
preco=float(input("Qual é o preço desse produto?: "))
unidades=float(input("Quantas unidades você comprou?: "))
total=round(preco*unidades)
desconto=0.9

print("Valor a pagar:")
print("R$",total*desconto if total>=100 else total)
