"""
7 – Utilizando como base o exercício anterior, inclua no menu mais duas opções: uma
para excluir uma pessoa baseada no seu nome e outra para atualizar a idade, altura e
peso, baseado, também, no nome informado.
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

###############################################################

listaDePessoas=[]
listaDePessoas.append(Pessoa("John Python",37,1.7,80))

def nomeEhValido(nomeDigitado):
        for pessoa in listaDePessoas:
                if pessoa.nome == nomeDigitado:
                        return True

def cadastrar():
        nome=input("Nome (str): ") 
        idade=int(input("Idade (int): "))
        altura=float(input("Altura (float): "))
        peso=float(input("Peso (float): "))
        print("Cadastrado.")
        listaDePessoas.append(Pessoa(nome,idade,altura,peso))

def listar():
        for pessoa in listaDePessoas:
                print(pessoa.__str__())

def atualizar():
        nomeDigitado=input("Nome da pessoa a atualizar: ")
        if not nomeEhValido(nomeDigitado):
                print("Nome não encontrado...")
                return
        nome=input("Novo nome: ")
        idade=input("Nova idade: ")
        altura=input("Nova altura: ")
        peso=input("Novo peso: ")

        for indice in range(len(listaDePessoas)):
                if listaDePessoas[indice].nome != nomeDigitado:
                        continue
                listaDePessoas[indice]=Pessoa(nome,idade,altura,peso)
                break

def excluir():
        nomeDigitado=input("Nome da pessoa a EXCLUIR: ")
        if not nomeEhValido(nomeDigitado):
                print("Nome não encontrado...")
                return
        
        for indice in range(len(listaDePessoas)):
                if listaDePessoas[indice].nome != nomeDigitado:
                        continue
                print("Removido.")
                listaDePessoas.pop(indice)
                break
        



while True:
        print("\nCadastro de Pessoas")
        print("-------------------")
        print("1 - Cadastrar      ")
        print("2 - Listar         ")
        print("3 - Atualizar      ")
        print("4 - Excluir        ")
        print("0 - Sair           \n")
        opcao=input("Opção: ")

        match opcao:
                case "1":
                        cadastrar()
                case "2":
                        listar()
                case "3":
                        atualizar()
                case "4":
                        excluir()
                case "0":
                        break
                case _:
                        print("Opção inválida! @w@")
        input("\n<Enter> para continuar...")

