#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1 - Nossa necessidade é utilizar o recurso de liberação de portas dos Laboratórios de
Informática utilizando os dispositivos instalados em cada porta com fechadura eletrônica.
Para tal, desenvolveremos um sistema que identifique e autorize a entrada dos
professores já cadastrados no sistema de uso dos laboratórios.
Implemente um algoritmo de acordo com os requisitos listados abaixo:
A – Serão utilizados 6 laboratórios com as nomenclaturas Lab102, Lab103, Lab104,
Lab105, Lab106, Lab107.
B – Os professores autorizados de acordo com cada laboratório:
• Lab102 – Prof Ignácio, Prof Thiago Paes, Profa Ryan, Prof André, Profa
Fabiana;
• Lab103 – Prof Alberto;
• Lab104 – Prof Ryan, Prof Juliano, Prof Schalata, Prof André;
• Lab105 – Prof Ignácio, Prof Alberto, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab106 – Prof Schalata, Prof Ignácio, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab107 – Prof André, Prof Schalata, Prof Thiago Waltrik, Prof Thiago Paes, Prof
João Eduardo.
C – O programa deverá ter uma opção para cadastrar as listas por laboratório e a
lista de professores. Deverá ter opção de imprimir todos os cadastros de cada laboratório,
bem como a lista de professores com seu código de crachá.
D - O sistema de identificação de liberação da porta será feito através do fecho
eletrônico através do Crachá do Servidor, conforme a tabela de crachás abaixo. Vamos
simular que a autorização se dará por meio do teclado dos dispositivos na porta. Você
deve criar no seu programa, uma chamada que permita digitar o código do crachá.
Cadastro de Professores
001 – Prof Thiago Paes
002 – Prof Schalata
003 – Prof Ignácio
004 – Prof Ryan
005 – Prof André
006 – Profa Fabiana
007 – Prof Alberto
008 – Prof Juliano
009 – Prof Thiago Waltrik
010 – Prof João Eduardo
Observação: Faça com que seu algoritmo “converse” com o usuário e que seja claro
na troca de mensagens.
"""

professor={'001':"Paes",       '002':"Schalata", '003':"Ignácio",
           '004':"Ryan",       '005':"André",    '006':"Fabiana",
           '007':"Alberto",    '008':"Juliano",  '009':"Waltrik",
           '010':"João Eduardo"}

laboratorio={'Lab102':['001','003','004','005','006'],
             'Lab103':['007'],
             'Lab104':['002','004','005','008'],
             'Lab105':['001','003','007','009'],
             'Lab106':['001','002','003','009','010'],
             'Lab107':['001','002','005','009','010']}

import time
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def formatLabKey(labKey):
    labKey=labKey.capitalize()
    if labKey.isdigit():
        labKey="Lab"+labKey.zfill(3)
    return labKey

def findSearchedProfKey(searchedProfValue):
    for profKey,profValue in professor.items(): 
        if professor[profKey]==searchedProfValue:
            searchedProfKey=profKey
            return searchedProfKey
    else:
        print("Nome inválido. Tente 'listar professores'?")
        return "err"


def findSearchedProfValue(searchedProfKey):
    if not searchedProfKey in professor:
        print("Crachá inválido. Tente 'listar professores'?")
        return "err"
    searchedProfValue=professor[searchedProfKey]
    return searchedProfValue


def listarLabs():
    print("\nLaboratórios e permissões:")
    for labKey,labValue in laboratorio.items():
        print(f"{labKey} -",end=' ' if labValue else "\n")
        for profKey in labValue:
            if labValue[-1]==profKey: # Se está na última iteração...
                print(f"{professor[profKey]}")
            else:
                print(f"{professor[profKey]},",end=' ')


def listarProfs():
    print("\nProfessores cadastrados:")
    print("[crachá] - [nome]")
    for key,value in professor.items():
        print(f"{key} - {value}")
        

def pesquisarProfessor():
    searchedProf=input("Nome OU crachá: ")
    if searchedProf.isdigit():
        searchedProfKey=searchedProf
        searchedProfValue=findSearchedProfValue(searchedProfKey)
    else:
        searchedProfValue=searchedProf.capitalize()
        searchedProfKey=findSearchedProfKey(searchedProfValue)
    if searchedProfValue == "err" or searchedProfKey == "err":
        return
    print(f"\nResultado da busca\nNome: {searchedProfValue}\nCrachá: {searchedProfKey}")
    print("Labs:",end=' ')                                   ###########
    for labKey,labValue in laboratorio.items():              #    2    #
        for profKey in labValue: # labValue is a list  ###########
            if professor[profKey]==searchedProfValue:
                print(labKey,end=' ')
    print("")


def cadastrarLab():
    newLabKey=input("Nome do laboratório (e.g. 'Lab102', '104'): ")
    if newLabKey.isalpha():
        print("Nome inválido!")
        return
    newLabKey=formatLabKey(newLabKey)
    if newLabKey in laboratorio:
        print("Laboratório já existe!")
        return
    if not "Lab" in newLabKey:
        print("Nome inválido!")
        return
    laboratorio[newLabKey]=[]
    print("Laboratório cadastrado com sucesso.")


def cadastrarProf():
    newProfValue=input("Nome do professor: ").capitalize()
    if newProfValue in professor.values():
        print("Professor já existe!")
        return
    newProfKey=input("Crachá do professor (e.g. '011'): ").zfill(3)
    if newProfKey in professor:
        print("Professor já existe!")
        return
    professor[newProfKey]=newProfValue
    print("Professor cadastrado com sucesso.")


def adicionarPermissao():
    labKey=input("Laboratório a adicionar permissão (e.g. 'Lab102'): ")
    labKey=formatLabKey(labKey)
    if not labKey in laboratorio:
        print("Laboratório inválido. Tente 'listar laboratórios'?")
        return
    searchedProf=input("Nome OU crachá para adicionar: ")
    if searchedProf.isdigit():
        if not searchedProf in professor:
            print("Crachá inválido. Tente 'listar professores'?")
            return
        if searchedProf in laboratorio[labKey]:
            print("Crachá já está cadastrado no laboratório.")
            return
    else:
        searchedProf=findSearchedProfKey(searchedProf.capitalize())
    laboratorio[labKey].append(searchedProf)
    print("Permissão adicionada com sucesso!")


def removerLaboratorio():
    labKey=input("Laboratório a REMOVER (e.g. 'Lab102'): ")
    labKey=formatLabKey(labKey)
    if not labKey in laboratorio:
        print("Laboratório inválido. Tente 'listar laboratórios'?")
        return
    if input(f"Deseja realmente remover o {labKey}? (s/N): ") == "s":
        del laboratorio[labKey]
        print("Removido com sucesso.")
    else:
        print("Cancelado.")


def removerProfessor():
    searchedProf=input("Nome OU crachá do professor a REMOVER: ")
    if searchedProf.isdigit():
        searchedProfKey=searchedProf
        searchedProfValue=findSearchedProfValue(searchedProf)
    else:
        searchedProfKey=findSearchedProfKey(searchedProf.capitalize())
        searchedProfValue=searchedProf.capitalize()
    if input(f"Deseja realmente remover {searchedProfValue} de crachá {searchedProfKey}? (s/N): ") != "s":
        print("Cancelado.")
        return
    for labValue in laboratorio.values():
        for profKey in labValue:
            if profKey==searchedProfKey:
                labValue.remove(searchedProfKey)
    del professor[searchedProfKey]
    print("Removido com sucesso.")
    

def revogarPermissao():
    labKey=input("Laboratório a revogar uma permissão (e.g. 'Lab102'): ")
    labKey=formatLabKey(labKey)
    if not labKey in laboratorio:
        print("Laboratório inválido. Tente 'listar laboratórios'?")
        return
    searchedProf=input("Nome OU crachá para remover: ")
    if searchedProf.isdigit():
        if not searchedProf in professor:
            print("Crachá inválido. Tente 'listar professores'?")
            return
        if not searchedProf in laboratorio[labKey]:
            print("Crachá não está cadastrado no laboratório.")
    else:
        searchedProf=findSearchedProfKey(searchedProf.capitalize())
    for labValue in laboratorio.values():
        for profKey in labValue:
            if profKey==searchedProf:
                labValue.remove(searchedProf)
                break
    print("Permissão revogada com sucesso.")

def entrarEmLab():
    lab=input("Em qual laboratório você quer entrar? ")
    lab=formatLabKey(lab)
    if not lab in laboratorio:
        print("Oops! Laboratório inválido.")
        return
    loop="s"
    while loop!="n":
        cracha=input("Digite seu crachá na fechadura: ")
        nome=findSearchedProfValue(cracha)
        if not cracha in professor:
            print("Seu crachá não não existe!")
            return
        if cracha in laboratorio[lab]:
            time.sleep(1)
            print(f"Acesso permitido. Pode entrar, {nome} :)")
            time.sleep(2)
            return
        print("Acesso negado.")
        time.sleep(2)
        loop=input("Tentar novamente? (S/n): ")

while True:
    cls()
    print(" =================================== ")
    print("||  Sistema de Portas dos          ||")
    print("||  Laboratórios 🖥️                 ||")
    print("||   ---------------------------   ||")
    print("||  [1]  Listar laboratórios       ||")
    print("||  [2]  Listar professores        ||")
    print("||  [3]  Pesquisar professor       ||")
    print("||              ----               ||")
    print("||  [4]  Cadastrar laboratório     ||")
    print("||  [5]  Cadastrar professor       ||")
    print("||  [6]  Adicionar permissão       ||")
    print("||  [7]  Remover laboratório       ||")
    print("||  [8]  Remover professor         ||")
    print("||  [9]  Revogar permissão         ||")
    print("||              ----               ||")
    print("||  [10] Entrar em um laboratório  ||")
    print("||              ----               ||")
    print("||  [0]  Sair                      ||")
    print(" =================================== ")
    match input("Opção: "):
        case "1": # [1] Listar laboratórios
            listarLabs()
        case "2": # [2] Listar professores
            listarProfs()
        case "3": # [3] Pesquisar professor
            pesquisarProfessor()                
        case "4":
            cadastrarLab()
        case "5":
            cadastrarProf()
        case "6":
            adicionarPermissao()
        case "7":
            removerLaboratorio()
        case "8":
            removerProfessor()
        case "9":
            revogarPermissao()
        case "10":
            entrarEmLab()
        case "0":
            break
        case _:
            print("Opção inválida!! @w@")
    input("\nEnter para voltar...")
