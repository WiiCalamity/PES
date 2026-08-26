#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9 - Construa uma função que receba uma data no formato DD/MM/AAAA (string) e
devolva uma string com a data por extenso, por exemplo: “doze de agosto de dois mil e
vinte e quatro”. Seu algoritmo deve ser capaz de converter datas entre os anos de 2000 e
2100.
"""
mes={"01":"Janeiro",  "02":"Fevereiro", "03":"Março",    "04":"Abril",
     "05":"Maio",     "06":"Junho",     "07":"Julho",    "08":"Agosto",
     "09":"Setembro", "10":"Outubro",   "11":"Novembro", "12":"Dezembro",
     "0":""}

dezena={"1":"dez", "2":"vinte", "3":"trinta", "4":"quarenta",
        "5":"cinquenta", "6":"sessenta", "7":"setenta", "8":"oitenta",
        "9":"noventa", "100":"cem", "0":""}

unidade={"1":"um",         "2":"dois",      "3":"três",      "4":"quatro",
         "5":"cinco",      "6":"seis",      "7":"sete",      "8":"oito",
         "9":"nove",       "10":"dez",      "11":"onze",     "12":"doze",
         "13":"treze",     "14":"quatorze", "15":"quinze",   "16":"dezesseis",
         "17":"dezessete", "18":"dezoito",  "19":"dezenove", "100":"cem",
         "0":""}

def extenderData(date):
        day=int(date[0]+date[1]) # e.g. [12]/04/2007
        month=date[3]+date[4] # e.g. 12/[04]/2007
        year=int(date[7]+date[8]+date[9]) # e.g. 12/04/2[007]

        if day<=19:
                longDay=unidade[str(day)].title()
        else:
                longDay=f"{dezena[date[0]].title()} e {unidade[date[1]]}"
        longYear="dois mil "
        if year<=19 and year>=1 or year==100:
                longYear+=f"e {unidade[str(year)]}"
        elif year!=0:
                longYear+=f"e {dezena[date[8]]} e {unidade[date[9]]}"
        longDate=f"{longDay} de {mes[month]} de {longYear}"
        return longDate

data=input("Digite uma data (dd/mm/aaaa): ")
if int(data[0]+data[1])>31 or int(data[3]+data[4])>12:
        print("Oops! Data inválida!")
else:
        print(extenderData(data))
