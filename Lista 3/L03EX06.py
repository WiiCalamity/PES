#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6 – Adicione ao programa da questão anterior, uma opção para excluir o cadastro
baseado no código da pessoa. Adicione também uma opção para pesquisar que utilizará
o nome da pessoa como critério de busca.
"""

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def cadastrar():
    for i in range(len(nomes)):
        if nomes[i]=="null":
            nomes.insert(i, input("Nome: "))
            idades.insert(i, input("Idade: "))
            alturas.insert(i, input("Altura: "))
            pesos.insert(i, input("Peso: "))
            print("Cadastrado com sucesso!")
            
def excluir():
    for i in range(len(nomes)-1):
        print(nomes[i])
        
    opcao=input("Digite o nome da pessoa a excluir: ")
    for i in range(len(nomes)-1):
        if nomes[i]==opcao:
            break
    else:
        print("Erro! Nome não encontrado!")
        return
    
    for i in range(len(nomes)-1):
        # Não sei como posso fazer isso de forma mais eficiente
        aux=nomes[i]
        nomes[i]=nomes[i+1]
        nomes[i+1]=aux
        
        aux=idades[i]
        idades[i]=idades[i+1]
        idades[i+1]=aux
        
        aux=alturas[i]
        alturas[i]=alturas[i+1]
        alturas[i+1]=aux
        
        aux=pesos[i]
        pesos[i]=pesos[i+1]
        pesos[i+1]=aux

    del nomes[-1]
    del idades[-1]
    del alturas[-1]
    del pesos[-1]
    print("Removido com sucesso!")
    
def excluirPorID():
    for i in range(len(nomes)-1):
        print("ID",i,"-",nomes[i])
        
    i=input("Digite o ID da pessoa a excluir: ")
    for i in range(len(nomes)-1):
        # Não sei como posso fazer isso de forma mais eficiente
        aux=nomes[i]
        nomes[i]=nomes[i+1]
        nomes[i+1]=aux
        
        aux=idades[i]
        idades[i]=idades[i+1]
        idades[i+1]=aux
        
        aux=alturas[i]
        alturas[i]=alturas[i+1]
        alturas[i+1]=aux
        
        aux=pesos[i]
        pesos[i]=pesos[i+1]
        pesos[i+1]=aux

    del nomes[-1]
    del idades[-1]
    del alturas[-1]
    del pesos[-1]
    print("Removido com sucesso!")
    
def alterar():
    for i in range(len(nomes)-1):
        print(nomes[i])
        
    opcao=input("Digite o nome da pessoa a alterar: ")
    for i in range(len(nomes)-1):
        if nomes[i]==opcao:
            break
    else:
        print("Erro! Nome não encontrado!")
        return
    
    idades[i]=input("Idade: ")
    alturas[i]=input("Alturas: ")
    pesos[i]=input("Pesos: ")
    print("Alterado com sucesso!")
            
def listar():
    cls()
    print("Pessoas cadastradas: " if nomes[0]!="null" else "Ninguém cadastrado.")
    print(" ")
    for i in range(len(nomes)-1):
        print(nomes[i])
        print("Idade:",idades[i])
        print("Altura:",alturas[i])
        print("Peso:",pesos[i])
        print(" ")
        
def pesquisar():
    cls()
    for i in range(len(nomes)-1):
        print(nomes[i])
    
    opcao=input("Nome a pesquisar: ")
    for i in range(len(nomes)-1):
        if nomes[i]==opcao:
            break
    else:
        print("Erro! Nome não encontrado!")
        return
    
    print("Idade:",idades[i])
    print("Altura:",alturas[i])
    print("Peso:",pesos[i])
    print(" ")
    

nomes=["null"]
idades=["null"]
alturas=["null"]
pesos=["null"]
while True:
    cls()
    print("..........................")
    print(":   Medidas corpóreas    :")
    print(":........................:")
    print(": [1] Cadastrar pessoa   :")
    print(": [2] Excluir por nome   :")
    print(": [3] Excluir por ID     :")
    print(": [4] Alterar medidas    :")
    print(": [5] Listar tudo        :")
    print(": [6] Pesquisar por nome :")
    print(": [0] Sair               :")
    print(":........................:")
    opcao=str(input("Opção: "))
    
    match opcao:
        case "1":
            cadastrar()
        case "2":
            excluir()
        case "3":
            excluirPorID()
        case "4":
            alterar()
        case "5":
            listar()
        case "6":
            pesquisar()
        case "0":
            break
        case _:
            print("Opção inválida!! @w@")
        
    input("Enter para voltar...")