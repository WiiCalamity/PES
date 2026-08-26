#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:30:54 2026

@author: aluno
"""

"""
5 – Programe um algoritmo com mais algumas funções úteis para a manipulação de listas
numéricas:
a) uma função que receba uma lista e retorne True, caso esteja vazia, ou False, caso
possua um ou mais elementos;
b) uma função que receba uma lista e retorne o maior valor;
c) uma função que receba uma lista e retorne o menor valor;
d) uma função que receba uma lista e retorne o valor médio.
As funções dos itens b, c e d devem retornar -1 caso a lista esteja vazia. No seu
programa principal, crie duas listas (uma vazia e outra com alguns elementos) e teste
(comprove) o funcionamento de cada uma das funções.
"""

teste1=[]
teste2=[5,8,99,-14,13]
teste3=[16,"string","abc"]

def listaEhVazia(lista):
        return True if len(lista)==0 else False

def buscarMaiorValor(lista):
        if len(lista)==0: return -1
        maior=lista[0]
        for i in range(len(lista)):
                if lista[i] > maior:
                        maior=lista[i]
        return maior

def buscarMenorValor(lista):
        if len(lista)==0: return -1
        menor=lista[0]
        for i in range(len(lista)):
                if lista[i] < menor:
                        menor=lista[i]
        return menor

def buscarMedia(lista):
        if len(lista)==0: return -1
        numDeElementos=len(lista)
        soma=float(0)
        for i in range(numDeElementos):
                soma+=lista[i]
        media=soma/numDeElementos
        return media


print("teste1 está vazio:",listaEhVazia(teste1))
print("teste3 está vazio:",listaEhVazia(teste3))
print("O MENOR valor de teste2 é:", buscarMenorValor(teste2))
print("O MAIOR valor de teste2 é:", buscarMaiorValor(teste2))
print("A MÉDIA de teste2 é:", buscarMedia(teste2))
