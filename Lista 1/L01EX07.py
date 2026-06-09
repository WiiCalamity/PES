#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7 - Qual é o seu Signo? Solicite o dia e o mês de nascimento do usuário. Com base
nesses valores, use condicionais para determinar o signo.
"""
import time
import os
def cls(): # https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')

cls()
print("Qual é o seu signo? Eu descobrirei o seu segredo inato!")
time.sleep(2)

dia=int(input("Qual é o dia de seu nascimento? (01-31): "))
time.sleep(1)
mes=int(input("Qual é o mês de seu nascimento? (01-12): "))

if (mes==1 and dia>=20) or (mes==2 and dia<=18):
    signo=str("Aquário")
elif mes==2 or (mes==3 and dia<=20):
    signo=str("Peixes")
elif mes==3 or (mes==4 and dia<=19):
    signo=str("Áries")
elif mes==4 or (mes==5 and dia<=20):
    signo=str("Touro")
elif mes==5 or (mes==6 and dia<=21):
    signo(str("Gêmeos"))
elif mes==6 or (mes==7 and dia<=21):
    signo=(str("Câncer"))
elif mes==7 or (mes==8 and dia<=23):
    signo=(str("Leão"))
elif mes==8 or (mes==9 and dia<=23):
    signo=(str("Virgem"))
elif mes==9 or (mes==10 and dia<=23):
    signo=(str("Libra"))
elif mes==10 or (mes==11 and dia<=23):
    signo=(str("Escorpião"))
elif mes==11 or (mes==12 and dia <=21):
    signo=str("Sagitário")
else:
    signo=str("Capricórnio")

time.sleep(1)
print("Parabéns, o seu signo é:", signo)
