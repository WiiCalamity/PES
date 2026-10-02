"""
6 – Utilizando como base a classe Pessoa do exercício anterior, crie um algoritmo que
funcionará como um cadastro de pessoas em uma lista. Seu algoritmo deve ter um menu
conforme abaixo:

Cadastro de Pessoas
-------------------
1 – Cadastrar
2 – Listar
0 – Sair
Opção:
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

listaDePessoas=[]

def cadastrar():
        nome=input("Nome (str): ")
        idade=input("Idade (int): ")
        altura=input("Altura (float): ")
        peso=input("Peso (float): ")
        listaDePessoas.append(Pessoa(nome,idade,altura,peso))

def listar():
        for pessoa in listaDePessoas:
                print(pessoa)


while True:
        print("Cadastro de Pessoas")
        print("-------------------")
        print("1 - Cadastrar      ")
        print("2 - Listar         ")
        print("0 - Sair           ")
        opcao=input("Opção: ")

        match opcao:
                case "1":
                        cadastrar()
                case "2":
                        listar()
                case "0":
                        break
                case _:
                        print("Opção inválida! @w@")
        input("\n<Enter> para continuar...")