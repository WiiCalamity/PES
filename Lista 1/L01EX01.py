'''
1 – Solicite o valor total de uma compra. Se o valor for maior ou igual a 100, exiba "Você
ganhou um cupom de desconto!". Caso contrário, exiba "Continue comprando para
ganhar um cupom de desconto!".
'''

valorTotal = float(input("Quantos reais você gastou?? "))
if valorTotal >= 100: # Compara valorTotal com o número 100
    print("Você ganhou um cupom de desconto!")
else:
    print("Continue comprando para ganhar um cupom de desconto!")
# Não precisa fechar