'''
Exercício 10: Implemente um algoritmo que solicite ao usuário a
quantidade de salgados consumidos na cantina e o valor do
salgado (considere que todos possuem o mesmo preço). Solicite
também ao usuário a quantidade de sucos consumida e o valor
do suco (considere, também, que todos possuem o mesmo
preço). Em seguida, exiba o valor total da compra.
'''
# Reciclado do exercício anterior

numDeSalgados = int(input("Quantos salgados você quer? "))
precoDoSalgado = float(input("Qual o preço de cada salgado? "))
numDeSucos = int(input("Quantos sucos você quer? "))
precoDoSuco = float(input("Qual o preço de cada suco? "))

valorDaCompra = (precoDoSalgado*numDeSalgados) + (precoDoSuco*numDeSucos) # Calcula o valor dos salgados, o valor dos sucos e junta-os.
print ("O valor total da sua compra é: R$",valorDaCompra)