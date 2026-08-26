"""
1 – Crie um programa com uma função para calcular a média aritmética simples entre 3
notas. Seu programa deve solicitar 3 notas, chamar a função e exibir o resultado na tela.
"""

def calcularMedia(a,b,c):
        print((a+b+c)/3)

n1=float(input("Nota 1: "))
n2=float(input("Nota 2: "))
n3=float(input("Nota 3: "))
calcularMedia(n1,n2,n3)