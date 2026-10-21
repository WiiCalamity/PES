"""
1 - Livro e MarcadorDePagina (0..1).
Objetivo: Implementar um relacionamento opcional simples.
Classes: MarcadorDePagina e Livro.
Regras:
• A classe MarcadorDePagina deve ter um atributo pagina_atual.
• A classe Livro deve ter um atributo titulo e um total_paginas.
• Um Livro pode ter zero ou um MarcadorDePagina (ele começa sem marcador,
0..1).
• Crie um método no Livro chamado adicionar_marcador(pagina). Este método deve
criar uma instância de MarcadorDePagina e associá-la ao livro. Se o livro já tiver
um marcador, apenas atualize a pagina_atual dele.
Comprove o funcionamento da sua implementação no programa principal.
Veja, na figura abaixo, o Diagrama de Classes completo:

MarcadorDePagina                       Livro
+ pagina_atual                         + titulo
--------         0..1              1   + totalDePaginas
+ __init__()      =================    --------
+ __repr__()                           + __init__()
                                       + adicionarMarcador(pagina)
                                       + __repr__()
"""

        
class Marcador:
        def __init__(self,paginaAtual: int):
                self.paginaAtual = paginaAtual

        def __repr__(self):
                return f"Eu sou um marcador e eu estou na página {self.paginaAtual}\n"


class Livro:
        def __init__(self, titulo: str, totalDePaginas: int):
                self.titulo = titulo
                self.totalDePaginas = totalDePaginas
                self.paginaMarcada = None

        def __repr__(self):
                return f"Título: {self.titulo}\nPáginas: {self.totalDePaginas}\n"

        def adicionarMarcador(self, paginaAMarcar: int):
                if paginaAMarcar <= 0 or paginaAMarcar > self.totalDePaginas:
                        return False
                self.paginaMarcada = Marcador(paginaAMarcar)
                # Por que atualizar o marcador se posso trocar por um novo
                # tendo o mesmo resultado?


print("Criando um livro...")
livroBacana = Livro("Harry Potter 2", 417)
print(livroBacana)

print("Adicionando marcador...")
livroBacana.adicionarMarcador(44)
print(livroBacana.paginaMarcada)

print("Atualizando marcador...")
livroBacana.adicionarMarcador(52)
print(livroBacana.paginaMarcada)
