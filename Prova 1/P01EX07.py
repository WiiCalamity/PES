#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 7
"""
estacionamento=[]

import os
def clear():
        os.system("cls" if os.name=="nt" else "clear")

def cadastrar():
        estacionamento.append(input("Nova placa: ").upper())

def excluir():
        placa=input("Placa a remover: ").upper()
        if not placa in estacionamento:
                print("Placa não encontrada!")
                return
        print(f"A placa <{placa}> foi removida.")
        estacionamento.remove(placa)

def listar():
        print("\nPLACAS CADASTRADAS")
        if len(estacionamento)==0:
                print("O estacionamento está vazio!")
                return
        for index in range(len(estacionamento)):
                print(f"[{index}] {estacionamento[index]}")

while True:
        clear()
        print("1 - Cadastrar ")
        print("2 - Excluir   ")
        print("3 - Listar    ")
        print("0 - Sair      ")
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
                        print("Opção inválida!! @w@")
        input("\n<Enter> para continuar...")