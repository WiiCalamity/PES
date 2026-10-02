"""
Exercício B: implemente a classe abaixo, crie 2 objetos e chame o método apresentar().
A apresentação deve mostrar o nome completo e a especialização do professor (filosofia, informática, etc).
 __________________ 
| Professor        |
| -----------------|
| + nome           |
| + sobrenome      |
| + especialização |
| ---------------- |
| + __init__()     |
| + apresentar()   |
'------------------'
"""

class Professor:
        def __init__(self,nome,sobrenome,especializacao):
                self.nome=nome
                self.sobrenome=sobrenome
                self.especializacao=especializacao
        
        def apresentar(self):
                return f"Olá, eu sou o professor {self.nome} {self.sobrenome} e trabalho com {self.especializacao}."

walwal=Professor("Thiago","Waltrik","engenharia de software")
print(walwal.apresentar())

bread=Professor("Thiago","Paes","banco de dados")
print(bread.apresentar())
