#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4 – Faça um algoritmo que solicite ao usuário a quantidade de cidades que devem ser
cadastradas em uma lista. Em seguida, faça a leitura das cidades e imprima o resultado
na tela. Ao final, solicite ao usuário o nome de uma cidade para ser removida, faça a
remoção dela e imprima a lista novamente.
"""
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
cidades=[]
for i in range(int(input("Quantas cidades a cadastrar?? "))):
    print("Cidade",i+1,":",end=" ")
    cidades.append(input())

cls()
print("Cidades cadastradas:")
for i in cidades:
    print(">",i)

print(" ")
demolicao=input("Agora escolha uma cidade para DEMOLIR: ")
if demolicao in cidades:
    cidades.remove(demolicao)
    cls()
    print("Cidades cadastradas (após a demolição):")
    for i in cidades:
        print(">",i)
else:
    print("Essa cidade não está cadastrada!!")

