"""
8 – Implemente um algoritmo com as duas classes definidas logo abaixo. Seu algoritmo
deve ter um menu com as seguintes opções:
Sistema de Cadastro
-------------------                          
                                            .================. .==================.
                                            | Estudante      | | Professor        |
1 – Cadastrar estudante                     | -------------- | | ---------------- |
2 – Cadastrar professor                     | + matricula    | | + matricula      |
3 – Listar estudantes                       | + nome         | | + nome           |
4 – Listar professores                      | + sobrenome    | | + sobrenome      |
5 – Alterar estudante pela matrícula        | + idade        | | + idade          |
6 – Alterar estudante pelo nome             | -------------- | | + especializacao |
7 – Alterar professor pela matrícula        | + __init__()   | | ---------------- |
8 – Alterar professor pelo nome             | + apresentar() | | + __init__()     | 
9 – Excluir estudante pela matrícula        '================' | + apresentar()   | 
10 – Excluir professor pela matrícula                          '==================' 
0 – Sair                                             
Opção:
"""

#   ___ _                     #
#  / __| |__ _ ______ ___ ___ #
# | (__| / _` (_-<_-</ -_|_-< #
#  \___|_\__,_/__/__/\___/__/ #

class Estudante():
        def __init__(self,matricula,nome,sobrenome,idade):
                self.matricula=matricula
                self.nome=nome
                self.sobrenome=sobrenome
                self.idade=idade
        
        def __repr__(self):
                return f"Eu sou o(a) estudante {self.nome} {self.sobrenome}, "+\
                f"eu tenho {self.idade} anos "+\
                f"e minha matrícula é {self.matricula}."


class Professor():
        def __init__(self,matricula,nome,sobrenome,idade,especializacao):
                self.matricula=matricula
                self.nome=nome
                self.sobrenome=sobrenome
                self.idade=idade
                self.especializacao=especializacao
        
        def __repr__(self):
                return f"Eu sou o(a) Prof. {self.nome} {self.sobrenome}, "+\
                f"eu tenho {self.idade} anos, "+\
                f"eu trabalho com {self.especializacao} "+\
                f"e minha matrícula é {self.matricula}."


#  ___             /\/|         #
# | __|  _ _ _  __|/\/  ___ ___ #
# | _| || | ' \/ _/ _ \/ -_|_-< #
# |_| \_,_|_||_\__\___/\___/__/ #
#               )_)             #

import os
def clear():
        os.system(cls if os.name == "nt" else clear)


def cadastrarObjeto(lista):
        matricula = int(input("Matrícula: "))
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        idade = int(input("Idade: "))
        if lista == listaDeProfessores:
                especializacao = input("Especialização: ")
                listaDeProfessores.append(Professor(matricula,nome,sobrenome,idade,especializacao))
                return
        listaDeEstudantes.append(Estudante(matricula,nome,sobrenome,idade))


def listarObjetos(lista):
        for objeto in lista:
                print(objeto)


def alterarEstudantePorMatricula():
        matricula = int(input("Matrícula: "))
        for estudante in listaDeEstudantes:
                if estudante.matricula == matricula:
                        matricula = input("Nova matrícula: ")
                        nome = input("Novo nome: ")
                        sobrenome = input("Novo sobrenome: ")
                        idade = int(input("Nova idade: "))
                        print("Alterado.")
                        listaDeEstudantes.remove(estudante)
                        listaDeEstudantes.append(Estudante(matricula,nome,sobrenome,idade))
                        return
        print("Matrícula não encontrada.")


def alterarEstudantePorNome():
        nome = input("Nome: ")
        for estudante in listaDeEstudantes:
                if estudante.nome == nome:
                        matricula = input("Nova matrícula: ")
                        nome = input("Novo nome: ")
                        sobrenome = input("Novo sobrenome: ")
                        idade = int(input("Nova idade: "))
                        print("Alterado.")
                        listaDeEstudantes.remove(estudante)
                        listaDeEstudantes.append(Estudante(matricula,nome,sobrenome,idade))
                        return
        print("Nome não encontrado.")


def alterarProfessorPorMatricula():
        matricula = int(input("Matrícula: "))
        for professor in listaDeProfessores:
                if professor.matricula == matricula:
                        matricula = input("Nova matrícula: ")
                        nome = input("Novo nome: ")
                        sobrenome = input("Novo sobrenome: ")
                        idade = int(input("Nova idade: "))
                        especializacao = input("Nova especialização: ")
                        print("Alterado.")
                        listaDeProfessores.remove(professor)
                        listaDeProfessores.append(Professor(matricula,nome,sobrenome,idade,matricula))
                        return
        print("Matrícula não encontrada.")


def alterarProfessorPorNome():
        nome = input("Nome: ")
        for professor in listaDeProfessores:
                if professor.nome == nome:
                        matricula = input("Nova matrícula: ")
                        nome = input("Novo nome: ")
                        sobrenome = input("Novo sobrenome: ")
                        idade = int(input("Nova idade: "))
                        especializacao = input("Nova especialização: ")
                        print("Alterado.")
                        listaDeProfessores.remove(professor)
                        listaDeProfessores.append(Professor(matricula,nome,sobrenome,idade,matricula))
                        return
        print("Nome não encontrado.")

def excluirProfessorPorMatricula():
        matricula = int(input("Matrícula: "))
        for professor in listaDeProfessores:
                if professor.matricula == matricula:
                        listaDeProfessores.remove(professor)
                        print("Removido.")
                        return
        print("Matrícula não encontrada.")


def excluirEstudantePorMatricula():
        matricula = int(input("Matrícula: "))
        for estudante in listaDeEstudantes:
                if estudante.matricula == matricula:
                        listaDeEstudantes.remove(estudante)
                        print("Removido.")
                        return
        print("Matrícula não encontrada.")


#  ___                            _      _  #
# / __| ___ __ _ _  _ ___ _ _  __(_)__ _| | #
# \__ \/ -_) _` | || / -_) ' \/ _| / _` | | # 
# |___/\___\__, |\_,_\___|_||_\__|_\__,_|_| # 
#             |_|                           #



listaDeProfessores=[Professor(10293, "Thiago", "Waltrik", 23, "programação")]
listaDeEstudantes=[Estudante(20110, "Kiara", "Rosa", 17)]

while True:
        print("Sistema de Cadastro                   ")
        print("-------------------                   ")
        print("1 – Cadastrar estudante               ")
        print("2 – Cadastrar professor               ")
        print("3 – Listar estudantes                 ")
        print("4 – Listar professores                ")
        print("5 – Alterar estudante pela matrícula  ")
        print("6 – Alterar estudante pelo nome       ")
        print("7 – Alterar professor pela matrícula  ")
        print("8 – Alterar professor pelo nome       ")
        print("9 – Excluir estudante pela matrícula  ")
        print("10 – Excluir professor pela matrícula ")
        print("0 – Sair                            \n")
        opcao=input("Opção: ")

        match opcao:
                case "1":
                        cadastrarObjeto(listaDeEstudantes)
                case "2":
                        cadastrarObjeto(listaDeProfessores)
                case "3":
                        listarObjetos(listaDeEstudantes)
                case "4":
                        listarObjetos(listaDeProfessores)
                case "5":
                        alterarObjeto(listaDeEstudantes)
                case "6":
                        alterarEstudantePorNome()
                case "7":
                        alterarProfessorPorMatricula()
                case "8":
                        alterarProfessorPorNome()
                case "9":
                        excluirEstudantePorMatricula()
                case "10":
                        excluirProfessorPorMatricula()
                case "0":
                        break
                case _:
                        print("Opção inválida! @w@")
        input("\n<Enter> para continuar...")


