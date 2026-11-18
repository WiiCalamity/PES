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
"""
Para fazer:
[x] Sistema de login
[x] Cadastro de horário
[ ] Edição da agenda
[x] Registro de serviços
[x] Consulta de clientes
[ ] Relatório de lucros
[ ] Relatório de demandas
[x] Ver agenda (profissional)
[ ] Pickle
Onde parei: método de editar agenda do admin
"""

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
                self.horariosMarcados = []

        def __repr__(self):
                return f"{self.cpf}: \"{self.nome}\" {self.email} {self.telefone}"

        def obterNomeDaClasse(self):
                return type(self).__name__

        def printarAgenda(self, mes, dia):
                for i in range(len(horarioDeFuncionamento)):
                        marca = i
                        for horario in listaDeHorariosMarcados:
                                if horario.hora == horarioDeFuncionamento[i] \
                                and horario.mes == mes and horario.dia == dia:
                                        marca = "X"
                                        break
                        print(f"[ {marca} ] {horarioDeFuncionamento[i]}")


        def agendarHorario(self):
                mes = input("Digite o mês (e.g. 12): ")
                if int(mes) > 12:
                        print("NÃO")
                        return
                dia = input("Digite o dia (e.g. 1): ")
                if int(dia) > 31:
                        print("NÃO")
                        return

                self.printarAgenda(mes, dia)
                hora = horarioDeFuncionamento[int(input("Selecione a hora: "))]

                printarServicosCurto()
                servicoEscolhido = listaDeServicos[int(input("Selecione o serviço: "))]
                print("Você escolheu: ",servicoEscolhido.nome)

                for profissional in listaDeProfissionais:
                        if servicoEscolhido in profissional.servicos:
                                profissionalEscolhido = profissional
                                break
                listaDeHorariosMarcados.append(
                        HorarioMarcado(mes,dia,hora,servicoEscolhido,self,profissionalEscolhido)
                        )
                self.horariosMarcados.append(listaDeHorariosMarcados[-1])


        def verMeusHorarios(self):
                print(f"Você tem {len(self.horariosMarcados)} horário(s).")
                for i in range(len(self.horariosMarcados)):
                        print(f"[{i+1}] Mês {self.horariosMarcados[i].mes} " +
                              f"dia {self.horariosMarcados[i].mes} " +
                              f"às {self.horariosMarcados[i].hora}: " +
                              f"R$ {self.horariosMarcados[i].valorTotal} " +
                              f"{self.horariosMarcados[i].servico.nome} "
                              # Que pesadelo ^^
                        )


        def printarServicosCurto(self):
                i = 0
                for servico in listaDeServicos:
                        print(f"[{i}] {servico.nome}")
                        i += 1


        def printarServicosCompleto(self):
                [print(s) for s in listaDeServicos]



class Profissional(Cliente):
        def __init__(self,cpf,nome,email,telefone,senha,servicos):
                self.cpf = cpf
                self.nome = nome
                self.email = email
                self.telefone = telefone
                self.senha = senha
                self.horariosMarcados = []
                self.servicos = servicos
        
        def __repr__(self):
                return self.nome
        
        def printarAgenda(self, mes, dia):
                for i in range(len(horarioDeFuncionamento)):
                        apendice = ""
                        for horario in listaDeHorariosMarcados:
                                if horario.hora == horarioDeFuncionamento[i] \
                                and horario.mes == mes and horario.dia == dia:
                                        apendice = f"(indisponível: " + \
                                        f"{horario.profissional}" + \
                                        f"{horario.cliente.nome})"
                                        break
                        print(f"[ {i} ] {horarioDeFuncionamento[i]} {apendice}")

        def adicionarServico(self, servico):
                self.servicos.append(servico)
        

class Administrador(Profissional):
        def __init__(self,cpf,nome,email,telefone,senha):
                self.cpf = cpf
                self.nome = nome
                self.email = email
                self.telefone = telefone
                self.senha = senha

        def printarHorariosMarcados(self):
                i = 0
                for horario in listaDeHorariosMarcados:
                        print(f"[{i}] {horario.dia}/{horario.mes} {horario.hora} -- " + \
                                f"{horario.cliente.nome} "
                                f"({horario.servico.nome} com {horario.profissional.nome})"
                        )
                        i += 1

        def editarHorario(self):
                self.printarHorariosMarcados()
                indiceDoHorario = int(input("Horario: "))
                mes = input("Mes: ")
                dia = input("Dia: ")
                hora = input("Hora: ")

                self.printarServicosCurto()
                servico = listaDeServicos[int(input("Servico: "))]

                self.printarClientesCurto()
                indiceDoCliente = int(input("Cliente: "))
                cliente = listaDeClientes[indiceDoCliente]

                self.printarProfissionaisCurto()
                indiceDoProfissional = int(input("Profissional: "))
                profissional = listaDeProfissionais[indiceDoProfissional]

                horarioNovo = HorarioMarcado(mes,dia,hora,servico,cliente,profissional)

                i = 0
                for horario in cliente.horariosMarcados:
                        print("EEEEEEEE")
                        if horario.mes == mes and horario.dia == dia and horario.hora == hora:
                                print("AAAAAAA")
                                listaDeClientes[indiceDoCliente].horariosMarcados[i] = horarioNovo
                                break
                        i += 1

                i = 0
                for horario in profissional.horariosMarcados:
                        print("DDDDDDD")
                        if horario.mes == mes and horario.dia == dia and horario.hora == hora:
                                print("BBBBBB")
                                listaDeProfissionais[indiceDoProfissional].horariosMarcados[i] = horarioNovo
                                break
                        i += 1

                listaDeHorariosMarcados[indiceDoHorario] = horarioNovo










                # self.printarAgenda(input("Mês: "), input("Dia: "))
                #
                # indiceDaHora = int(input("Hora: "))
                # hora = horarioDeFuncionamento[indiceDaHora]
                #
                # mes = input("Mês: ")
                # dia = input("Dia: ")
                # hora = input("Hora: ")
                #
                # self.printarServicosCurto()
                # servico = listaDeServicos[int(input("Serviço: "))]
                #
                # self.printarClientesCurto()
                # indiceDoCliente = int(input("Cliente: "))
                # cliente = listaDeClientes[indiceDoCliente]
                #
                # self.printarProfissionaisCurto()
                # indiceDoProfissional = int(input("Profissional: "))
                # profissional = listaDeProfissionais[indiceDoProfissional]






                # horarioNovo = HorarioMarcado(mes,dia,hora,servico,cliente,profissional)
                # i = 0
                # for horario in listaDeHorariosMarcados:
                #         if horario.mes == mes and horario.dia == dia and horario.hora == hora:
                #                 listaDeHorariosMarcados[i] = horarioNovo
                #                 break
                #         i += 1
                # i = 0
                # j = 0
                # for cliente in listaDeClientes:
                #         for horario in cliente.horariosMarcados:
                #                 if horario.mes == mes and horario.dia == dia \
                #                 and horario.hora == hora:
                #                         listaDeClientes[i].horariosMarcados[j] = horarioNovo
                #                         break
                #                 j += 1
                #         i += 1
                #
                # i = 0
                # j = 0
                # for profissional in listaDeProfissionais:
                #         for horario in profissional.horariosMarcados:
                #                 if horario.mes == mes and horario.dia == dia \
                #                 and horario.hora == hora:
                #                         listaDeProfissionais[i].horariosMarcados[j] = horarioNovo
                #                         break


        def printarClientesCurto(self):
                i = 0
                for cliente in listaDeClientes:
                        print(f"[{i}] {cliente.nome} ({cliente.cpf})")
                        i += 1

        def printarProfissionaisCurto(self):
                i = 0
                for profissional in listaDeProfissionais:
                        print(f"[{i}] {profissional.nome} ({profissional.cpf})")
                        i += 1

        def cadastrarProfissional(self):
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
                        print(f"[{i}] {servico.nome}")
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

class Servico:
        def __init__(self,nome,valor,profissionaisResponsaveis: list):
                self.nome = nome
                self.valor = valor
                self.profissionaisResponsaveis = profissionaisResponsaveis

        def __repr__(self):
                return f"{self.nome}\n" + \
                f" * Preço: {self.valor}\n" + \
                f" * Profissionais: {self.profissionaisResponsaveis}\n"

        def adicionarProfissional(self, profissional):
                self.profissionaisResponsaveis.append(profissional)


class HorarioMarcado:
        def __init__(self,mes,dia,hora,servico,cliente,profissional):
                self.mes = mes
                self.dia = dia
                self.hora = hora
                self.servico = servico
                self.valorTotal = servico.valor
                self.cliente = cliente
                self.profissional = profissional

        def __repr__(self):
                return f"{self.dia}/{self.mes}:{self.hora}-{self.profissional}"


#############################################################################
#__     __         _   __            _       ___       _      _       _     #
#\ \   / /_ _ _ __(_) /_/___   _____(_)___  |_ _|_ __ (_) ___(_) __ _(_)___ #
# \ \ / / _` | '__| |/ _` \ \ / / _ \ / __|  | || '_ \| |/ __| |/ _` | / __|#
#  \ V / (_| | |  | | (_| |\ V /  __/ \__ \  | || | | | | (__| | (_| | \__ \#
#   \_/ \__,_|_|  |_|\__,_| \_/ \___|_|___/ |___|_| |_|_|\___|_|\__,_|_|___/#
#############################################################################

horarioDeFuncionamento = [
        "08:00", "08:30", "09:00", "09:30", "10:00", "10:30",
        "11:00", "11:30", "13:30", "14:00", "14:30", "15:00",
        "15:30", "16:00", "16:30", "17:00", "17:30", "18:00",
]

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

# Monstruosidade
listaDeServicos[0].adicionarProfissional(listaDeProfissionais[0])
listaDeServicos[1].adicionarProfissional(listaDeProfissionais[0])
listaDeServicos[1].adicionarProfissional(listaDeProfissionais[1])
listaDeProfissionais[0].adicionarServico(listaDeServicos[0])
listaDeProfissionais[1].adicionarServico(listaDeServicos[1])

listaDeHorariosMarcados = [
        HorarioMarcado("12","1","11:00",listaDeServicos[0],listaDeClientes[0],listaDeProfissionais[0])
]
listaDeClientes[0].horariosMarcados.append(listaDeHorariosMarcados[0])
listaDeProfissionais[0].horariosMarcados.append(listaDeHorariosMarcados[0])


########################################
# _____                 /\/|           #
#|  ___|   _ _ __   ___|/\/   ___  ___ #
#| |_ | | | | '_ \ / __/ _ \ / _ \/ __|#
#|  _|| |_| | | | | (_| (_) |  __/\__ \#
#|_|   \__,_|_| |_|\___\___/ \___||___/#
#                   )_)                #
########################################

def prosseguir():
        input("\n<Enter> para continuar...")

def fazerLogin():
        global login
        cpf = input("CPF: ")
        senha = getpass.getpass(prompt="Senha: ")
        for usuario in listaDeClientes+listaDeProfissionais+[contaDoAdmin]:
                if usuario.cpf == cpf and usuario.senha == senha:
                        login = usuario
                        return True
        print("CPF ou senha incorretos.")


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




def editarServico():
        # Incompleto
        for i in range(len(listaDeServicos)):
                print(f"[{i}] {listaDeServicos[i]}")
        s = input("Serviço: ")


###########################################
# ____       _            _             _ #
#|  _ \ _ __(_)_ __   ___(_)_ __   __ _| |#
#| |_) | '__| | '_ \ / __| | '_ \ / _` | |#
#|  __/| |  | | | | | (__| | |_) | (_| | |#
#|_|   |_|  |_|_| |_|\___|_| .__/ \__,_|_|#
#                          |_|            #
###########################################

#login = None
#login = listaDeClientes[0]
#login = listaDeProfissionais[0]
login = contaDoAdmin
while True:
        while not login:
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
                                if fazerLogin():
                                        break
                        case "2":
                                cadastrar()
                prosseguir()

        while login.obterNomeDaClasse() == "Administrador":
                clear()
                print("  ========================================  ")
                print("||         Você é administrador!          ||")
                print("||                                        ||")
                print("||----------------------------------------||")
                print("||                                        ||")
                print("|| [1]  Ver clientes                      ||")
                print("|| [2]  Ver serviços                      ||")
                print("||                                        ||")
                print("|| [3]  Editar serviço                    ||")
                print("|| [4]  Editar horario                    ||")
                print("||                                        ||")
                print("|| [5]  Cadastrar profissional            ||")
                print("|| [6]  Cadastrar serviço                 ||")
                print("||                                        ||")
                print("|| [7]  Atrelar profissional a um serviço ||")
                print("|| [8]  Atrelar serviço a um profissional ||")
                print("||                                        ||")
                print("|| [9]  Relatório de demandas             ||")
                print("|| [10] Relatório de lucros               ||")
                print("||                                        ||")
                print("|| [0]  Sair                              ||")
                print("||                                        ||")
                print("  ========================================  ")
                key = input("Opção: ")
                match key:
                        case "1":
                                [print(c) for c in listaDeClientes]
                        case "2":
                                [print(s) for s in listaDeServicos]
                        case "4":
                                contaDoAdmin.editarHorario()
                        case "5":
                                contaDoAdmin.cadastrarProfissional()
                        case "6":
                                contaDoAdmin.cadastrarServico()
                        case "0":
                                break
                prosseguir()

        while login.obterNomeDaClasse() == "Profissional":
                clear()
                print(f"Olá, {login.nome}.         ")
                print(f"  =======================  ")
                print(f"||                       ||")
                print(f"|| [1] Ver agenda        ||")
                print(f"|| [2] Ver meus horários ||")
                print(f"||                       ||")
                print(f"|| [3] Listar serviços   ||")
                print(f"||                       ||")
                print(f"|| [0] Sair              ||")
                print(f"||                       ||")
                print(f"  =======================  ")
                key = input("Opção: ")
                match key:
                        case "1":
                                mes = input("Digite o mês (e.g. 12): ")
                                if int(mes) > 12:
                                        print("NÃO")
                                        continue
                                dia = input("Digite o dia (e.g. 1): ")
                                if int(dia) > 31:
                                        print("NÃO")
                                        continue

                                login.printarAgenda(mes, dia)
                        case "2":
                                login.verMeusHorarios()
                        case "3":
                                printarServicosCurto()
                        case "0":
                                break
                prosseguir()

        while login.obterNomeDaClasse() == "Cliente":
                clear()
                print(f"Olá, {login.nome}.         ")
                print(f"  =======================  ")
                print(f"||                       ||")
                print(f"|| [1] Agendar horário   ||")
                print(f"|| [2] Ver meus horários ||")
                print(f"||                       ||")
                print(f"|| [3] Listar serviços   ||")
                print(f"||                       ||")
                print(f"|| [0] Sair              ||")
                print(f"||                       ||")
                print(f"  =======================  ")
                key = input("Opção: ")
                match key:
                        case "1":
                                login.agendarHorario()
                        case "2":
                                login.verMeusHorarios()
                        case "3":
                                printarServicosCurto()
                        case "0":
                                break
                prosseguir()
        login = None

