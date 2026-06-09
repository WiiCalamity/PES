#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5 - Determinador de Temperatura: Solicite a temperatura do dia (em ºC). Dependendo da
temperatura informada, exiba a mensagem apropriada conforme abaixo:
• Menos de 10 ºC: “Está muito frio! Use roupas quentes.”;
• De 10 ºC até 20 ºC (inclusive): “Frio. Vista-se bem!”;
• Acima de 20 ºC até 25 ºC (inclusive): “Temperatura agradável.”;
• Acima de 25 ºC até 30 ºC (inclusive): “Está ficando quente!”;
• Acima de 30 ºC: “Está muito quente! Fique hidratado.”.
Obs.: o algoritmo deve aceitar temperaturas com valores decimais (ex.: 20,5 ºC, 25,8 ºC
etc.).
"""

temperatura = float(input("Qual a temperatura hoje? :) "))

if temperatura < 10:
    print("Está muito frio! USe roupas quentes.")
elif temperatura <= 20:
    print("Frio. Vista-se bem!")
elif temperatura <= 25:
    print("Temperatura agradável.")
elif temperatura <= 30:
    print("Está ficando quente!")
else:
    print("Está muito quente! Fique hidratado.")


