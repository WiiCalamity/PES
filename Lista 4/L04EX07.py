#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7 – Utilizando como base o exercício 6, implemente dois novos recursos: um para
informar a maior nota cadastrada e outro para informar a menor nota cadastrada. Caso
não existam notas cadastradas, seu programa deve informar “Erro: não há notas
cadastradas”. Crie um menu, conforme abaixo, para permitir a interação com o seu
programa:
Notas
-----
1 - Cadastrar
2 - Excluir
3 - Listar
4 - Calcular média
5 – Mostrar maior nota
6 – Mostrar menor nota
0 - Sair
Opção:
"""

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

notas=[]

def cadastrar():
    opcao=float(input("Cadastrar nota: "))
    if opcao>=0 and opcao<=10:
        notas.append(opcao)
        print("Sucesso!")
    else:
        print("Erro! Fora do intervalo!")

def excluir():
    cls()
    if len(notas)==0:
        print("Nenhuma nota cadastrada.")
        print(" ")
        return
    print("Notas do discente:")
    for i in range(len(notas)):
        print("Índice",i,"->",notas[i])
    print(" ")
    opcao=int(input("Digite o ÍNDICE da nota para excluir: "))
    opcao=notas[opcao]
    if opcao in notas:
        notas.remove(opcao)
    else:
        print("Erro! Fora do índice!")
            

def listar():
    cls()
    print("Notas do discente: " if len(notas)!=0 else "Nenhuma nota cadastrada.")
    for i in range(len(notas)):
        print(notas[i])
    print(" ")

def situacao():
    media=float(0)
    for i in range(len(notas)):
        media+=notas[i]
    media=media/len(notas)
    print("Média: %.1f" % media)
    print("Situação: Aprovado!" if media>=6 else "Situação: Reprovado.")
    
def maiorNota():
    if len(notas)==0:
        print("Nenhuma nota cadastrada.")
        print(" ")
        return
    opcao=float(0)
    for i in notas:
        if i > opcao:
            opcao=i
    print("A maior nota é:",opcao)
    
def menorNota():
    if len(notas)==0:
        print("Nenhuma nota cadastrada.")
        print(" ")
        return
    opcao=float(10)
    for i in notas:
        if i < opcao:
            opcao=i
    print("A menor nota é:",opcao)
        

while True:
    cls()
    print(" ------------------- ")
    print("| Notas do Discente |")
    print(" ------------------- ")
    print("| [1] Cadastrar     |")
    print("| [2] Excluir       |")
    print("| [3] Listar notas  |")
    print("| [4] Situação      |")
    print("| [5] Maior nota    |")
    print("| [6] Menor nota    |")
    print("| [0] Sair          |")
    print(" ------------------- ")

    opcao=input("Opção: ")
    match opcao:
        case "1":
            cadastrar()
        case "2":
            excluir()
        case "3":
            listar()
        case "4":
            situacao()
        case "5":
            maiorNota()
        case "6":
            menorNota()
        case "0":
            break
        case _:
            print("Opção inválida! @w@")
    input("Enter para voltar...")
