#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4 – Solicite ao usuário um superpoder entre três opções: “força”, “velocidade” ou “voo”.
Use estruturas de decisão para exibir uma frase que diga qual super-herói você seria com
base na escolha:
• Se escolher “força”: exiba “Você seria o Hulk!”;
• Se escolher “velocidade”: exiba “Você seria o Flash!”;
• Se escolher “voo”: exiba “Você seria o Superman!”.
"""

# Eu decidi que a escolha seria por um número em vez
# de uma string porque imagino que seja mais conveniente
# para o usuário. Em outras palavras, é mais prático digitar
# "2" do que "Velocidade".
print("Escolha um superpoder (1-3):")
print("[1] Força")
print("[2] Velocidade")
print("[3] Voo")
superpoder = str(input())

if superpoder == "1":
    print("Você seria o Hulk!")
elif superpoder == "2":
    print("Você seria o Flash!")
elif superpoder == "3":
    print("Você seria o Superman!")
else:
    print("Erro! Opção inválida!")
    

