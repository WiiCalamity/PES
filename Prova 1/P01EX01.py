#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 1
"""

nome=input("Nome: ")
senha=input("Senha: ")
if nome=="admin" and senha=="12345":
        print("Login bem-sucedido")
else:
        print("Nome de usuário ou senha incorretos")
