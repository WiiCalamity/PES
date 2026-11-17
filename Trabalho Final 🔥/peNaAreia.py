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
import os
def clear():
        os.system('cls' if os.name=='nt' else 'clear')

# Para fazer:
# [x] Sistema de login
# [ ] Cadastro de horário
# [ ] Edição da agenda
# [ ] Registro de serviços
# [ ] Consulta de clientes
# [ ] Relatório de lucros
# [ ] Relatório de demandas
# [ ] Pickle

###################################
#  ____ _                         #
# / ___| | __ _ ___ ___  ___  ___ #
#| |   | |/ _` / __/ __|/ _ \/ __|#
#| |___| | (_| \__ \__ \  __/\__ \#
# \____|_|\__,_|___/___/\___||___/#
###################################

class Cliente:
        def __init__(self,cpf,nome,email,telefone,senha):
                self.cpf = cpf
                self.nome = nome
                self.email = email
                self.telefone = telefone
                self.senha = senha
        
        def agendarHorario(self):
                pass
        
        def obterNomeDaClasse(self):
                return type(self).__name__


class Profissional(Cliente):
        def __init__(self,cpf,nome,email,telefone,senha,servicos):
                self.cpf = cpf
                self.nome = nome
                self.email = email
                self.telefone = telefone
                self.senha = senha
                self.servicos = servicos
        
        def __repr__(self):
                return self.nome

        def adicionarServico(self, servico):
                self.servicos.append(servico)
        

class Administrador(Profissional):
        def __init__(self,cpf,nome,email,telefone,senha):
                self.cpf = cpf
                self.nome = nome
                self.email = email
                self.telefone = telefone
                self.senha = senha


class Servico:
        def __init__(self,nome,valor,profissionaisResponsaveis: list):
                self.nome = nome
                self.valor = valor
                self.profissionaisResponsaveis = profissionaisResponsaveis

        def __repr__(self):
                return f" * Nome: {self.nome}\n" + \
                f" * Preço: {self.valor}\n" + \
                f" * Profissionais: {self.profissionaisResponsaveis}\n"
        
        def obterNome(self):
                return self.nome
        
        def adicionarProfissional(self, profissional):
                self.profissionaisResponsaveis.append(profissional)


class Horario:
        def __init__(self,dia,hora,servico,valorTotal,
        nomeDoCliente,nomeDoProfissional):
                self.dia = dia
                self.hora = hora
                self.servico = servico
                self.valorTotal = servico.valor
                self.nomeDoCliente = nomeDoCliente
                self.nomeDoProfissional = nomeDoProfissional

listaDeClientes = [
        Cliente("123.456","John Cliente","john@email","123","john")
]
listaDeServicos = [
        Servico("Corte de cabelo",35.0,[])
]
listaDeProfissionais = [
        Profissional("111.111","Jane Cortes","jane@email","111","jane",[])
]
contaDoAdmin = Administrador("admin","Admin","admin@penaareia","0","admin")

listaDeServicos[0].adicionarProfissional(listaDeProfissionais[0])
listaDeProfissionais[0].adicionarServico(listaDeServicos[0])

############################
# _                _       #
#| |    ___   __ _(_)_ __  #
#| |   / _ \ / _` | | '_ \ #
#| |__| (_) | (_| | | | | |#
#|_____\___/ \__, |_|_| |_|#
#            |___/         #
############################

def fazerLogin():
        cpf = input("CPF: ")
        senha = getpass.getpass(prompt="Senha: ")
        for usuario in listaDeClientes+listaDeProfissionais+[contaDoAdmin]:
                if usuario.cpf == cpf and usuario.senha == senha:
                        break
        else:
                print("CPF ou senha incorretos.")
                return
        global login
        login = usuario
        print(f"Bem vindo(a), {login.nome}")

def cadastrar():
        cpf = input("CPF: ")
        for cliente in listaDeClientes:
                if cpf == cliente.cpf:
                        print("CPF já existe!")
                        return
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Número de telefone: ")
        senha = getpass.getpass(prompt="Senha: ")
        listaDeClientes.append(Cliente(cpf,nome,email,telefone,senha))
        print("Cadastrado! Agora faça login.")

login = contaDoAdmin
#login = None
while login==None:
        clear()
        print("  ===================  ")
        print("||       Login       ||")
        print("||                   ||")
        print("||-------------------||")
        print("||                   ||")
        print("|| [1] Fazer login   ||")
        print("|| [2] Cadastrar     ||")
        print("||                   ||")
        print("  ===================  ")
        key = input("Opção: ")
        match key:
                case "1":
                        fazerLogin()
                case "2":
                        cadastrar()
        input("<Enter>")


###########################################
# ____       _            _             _ #
#|  _ \ _ __(_)_ __   ___(_)_ __   __ _| |#
#| |_) | '__| | '_ \ / __| | '_ \ / _` | |#
#|  __/| |  | | | | | (__| | |_) | (_| | |#
#|_|   |_|  |_|_| |_|\___|_| .__/ \__,_|_|#
#                          |_|            #
###########################################

def cadastrarProfissional():
        cpf = input("CPF: ")
        for profissional in listaDeProfissionais:
                if cpf == profissional.cpf:
                        print("CPF já existe!")
                        return
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Número de telefone: ")
        senha = getpass.getpass(prompt="Senha: ")
        servicos = []

        i = 0
        for servico in listaDeServicos:
                print(f"[{i}] {servico.obterNome()}")
                i += 1
        servicosQueOProfissionalNovoRealiza = input("Digite o(s) serviço(s) realizados (e.g. 134): ")
        for num in servicosQueOProfissionalNovoRealiza:
                servicos.append(listaDeServicos[num])
        
        listaDeProfissionais.append(
                Profissional(cpf,nome,email,telefone,senha,servicos)
        )
        listaDeServicos[num].adicionarProfissional[-1]
        print("Cadastrado.")

while login.obterNomeDaClasse() == "Administrador":
        clear()
        print("  =============================  ")
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
        print("|| [5] Cadastrar profissional  ||")
        print("|| [6] Cadastrar administrador ||")
        print("||                             ||")
        print("|| [7] Ver serviços            ||")
        print("||                             ||")
        print("|| [0] Sair                    ||")
        print("||                             ||")
        print("  =============================  ")
        key = input("Opção: ")
        match key:
                case "5":
                        cadastrarProfissional()
                case "7":
                        i = 1
                        for servico in listaDeServicos:
                                print(f"Serviço [{i}]: ")
                                print(servico)
                                i += 1
                case "0":
                        break
        input("<Enter>")

while login.obterNomeDaClasse() == "Cliente":
        print("  =======================  ")
        print("||                       ||")
        print("|| [1] Agendar horário   ||")
        print("|| [2] Ver seus horários ||")
        print("|| [0] Sair              ||")
        print("||                       ||")
        print("  =======================  ")

