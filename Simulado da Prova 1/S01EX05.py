#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:32:39 2026

@author: aluno
"""

"""
5 – Desenvolva uma calculadora que leia dois números e apresente o seguinte menu:
• 1 – Adição;
• 2 – Subtração;
• 3 – Multiplicação;
• 4 – Divisão;
• 0 – Sair.
Realize a operação escolhida e exiba o resultado. Caso a opção seja inválida, apresente uma
mensagem de erro. O menu deve ser exibido novamente até que o usuário escolha a opção 0.
"""
import os
def clear():
        os.system("cls" if os.name=="nt" else "clear")

def prosseguir():
        input("\n<Enter> para continuar...")

def validarNumero(num):
        if not (num.removeprefix("-")).isdigit():
                print("Erro. Digite um número.")
                prosseguir()
                return True

def adicionar(a,b):
        print(f"{a} + {b} = {a+b}")

def subtrair(a,b):
        print(f"{a} - {b} = {a-b}")

def multiplicar(a,b):
        print(f"{a} * {b} = {a*b}")

def dividir(a,b):
        if b==0:
                print("Erro. Divisão por 0.")
                return
        print(f"{a} / {b} = {a/b}")

while True:
        clear()
        print("1 – Adição        ")
        print("2 – Subtração     ")
        print("3 – Multiplicação ")
        print("4 – Divisão       ")
        print("0 – Sair          ")
        opcao=input("Opção: ")
        if opcao=="0": break

        a=input("\nValor A: ")
        if validarNumero(a): continue
        a=float(a)
        
        b=input("Valor B: ")
        if validarNumero(b): continue
        b=float(b)
        match opcao:
                case "1":
                        adicionar(a,b)
                case "2":
                        subtrair(a,b)
                case "3":
                        multiplicar(a,b)
                case "4":
                        dividir(a,b)
                case _:
                        print("Opção inválida! @w@")
        prosseguir()