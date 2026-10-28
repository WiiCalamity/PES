#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 3
"""

meuDicio={"python":"uma linguagem de programação versátil e abrangente popular no mundo inteiro."}

def cadastrarPalavra():
        key=input("Cadastrar palavra: ")
        value=input("Cadastrar significado: ")
        meuDicio[key]=value


num=int(input("Quantas palavras você quer cadastrar?: "))
for _ in range(num):
        cadastrarPalavra()

print("---\nPALAVRAS CADASTRADAS\n")
for key,value in meuDicio.items():
        print(f">{key}<\n{value}\n")
