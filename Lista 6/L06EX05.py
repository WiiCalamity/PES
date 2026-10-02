"""
5 – Crie uma classe chamada Pessoa com:
• Atributos: nome, idade, altura e peso;
• Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
pessoa;
• Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
• Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
estão corretos.
"""
class Pessoa:
        def __init__(self,nome,idade,altura,peso):
                self.nome=nome
                self.idade=idade
                self.altura=altura
                self.peso=peso
        
        def __str__(self):
                return f"{self.nome}, {self.idade}, {self.altura}, {self.peso}"
        
        def obterTodosOsDados(self):
                return self.nome, self.idade, self.altura, self.peso

        def obterNome(self):
                return self.nome
        
        def obterImc(self):
                return round(self.peso/(self.altura**2),1)
        
        def obterNomeEImc(self): # método recursivo
                return self.obterNome(), self.obterImc()

sujeitoA=Pessoa("John Python", 34, 1.70, 80.0)
print(sujeitoA.obterTodosOsDados())
print(sujeitoA.obterNomeEImc())
print()

sujeitoB=Pessoa("Jane Rust", 35, 1.69, 70.0)
print(sujeitoB.obterTodosOsDados())
print(sujeitoB.obterNomeEImc())
print()

sujeitoC=Pessoa("Jim Bash", 48, 1.66, 72.0)
print(sujeitoC.obterTodosOsDados())
print(sujeitoC.obterNomeEImc())
print()