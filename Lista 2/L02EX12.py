#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
12 – Implemente um programa que funcione como uma calculadora entre dois números
informados. Seu programa deve exibir um menu que solicite a operação a ser realizada
entre dois números (adição, subtração, divisão e multiplicação) e os dois números a
serem utilizados no cálculo. Se o usuário digitar uma opção inválida, deve alertar o
usuário e exibir o menu novamente.
"""
import time
import os
def cls(): # https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')

operacao=str()
num1=float()
num2=float()
resultado=float()
i=int(0)

while i==0:
    cls()
    i=1
    print("+---------------------+")
    print("| [+] - Adição        |")
    print("| [-] - Subtração     |")
    print("| [*] - Multiplicação |")
    print("| [/] - Divisão       |")
    print("+---------------------+")
    print(" ")
    time.sleep(0.2)

    operacao=str(input("Digite a operação: "))
    if operacao!="+" and operacao!="-" and operacao!="*" and operacao!="/":
        print("Opção inválida!!")
        i=0
        time.sleep(2)
    else:
        num1=float(input("Digite o primeiro valor: "))
        num2=float(input("Digite o segundo valor: "))
    
        match operacao:
            case "+":
                resultado=float(num1)+float(num2)
            case "-":
                resultado=float(num1)-float(num2)
            case "*":
                resultado=float(num1)*float(num2)
            case "/":
                resultado=float(num1)/float(num2)

print("Resultado:",resultado)
            
    
