#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:03:59 2026

@author: aluno
"""

"""
4 – Crie um dicionário de palavras da língua portuguesa, utilizando as palavras como chaves e seus
significados como valores. Inicie com:
"apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma
situação difícil, ou usar de meios extremos e exagerados"
Solicite ao usuário mais 4 palavras e seus respectivos significados. Em seguida, peça uma
palavra para consulta e exiba seu significado. Caso ela não esteja cadastrada, informe “Palavra
não encontrada”.
"""
import os
def clear():
        os.system("cls" if os.name=="nt" else "clear")

meuDicio={"apelar":"recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação " +
          "difícil, ou usar de meios extremos e exagerados"}

def consultarDicionario(key):
        if not key in meuDicio:
                print("Palavra não encontrada.\n")
                return
        print(f"{key.upper()}\n{meuDicio[key]}\n")

def criarDefinicao():
        key=input("Palavra: ").lower()
        value=input("Definição: ")
        meuDicio[key]=value

#for i in range(4):
#        print(f"Criar uma definição ({i+1})")
#        criarDefinicao()

while True:
        clear()
        key=input("Consultar dicionário (0=parar): ").lower()
        if key=="0": break
        consultarDicionario(key)