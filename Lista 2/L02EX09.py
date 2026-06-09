#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9 – Considere que você deseja fazer uma reserva mensal, em dinheiro, para a compra de
um determinado presente para você mesmo(a). Considere que todo mês você depositará,
em uma poupança no banco, um mesmo valor em reais. Faça um programa que leia o
valor que será depositado mensalmente e exiba na tela o valor acumulado mês a mês
durante 24 meses. Considere que a taxa de juros de uma poupança é 0,5% ao mês, que
a poupança não possui nenhum saldo inicial.
https://www.idinheiro.com.br/calculadoras/calculadora-juros-compostos/
"""
# Professor Waltrik eu não consegui fazer esse.
# Tentei de tudo, menos o cálculo correto.
# Em minha defesa, estamos na aula de programação e não finança.

investimento=float(100)
#investimento=float(input("Valor a investir a cada mês: "))
saldo=float(0)
periodo=int(2)
juros=float(1.01)
rendimento=float(0)
print("RENDIMENTO", rendimento)

for i in range(periodo):
    saldo=(saldo+investimento)*(juros)
    if i==0:
        rendimento=float(0)
    print("i:",i)
    print("rendimento:",rendimento)
    print("Saldo acumulado:",saldo)

print("Total:",saldo)