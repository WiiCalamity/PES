#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
11 – Faça um programa para controlar o caixa de uma cantina. Seu programa deve
solicitar ao usuário o código do produto pedido e a quantidade comprada. Suponha que
para cada compra, apenas um tipo de produto possa ser comprado. O programa deve ser
interrompido caso o usuário digite 0. Para cada compra, seu programa deve exibir na tela
o nome do produto comprado e o valor total da compra. Ao final do programa, deve exibir
o valor total acumulado no caixa.
"""
# Professor Waltrik eu achei as intruções ambíguas. Fiz o que entendi (e mais).
import time
import os
def cls(): # https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')

id=str()
nomeDoProduto=str()
valor=float()
total=float(0)
quantidade=int()

while True:
    cls()
    print("+----+------------------+---------+")
    print("| ID | Produto          | Valor   |")
    print("+----+------------------+---------+")
    print("|  1 | Suco             | R$ 6,00 |")
    print("|  2 | Pão de queijo    | R$ 3,00 |")
    print("|  3 | Pastel           | R$ 7,00 |")
    print("|  4 | Salada de frutas | R$ 9,00 |")
    print("|  5 | Café com leite   | R$ 3,50 |")
    print("|  6 | Cappuccino       | R$ 4,50 |")
    print("|  7 | Iogurte          | R$ 6,50 |")
    print("|  8 | Água             | R$ 2,50 |")
    print("+----+------------------+---------+")
    print(" ")
    time.sleep(0.2)

    id=str(input("ID do produto: "))
    match id: #https://www.geeksforgeeks.org/python/python-match-case-statement/
        case "1":
            nomeDoProduto="Suco"
            valor=6
        case "2":
            nomeDoProduto="Pão de queijo"
            valor=3
        case "3":
            nomeDoProduto="Pastel"
            valor=7
        case "4":
            nomeDoProduto="Salada de frutas"
            valor=9
        case "5":
            nomeDoProduto="Café com leite"
            valor=3.5
        case "6":
            nomeDoProduto="Cappuccino"
            valor=4.5
        case "7":
            nomeDoProduto="Iogurte"
            valor=6.5
        case "8":
            nomeDoProduto="Água"
            valor=2.5
        case "0": 
            break
        case _:
            print("Opção inválida!")
            break
    
    print("Você escolheu:",nomeDoProduto)
    quantidade=int(input("Quantas unidades? "))
    if quantidade==0:
        break
    
    print(" ")
    print("Valor desta compra: R$",valor*quantidade)
    print(" ")
    total+=valor*quantidade
    print("Total: R$",total)
    print(" ")
    time.sleep(2)

print("Valor total: R$",total)
