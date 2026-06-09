'''
Exercício 09: Implemente um algoritmo que solicite ao usuário a
quantidade de salgados consumidos na cantina e o valor do
salgado (considere que todos possuem o mesmo preço).
Lembre-se que o preço é um número de ponto flutuante e não
um inteiro. Em seguida, exiba o valor total da compra.
Atenção: todos os algoritmos devem possuir comentários
'''

numDeSalgados = int(input("Quantos salgados? ")) # Você quer salgados inteiros, eu espero.
precoDoSalgado = float(input("Qual o preço de cada salgado? ")) # Por ser um valor monetário, o número pode ser fracionado.

valorDaCompra = precoDoSalgado * numDeSalgados
print ("O valor total da sua compra é: R$",valorDaCompra)
