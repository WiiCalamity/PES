#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5 – Crie um programa que funcionará como um cadastro de Amigos Próximos no
Instagram. Seu programa deve permitir que amigos sejam cadastrados ou removidos,
conforme a solicitação do usuário. Também deve ser possível exibir a lista com todos os
amigos cadastrados, porém, o programa deve avisar o usuário caso a lista esteja vazia.
Crie um menu, conforme abaixo, para permitir a interação com o seu programa:
Amigos Próximos
---------------
1 - Cadastrar
2 - Excluir
3 - Listar
0 - Sair
"""
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

amigos=[]

def cadastrar():
    opcao=input("Cadastrar novo amigo próximo: ")
    if not opcao in amigos:
        amigos.append(opcao)
        print("Sucesso!")
    else:
        print("Esse amigo já existe! Use outro nome!")

def excluir():
    cls()
    if len(amigos)==0:
        print("Você não tem amigos :P")
        print(" ")
        return
    else:
        print("Seus amigos próximos:")
        for i in range(len(amigos)):
            print(i+1,"-",amigos[i])
        print(" ")
        opcao=input("Digite o nome do amigo para excluir: ")
        if opcao in amigos:
            amigos.remove(opcao)
            print("Sucesso!")
        else:
            print("Erro! Amigo não encontrado!")

def listar():
    cls()
    print("Seus amigos próximos: " if len(amigos)!=0 else "Você não tem amigos :P")
    for i in range(len(amigos)):
        print(i+1,"-",amigos[i])
    print(" ")

while True:
    cls()
    print(" -------------------- ")
    print("| Amigos Próximos 👥 |")
    print(" -------------------- ")
    print("| [1] Cadastrar      |")
    print("| [2] Excluir        |")
    print("| [3] Listar         |")
    print("| [0] Sair           |") 
    print(" -------------------- ")
    
    opcao=input("Opção: ")
    match opcao:
        case "1":
            cadastrar()
        case "2":
            excluir()
        case "3":
            listar()
        case "0":
            break
        case _:
            print("Opção inválida! @w@")
    input("Enter para voltar...")