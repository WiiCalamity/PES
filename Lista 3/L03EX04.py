#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4 - Codifique um programa que funcionará como um cadastro de placas de automóveis de
um estacionamento (para até 15 automóveis). O cadastro deve ser realizado em uma
lista. Seu programa deve ter um menu com a seguinte estrutura:
1 – Cadastrar
2 - Excluir
3 - Listar
0 - Sair
A opção Cadastrar deve verificar se há espaço disponível na lista para o cadastro. Se
houver, deve proceder o cadastro. Se não, deve informar o usuário que não há espaço
disponível. A opção Excluir deve perguntar ao usuário qual placa deve ser excluída (pelo
nome da placa) e informar se houve sucesso ou falha. Já a opção listar deve
simplesmente listar todas as placas cadastradas. Dica: utilize um valor padrão para definir
um espaço vago na lista.
"""
import os
def cls(): # https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')

def cadastrar():
    for i in range(15):
        if placas[i]=="Livre!":
            placas[i]=str(input("Digite a placa: "))
            print("A placa",placas[i],"foi cadastrada com sucesso!")
            break
    else:
        print("Erro! Não há espaço no estacionamento!")
            
def excluir():
    cls()
    for i in range(15):
        print("[",i,"] -",placas[i])
    opcao=int(input("Digite a placa a excluir (0-14): "))
    if placas[opcao]!="Livre!":
        print("A placa",placas[opcao],"foi excluída.")
        placas[opcao]="Livre!"
    else:
        print("O espaço já está livre... mas tudo bem.")


def listar():
    cls()
    for i in range(15):
        print("ID",i,":",placas[i])
        

placas=["Livre!"]*15
while True:
    cls()
    print("#######################")
    print("#   Estacionamento    #")
    print("#######################")
    print("# [1] Cadastrar placa #")
    print("# [2] Excluir placa   #")
    print("# [3] Listar placas   #")
    print("# [4] Sair            #")
    print("#######################")
    print("Opção:", end=" ")
    opcao=int(input())
    
    match opcao:
        case 1:
            cadastrar()
        case 2:
            excluir()
        case 3:
            listar()
        case 4:
            break
        case _:
            print("Opção inválida!!")
    input("Enter para voltar...")
    