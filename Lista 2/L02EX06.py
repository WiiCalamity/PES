#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6 - Modifique o programa anterior de forma que o usuário também digite o início e o fim da
tabuada, em vez de começar iniciar no 1 e terminar no 10.
"""
num=int(input("num: "))
inicio=int(input("inicio: "))
fim=int(input("fim: "))

# Como controlar melhor a saída do print? Tem um espaço depois de fim.
print("Tabuada do",num,"(de",inicio,"até",fim,"):")
for i in range(inicio, fim):
    print(num, "x", i, "=", num*i)