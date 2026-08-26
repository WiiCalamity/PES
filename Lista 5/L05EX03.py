#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:16:21 2026

@author: aluno
"""

"""
3 – Codifique um programa com uma função para calcular o volume de um cilindro. Seu
programa principal deve solicitar a altura e o raio do cilindro em metros, chamar a função
e exibir o resultado na tela.
"""
PI=3.14

def calcularVolume(altura, raio):
        print(PI*raio**2*altura)

calcularVolume(float(input("Altura: ")), float(input("Raio: ")))