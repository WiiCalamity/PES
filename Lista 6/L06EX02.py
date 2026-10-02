"""
2 – Crie uma classe chamada Carro com:
• Atributos: marca e cor.
• Um método chamado pintar que recebe uma nova cor como argumento e altera o
atributo cor para essa nova cor.
• Um método chamado mostrar_cor que retorna a cor atual do carro.
Teste criando um objeto, alterando sua cor com o método pintar e exibindo a nova cor
com mostrar_cor.
"""

class Carro:
        def __init__(self,marca,cor):
                self.marca=marca
                self.cor=cor
        
        def pintar(self,novaCor):
                self.cor=novaCor

        def mostrarCor(self):
                return self.cor

minhaNave=Carro("Fiat","Branco")
print(f"Cor: {minhaNave.mostrarCor()}")

print("Pintando o carro...")

minhaNave.pintar("Azul")
print(f"Cor nova: {minhaNave.mostrarCor()}")