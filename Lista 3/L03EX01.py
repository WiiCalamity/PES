# -*- coding: utf-8 -*-
"""
1 - Implemente um programa com um cadastro de idades de 6 alunos utilizando lista. O
programa deve solicitar as idades dos 6 alunos. Após informar todas as idades, deve-se
apresentar apenas as idades que forem maiores ou iguais a 16.
"""
idades=[0]*6
check=bool()

for i in range(6):
    print("Idade do aluno",i+1,":",end=" ")
    idades[i]=int(input())

print(" ")
print("Alunos maiores de 16 anos:")
for i in range(6):
    if idades[i] >= 16: # Quem tem 16 anos ainda faz parte dos maiores de idade
       print("O aluno",i+1,"é maior de idade.")
       check=bool("OhYeah")

if not check:
    print("Ninguém é maior de idade!")
       
    