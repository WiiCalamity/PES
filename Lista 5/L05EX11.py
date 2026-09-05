#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
11 – Crie um algoritmo com uma função que retorna um valor em reais escrito por
extenso. Por exemplo, caso seja passado “1.74” como parâmetro para a função, ela deve
retornar: um real e setenta e quatro centavos. Caso seja passado “3251.90”, deve retornar
“três mil duzentos e cinquenta e um reais e noventa centavos”.
"""
# Adaptado de:
# https://www.tutorialspoint.com/article/integer-to-english-words-in-python-programming
# Está com problemas no colocamento de alguns E's. Todo o intervalo [1000-9999] por exemplo.

milhar=["", "mil", "milhão(s)", "bilhão(s)"]

centena=["","cem","duzentos","trezentos","quatrocentos","quinhentos",
         "seiscentos","setecentos","oitocentos","novecentos"]

dezena=["","dez","vinte","trinta","quarenta","cinquenta","sessenta","setenta",
        "oitenta","noventa"]

simples=["","um","dois","três","quatro","cinco","seis","sete","oito","nove",
         "dez","onze","doze","treze","quatorze","quinze","dezesseis",
         "dezessete","dezoito","dezenove"]

def atribuirPalavra(n): # Dois mil e vinte e seis :(
        if n==0:
                return ""
        elif n<20:
                return simples[n]+" "
        elif n<100:
                return dezena[n//10]+" e "+atribuirPalavra(n%10)
        else:
                return centena[n//100]+" e "+atribuirPalavra(n%100)

def extenderNumero(num):
        if num==0: return "zero "
        resultado=""
        indice=0
        while num > 0:
                if num%1000!=0:
                        grupo=atribuirPalavra(num%1000)
                        escala=milhar[indice]
                        if escala:
                                grupo+=escala+" "
                        resultado=grupo+resultado
                indice+=1
                num//=1000
        if resultado.endswith(" e mil "):
                return resultado.removesuffix("e mil ")+"mil "
        if resultado.endswith(" e "):
                return resultado.removesuffix(" e ")+" "
        return resultado

valor=float(input("Valor (float): "))
reais=int(valor//1)
centavos=int(round(valor%1*100))
print(f"{extenderNumero(reais)}real(s) e {extenderNumero(centavos)}centavo(s)")
