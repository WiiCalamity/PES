#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:59:07 2026

@author: aluno
"""

"""
11 – Crie um algoritmo com uma função que retorna um valor em reais escrito por
extenso. Por exemplo, caso seja passado “1.74” como parâmetro para a função, ela deve
retornar: um real e setenta e quatro centavos. Caso seja passado “3251.90”, deve retornar
“três mil duzentos e cinquenta e um reais e noventa centavos”.
"""

milhar=["", "mil", "milhão(s)", "bilhão(s)"]

centena=["","cem","duzentos","trezentos","quatrocentos","quinhentos",
         "seiscentos","setecentos","oitocentos","novecentos"]

dezena=["","dez","vinte","trinta","quarenta","cinquenta","sessenta","setenta",
        "oitenta","noventa"]

simples=["","um","dois","três","quatro","cinco","seis","sete","oito","nove",
         "dez","onze","doze","treze","quatorze","quinze","dezesseis",
         "dezessete","dezoito","dezenove"]

def atribuirPalavra(num):
        if num==0:
                return ""
        elif num<20:
                return simples[num]
        elif num<100:
                return dezena[num//10]+atribuirPalavra(num%10)
        else:
                return centena[num//100]+atribuirPalavra(num%100)

def fatiarNumero(num: float):
        plural=False
        while num>0:
                
                
