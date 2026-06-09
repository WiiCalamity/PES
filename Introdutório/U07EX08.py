'''
Exercício 08: Implemente um algoritmo que leia a quantidade
de partidas de um campeonato de futebol e indique a
quantidade de minutos total (de todas as partidas juntas).
Considere que cada partida terá sempre o mesmo tempo.
Comente seu algoritmo.
'''

numDePartidas = int(input("Quantas partidas? ")) # Variável inteira.
duracaoPorPartida = int(90) # Uma partida de futebol sempre tem 90 minutos (sem os acréscimos).

duracaoTotal = numDePartidas * duracaoPorPartida
print("Todas as partidas terão", duracaoTotal, "min no total")