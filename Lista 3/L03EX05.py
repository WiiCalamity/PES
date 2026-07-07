#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5 – Faça um programa que funcionará como um cadastro de medidas corpóreas. Seu
programa deve ter uma estrutura que seja capaz de armazenar as seguintes informações
sobre cada pessoa: nome, idade, altura e peso (cada uma em uma lista). A interação deve
ser através de um menu com as seguintes opções:
1 – Cadastrar
2 - Excluir
3 - Alterar
4 - Listar
0 - Sair
A opção Cadastrar deve solicitar as informações da pessoa a ser cadastrada. Já a opção
excluir, deve solicitar o nome de quem se deseja excluir o cadastro. A opção Alterar deve
solicitar o nome da pessoa a ser alterado e, em seguida, solicitar as novas informações
da pessoa (idade, altura e peso). A opção Listar deve apresentar todas as informações
das pessoas cadastradas.
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

nomes=["null"]
idades=["null"]
alturas=["null"]
pesos=["null"]
while True:
    cls()
    print("........................")
    print(":  Medidas corpóreas   :")
    print(":......................:")
    print(": [1] Cadastrar pessoa :")
    print(": [2] Excluir pessoa   :")
    print(": [3] Alterar medidas  :")
    print(": [4] Listar tudo      :")
    print(": [0] Sair             :")
    print(":......................:")
    opcao=str(input("Opção: "))
    
    match opcao:
        case "1":
            cadastrar()
        case "2":
            excluir()
        case "3":
            alterar()
        case "4":
            listar()
        case "0":
            break
        case _:
            print("Opção inválida!! @w@")
        
    input("Enter para voltar...")