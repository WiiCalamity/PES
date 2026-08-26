#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:36:44 2026

@author: aluno
"""

"""
6 - Crie uma função chamada tempo_total que receba a quantidade de horas e minutos
que um jovem passou jogando videogame e retorne o total de minutos jogados. Peça ao
usuário para inserir as horas e minutos, e exiba o tempo total em minutos.
"""

def tempo_total(h,m):
        print("Tempo total, em minutos:",(h*60)+m)

horas=int(input("Horas: "))
minutos=int(input("Minutos: "))
tempo_total(horas,minutos)