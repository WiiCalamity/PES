#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 6
"""

def distancia_total(quilometros,metros):
        return quilometros*1000+metros

km=float(input("Quantos QUILÔMETROS ele percorreu?: "))
m=float(input("Quantos METROS ele percorreu?: "))

distancia=distancia_total(km,m)
plural="" if abs(distancia)==1 else "s" # Desnecessário?

print(f"\nTotal percorrido: {distancia} metro{plural}")