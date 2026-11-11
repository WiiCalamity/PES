#!/bin/python3
"""
Sua dupla, no Trabalho 2, elaborou um projeto de sistema de informação, utilizando como
metodologia de desenvolvimento o Processo Unificado. Agora, devemos dar continuidade
ao desenvolvimento elaborando um protótipo, com uso do paradigma orientado a objetos,
que servirá para validar a modelagem conceitual, os requisitos e os casos de uso
identificados. Como se trata de um protótipo inicial, a interface com o usuário será modo
texto, similar à de um chatbot para WhatsApp.
Sua implementação deve possuir:
a) Cadastro de usuários;
b) Login de usuário;
c) Implementação de, pelo menos, 6 casos de uso que só poderão ser realizados
após o login no sistema (casos de uso estereotipados como CRUD contam apenas
como 1);
d) Modelagem de dados utilizando o paradigma de orientação a objetos (tendo como
base o modelo conceitual);
e) Persistência de dados através do pickle ou módulo semelhante.
"""
import pickle
import getpass

class Usuario:
        def __init__(self,cpf,nome,email,telefone,senha,cargo="cliente",servicoRealizado=None):
                self.cpf = cpf
                self.nome = nome
                self.email = email
                self.telefone = telefone
                self.senha = senha
                self.cargo = cargo
                self.servicoRealizado = servicoRealizado
        def __repr__(self):
                return f"Meu nome é {self.nome} e eu sou um usuário genérico"


class Servico:
        def __init__(self, nome, valor, profissionalResponsavel):
                self.nome = nome
                self.valor = valor
                self.profissionalResponsavel = profissionalResponsavel

class Horario:
        def __init__(self,dia,hora,servico,valorTotal,nomeDoCliente,nomeDoProfissional):
                self.dia = dia
                self.hora = hora
                self.servico = servico
                self.valorTotal = servico.valor
                self.nomeDoCliente = nomeDoCliente
                self.nomeDoProfissional = nomeDoProfissional

# Um Horario tem 1..n serviços
# Um servico tem 0..n horarios

listaServico = []
listaServico.append("Corte de cabelo", 20, [listaUsuario[1].nome])

listaHorario = []
listaHorario.append()

listaUsuario = []
listaUsuario.append(Usuario("000.111.222-33","John Cliente","john@email.com","abc1234"))
listaUsuario.append(Usuario("999.888.777-66","Jane Cortes","jane@email.com","abc1234","profissional"))
listaUsuario.append(Usuario("777.777.777-77","Admin","admin@penaareia.com","admin","admin"))

def cadastrarCliente():
        cpf = input("CPF: ")
        for usuario in listaUsuario:
                if cpf == usuario.cpf:
                        return "CPF já existe!"
        
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Número de telefone: ")
        senha = getpass.getpass(prompt="Senha: ")
        usuario.append(Cliente(cpf, nome, email, telefone, senha))
        return "Cadastrado! Agora faça login."


def fazerLogin():
        cpf = input("CPF: ")
        senha = getpass.getpass(prompt="Senha: ")

        for usuario in listaUsuario:
                if usuario.cpf == cpf and usuario.senha == senha:
                        break
        else:
                return "CPF ou senha incorretos."
        
        global login
        login = usuario
        return f"Bem vindo(a), {login.nome}"


def agendarHorario():
        dia = int(input("Dia (ex. 4): "))
        hora = input("Hora (ex. 13:30): ")
        servico = listaServico[0]
        valorTotal = servico.valor
        

        

while True:
        print("  ===================  ")
        print("||       Login       ||")
        print("||                   ||")
        print("||-------------------||")
        print("||                   ||")
        print("|| [1] Fazer login   ||")
        print("|| [2] Cadastrar     ||")
        print("|| [0] Sair          ||")
        print("||                   ||")
        print("  ===================  ")
        key = input("Opção: ")
        match key:
                case "1":
                        print(fazerLogin())
                case "2":
                        print(cadastrarCliente())
                case "0":
                        break

while True:
        print("  =======================  ")
        print("||                       ||")
        print("|| [1] Agendar horário   ||")
        print("|| [2] Ver seus horários ||")
        print("|| [0] Sair              ||")
        print("||                       ||")
        print("  =======================  ")


while True:
        print("  ===================  ")
        print("||      Você é                 ||")
        print("||   administrador!            ||")
        print("||-------------------          ||")
        print("||                             ||")
        print("|| [1] Confirmar horários      ||")
        print("|| [2] Ver clientes            ||")
        print("||                             ||")
        print("|| [3] Relatório de demandas   ||")
        print("|| [4] Relatório de lucros     ||")
        print("||                             ||")
        print("|| [8] Cadastrar funcionário   ||")
        print("|| [9] Cadastrar administrador ||")
        print("||                             ||")
        print("|| [0] Sair                    ||")
        print("||                             ||")
        print("  ===================  ")