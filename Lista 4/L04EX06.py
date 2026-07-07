#!/usr/bin/env python3
"""
6 – Elabore um programa que funcionará como um cadastro notas de um estudante. Seu
programa deve permitir que notas sejam cadastradas ou removidas (através do seu
índice, pois podem haver notas repetidas), conforme a solicitação do usuário. Também
deve ser possível exibir a lista com todas as notas cadastradas, porém, o programa deve
avisar o usuário caso a lista esteja vazia. O programa também deve ter uma opção para
calcular a média do aluno e exibir sua situação (aprovado se média for maior ou igual a 6
e reprovado, caso contrário). Crie um menu, conforme abaixo, para permitir a interação
com o seu programa:
Notas
-----
1 - Cadastrar
2 - Excluir
3 - Listar
4 - Calcular média
0 - Sair
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
    else:
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

while True:
    cls()
    print(" ------------------- ")
    print("| Notas do Discente |")
    print(" ------------------- ")
    print("| [1] Cadastrar     |")
    print("| [2] Excluir       |")
    print("| [3] Listar        |")
    print("| [4] Situação      |")
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
        case "0":
            break
        case _:
            print("Opção inválida! @w@")
    input("Enter para voltar...")
