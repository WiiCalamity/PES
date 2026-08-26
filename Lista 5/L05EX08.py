#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
8 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada no formato
de string, por exemplo: “15:31”. Deve haver pelo menos duas funções: uma para fazer a
conversão e uma para imprimir a saída. A função que faz a conversão deve ter duas
saídas: uma com a hora convertida e outra com “A”, caso seja “A.M.” e “P”, caso seja
“P.M.”. Inclua um loop que permita que o usuário repita esse cálculo para novos valores
de entrada todas as vezes que desejar.
"""

def converterNotacao(horario):
        # Grande bagunça. Sujo. Espirra lama.
        horario=horario.split(":")
        hora=int(horario[0])
        afixo="AM"
        if hora==0:
                hora=12
        elif hora>=12:
                afixo="PM"
                if hora!=12:
                        hora-=12
        horario[0]=str(hora)

        horario=":".join(horario)
        horario=horario+" "+afixo
        return horario,afixo.replace("M","")

def imprimirTupla(tupla):
        for item in tupla:
                print(item)

while True:
        horario=input("Horário (hh:mm) (0 para parar): ")
        if horario=="0": break
        print("---")
        imprimirTupla(converterNotacao(horario))
        print()
