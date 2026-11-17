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
# [x] Registro de serviços
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
        def __init__(self,mes,dia,hora,servico,cliente,profissional):
                self.mes = mes
                self.dia = dia
                self.hora = hora
                self.servico = servico
                self.valorTotal = servico.valor
                self.cliente = cliente
                self.profissional = profissional


listaDeClientes = [
        Cliente("123.456","John Cliente","john@email","123","john")
]
listaDeServicos = [
        Servico("Corte de cabelo",35.0,[]),
        Servico("Manicure",20.0,[])
]
listaDeProfissionais = [
        Profissional("111.111","Jane Cortes","jane@email","111","jane",[]),
        Profissional("222.222","Fulano Mãos","Fulano@email","222","fulano",[])
]
contaDoAdmin = Administrador("admin","Admin","admin@penaareia","0","admin")

# 0: Corte      | 0: Jane
# 1: Manicure   | 1: Fulano
listaDeServicos[0].adicionarProfissional(listaDeProfissionais[0])
listaDeServicos[1].adicionarProfissional(listaDeProfissionais[0])
listaDeServicos[1].adicionarProfissional(listaDeProfissionais[1])
listaDeProfissionais[0].adicionarServico(listaDeServicos[0])

horarioDeFuncionamento = [
        "09:00", "09:30", "08:00", "08:30", "10:00", "10:30",
        "11:00", "11:30", "13:30", "14:00", "14:30", "15:00",
        "15:30", "16:00", "16:30", "17:00", "17:30", "18:00",
]

listaDeHorarios = [
        Horario("01","12","11:00",listaDeServicos[0],listaDeClientes[0],listaDeProfissionais[0])
]

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

login = listaDeClientes[0]
#login = None
def loginLoop():
        while login == None:
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
loginLoop()


###########################################
# ____       _            _             _ #
#|  _ \ _ __(_)_ __   ___(_)_ __   __ _| |#
#| |_) | '__| | '_ \ / __| | '_ \ / _` | |#
#|  __/| |  | | | | | (__| | |_) | (_| | |#
#|_|   |_|  |_|_| |_|\___|_| .__/ \__,_|_|#
#                          |_|            #
###########################################
"""
dia 1 de setembro

[0]  09:30 | [x]  13:30
[1]  10:00 | [x]  14:00
[x]  10:30 | [x]  14:30
[x]  11:00 | [9]  15:00
[5]  11:30 | [10] 15:30
Digite o numero (x significa indisponivel):
"""

def agendarHorario():
        mes = input("Digite o mês (e.g. 11): ")
        dia = input("Digite o dia: ")
        horariosDoDia = [
                h for h in listaDeHorarios if h.mes == mes and h.dia == dia
        ]
        for i in range(len(horarioDeFuncionamento)):
                print(f"| [{i}] {horarioDeFuncionamento[i]} |",end="")
                if i % 3 == 0: print()


# Um profissional tem 1..n serviços
# Um serviço tem 0..n profissionais
def cadastrarServico():
        nome = input("Nome: ")
        valor = input("Valor: ")
        i = 0
        listaDeServicos.append(Servico(nome,valor,[]))

        for profissional in listaDeProfissionais:
                print(f"[{i}] {profissional.nome} ({profissional.cpf})")
                i += 1
        indiceDosProfissionais = input(
                "(em branco para nao atrelar)\n"
                "Digite o(s) profissional(s) que realiza(m) o serviço (e.g. 134): ")
        for i in indiceDosProfissionais:
                listaDeProfissionais[int(i)].adicionarServico(listaDeServicos[-1])
                listaDeServicos[-1].adicionarProfissional(listaDeProfissionais[int(i)])

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
        indiceDosServicos = input("Digite o(s) serviço(s) realizado(s) (e.g. 134): ")
        for i in indiceDosServicos:
                servicos.append(listaDeServicos[int(i)])
        
        listaDeProfissionais.append(
                Profissional(cpf,nome,email,telefone,senha,servicos)
        )
        for i in indiceDosServicos:
                listaDeServicos[int(i)].adicionarProfissional(listaDeProfissionais[-1])
        print("Cadastrado.")

def editarServico():
        for i in range(len(listaDeServicos)):
                print(f"[{i}] {listaDeServicos[i]}")
        s = input("Serviço: ")

while login.obterNomeDaClasse() == "Administrador":
        clear()
        print("  =============================  ")
        print("||      Você é                           ||")
        print("||   administrador!                      ||")
        print("||-------------------                    ||")
        print("||                                       ||")
        print("|| [1] Confirmar horários                ||")
        print("|| [2] Ver clientes                      ||")
        print("||                                       ||")
        print("|| [3] Relatório de demandas             ||")
        print("|| [4] Relatório de lucros               ||")
        print("||                                       ||")
        print("|| [5] Cadastrar profissional            ||")
        print("|| [6] Cadastrar serviço                 ||")
        print("||                                       ||")
        print("|| [7] Atrelar profissional a um serviço ||")
        print("|| [8] Atrelar serviço a um profissional ||")
        print("||                                       ||")
        print("|| [7] Ver serviços                      ||")
        print("|| [8] Editar serviço                    ||")
        print("||                                       ||")
        print("|| [0] Sair                              ||")
        print("||                                       ||")
        print("  =============================  ")
        key = input("Opção: ")
        match key:
                case "5":
                        cadastrarProfissional()
                case "6":
                        cadastrarServico()
                case "7":
                        for i in range(len(listaDeServicos)):
                                print(f"Serviço {i+1}: ")
                                print(listaDeServicos[i])
                case "0":
                        login=None
        input("<Enter>")

while login.obterNomeDaClasse() == "Cliente":
        print(f"   Olá, {login.nome}.      ")
        print(f"  =======================  ")
        print(f"||                       ||")
        print(f"|| [1] Agendar horário   ||")
        print(f"|| [2] Ver seus horários ||")
        print(f"|| [0] Sair              ||")
        print(f"||                       ||")
        print(f"  =======================  ")
        key = input("Opção: ")
        match key:
                case "1":
                        agendarHorario()

loginLoop()
