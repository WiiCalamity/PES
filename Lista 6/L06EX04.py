"""
4 – Crie uma classe chamada Produto com:
• Atributos: nome e quantidade.
• Um método chamado esta_disponivel que retorna True se a quantidade for maior
que 0 e False caso contrário.
• Um método chamado vender que diminui a quantidade em 1.
Teste criando um objeto, verificando a disponibilidade, vendendo produtos e verificando
novamente.
"""

class Produto:
        def __init__(self,nome,quantidade):
                self.nome=nome
                self.quantidade=quantidade

        def estaDisponivel(self):
                return True if self.quantidade>0 else False

        def vender(self,num=1):
                self.quantidade-=num
        
        def descrever(self):
                return f"Produto: {self.nome}\n" + \
                       f"Estoque: {self.quantidade}\n" + \
                       f"Disponível?: {self.estaDisponivel()}\n"

meuSuperProduto=Produto("Shampoo 6-em-1",30)
print(meuSuperProduto.descrever())

print("Vendendo uma unidade...")
meuSuperProduto.vender()
print(meuSuperProduto.descrever())

print("Vendendo TODAS as unidades...")
todoOEstoque=meuSuperProduto.quantidade
meuSuperProduto.vender(todoOEstoque)
print(meuSuperProduto.descrever())

print("Vendendo uma unidade...")
meuSuperProduto.vender()
print(meuSuperProduto.descrever())