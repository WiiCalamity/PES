"""
1 – Crie uma classe chamada Livro com:
• Atributos: titulo e autor.
• Um método chamado descricao que retorna: "{titulo} foi escrito por {autor}."
Teste criando um objeto e chamando o método para exibir a descrição.
"""
class Livro:
        def __init__(self,titulo,autor):
                self.titulo=titulo
                self.autor=autor

        def descricao(self):
                return f"{self.titulo} foi escrito por {self.autor}"

meuLivro=Livro("O Pequeno Príncipe","Antoine de Saint-Exupéry")
print(meuLivro.descricao())