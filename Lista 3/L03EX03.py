#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3 – Faça um programa que funcionará como um cadastro de códigos de produtos de uma
loja de roupas. O cadastro deve ser realizado em uma lista com até 10 códigos. Inicialize
os elementos da lista com -1, este valor indicará que o elemento está vago para o
cadastro. Seu programa deve ter um menu com uma opção para cadastrar um novo
código (apenas um por vez) e para listar os todos códigos cadastrados (não devem ser
listados códigos não cadastrados). Deve-se também informar se houve sucesso ou falha
na hora de cadastrar um novo código e também não deve ser possível cadastrar um
produto com o código -1. No momento do cadastro, não deve ser informado o valor do
índice, esse deve ser “calculado” automaticamente. Veja como deve ser criado o menu:
    
Menu
----
1 – Cadastrar
2 – Listar todos
0 – Sair
"""

import os
def cls(): # https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')

def cadastrar_codigo():
    for i in range(11):
        if i==10: # Se o laço detectou que está todo preenchido
            print("Erro! Todos os códigos já estão preenchidos!")
        elif codigos[i]==-1:
            codigos[i]=int(input("Digite o código: "))
            if codigos[i]==-1:
                print("Erro! O código não pode ser -1!")
            else:
                print("Código cadastrado com sucesso!")
            break

def listar_codigos():
    listaVazia=bool("Sim, está vazia")
    for i in range(10):
        if codigos[i] != -1:
            print("Produto ",i+1,": código",codigos[i])
            listaVazia=bool()
    if listaVazia:
        print("A lista está vazia. Vá cadastrar um código.")

codigos=[-1]*10
while True:
    cls()
    print("#-------------------------#")
    print("|          *Menu          |")
    print("#-------------------------#")
    print("| [1] Cadastrar um código |")
    print("| [2] Listar códigos      |")
    print("| [0] Escapar             |") # Haha
    print("#-------------------------#")
    print("Opção:", end=" ")
    opcao=int(input())
    
    match opcao:
        case 1:
            cadastrar_codigo()
        case 2:
            listar_codigos()
        case 0:
            break
        case _:
            print("Opção inválida!!")
    
    input("Enter para voltar...")

    
