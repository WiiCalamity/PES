#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6 - Jogo do Pedra, Papel, Tesoura. Solicite as escolhas do jogador 1 e do jogador 2
(“pedra”, “papel” ou “tesoura”). Use condicionais para determinar quem ganhou:
• Pedra ganha de tesoura, tesoura ganha de papel, papel ganha de pedra.
• Exiba uma mensagem como “Jogador 1 venceu!” ou “Empate!”.
"""
import os
def cls(): # https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')

cls()
escolhaDoJog1 = str(input("Jogador 1, escolha [pedra], [papel], ou [tesoura]: "))
cls() # Limpar a tela para manter a escolha do jogador 1 em sigilo.
escolhaDoJog2 = str(input("Jogador 2, escolha [pedra], [papel], ou [tesoura]: "))

quemGanhou="indefinido"

if escolhaDoJog1 == escolhaDoJog2: # "Buraco Negro" empata com "Buraco Negro" também.
    quemGanhou=0
elif escolhaDoJog1=="pedra" and escolhaDoJog2=="papel":
    quemGanhou=2
elif escolhaDoJog1=="pedra" and escolhaDoJog2=="tesoura":
    quemGanhou=1
elif escolhaDoJog1=="papel" and escolhaDoJog2=="pedra":
    quemGanhou=1
elif escolhaDoJog1=="papel" and escolhaDoJog2=="tesoura":
    quemGanhou=2
elif escolhaDoJog1=="tesoura" and escolhaDoJog2=="pedra":
    quemGanhou=2
elif escolhaDoJog1=="tesoura" and escolhaDoJog2=="papel":
    quemGanhou=1
    
if quemGanhou==0:
    print("É um empate!")
elif quemGanhou==1:
    print("Jogador 1 venceu!")
elif quemGanhou==2:
    print("Jogador 2 venceu!")
else:
    print("Erro! Alguém digitou errado!")

    
