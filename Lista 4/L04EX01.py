#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1 – Implemente um algoritmo com uma lista de nomes de bairros de Garopaba. O nome
do primeiro bairro deve ser adicionado manualmente (no próprio programa), em seguida,
deve ser solicitado ao usuário para cadastrar o nome de mais 5 bairros. Ao final, o
programa deve exibir o nome de todos os bairros cadastrados na tela.
"""

bairros=[]
bairros.append("Campo D'una")
for i in range(5):
    bairros.append(input("Adicionar novo bairro: "))

print(" ")
print("Bairros cadastrados:")
for i in bairros:
    print(">",i)