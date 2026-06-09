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

investimento=float(input("Valor a investir a cada mês: "))
saldo=float(0)
periodo=int(24)
juros=float(0.005)

for i in range(periodo):
    saldo=saldo+(saldo*juros)+investimento

print("Saldo final: R$ %.2f" % saldo)