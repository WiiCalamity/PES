#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10 - Construa uma função que receba uma string como parâmetro e devolva (retorne)
outra string com os caracteres embaralhados. Por exemplo: se função receber a palavra
python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma
aleatória. Padronize sua função que todos os caracteres sejam devolvidos em caixa alta
ou caixa baixa, independentemente de como foram digitados. Para lhe auxiliar nesse
exercício, pesquisa sobre a biblioteca Random do Python.
"""
import random

def shuffleString(myString):
        slicedString=list(myString.lower())
        random.shuffle(slicedString)
        shuffledString="".join(slicedString)
        return shuffledString

print("0 para interromper.")
while True:
        myString=input("String: ")
        if myString=="0": break
        print(shuffleString(myString))
        print()
