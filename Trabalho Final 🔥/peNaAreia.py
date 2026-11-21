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
[x] Edição da agenda
[x] Registro de serviços
[x] Consulta de clientes
[ ] Relatório de lucros
[ ] Relatório de demandas
[x] Ver agenda (profissional)
[ ] Pickle
Onde parei: Relatório
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
                self.horariosAgendados = []

        def __repr__(self):
                return f"{self.cpf}: \"{self.nome}\" {self.email} {self.telefone}"

        def obterNomeDaClasse(self):
                return type(self).__name__

        def printarAgenda(self, mes, dia):
                for i in range(len(horarioDeFuncionamento)):
                        marca = i
                        for horario in listaDeHorariosAgendados:
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

                self.printarServicosCurto()
                servicoEscolhido = listaDeServicos[int(input("Selecione o serviço: "))]
                print("Você escolheu: ",servicoEscolhido.nome)

                for profissional in listaDeProfissionais:
                        if servicoEscolhido in profissional.servicos:
                                profissionalEscolhido = profissional
                                break
                listaDeHorariosAgendados.append(
                        HorarioAgendado(mes,dia,hora,servicoEscolhido,self,profissionalEscolhido)
                        )
                self.horariosAgendados.append(listaDeHorariosAgendados[-1])


        def verMeusHorarios(self):
                print(f"Você tem {len(self.horariosAgendados)} horário(s).")
                for i in range(len(self.horariosAgendados)):
                        print(f"[{i+1}] Mês {self.horariosAgendados[i].mes} " +
                              f"dia {self.horariosAgendados[i].mes} " +
                              f"às {self.horariosAgendados[i].hora}: " +
                              f"R$ {self.horariosAgendados[i].valorTotal} " +
                              f"{self.horariosAgendados[i].servico.nome} "
                              # Que pesadelo ^^
                        )


        def printarServicosCurto(self):
                i = 0
                for servico in listaDeServicos:
                        print(f"[{i}] {servico.nome}")
                        i += 1


        def printarServicosCompleto(self):
                i = 0
                for servico in listaDeServicos:
                        print(f"[{i}] {servico}")
                        i += 1



class Profissional(Cliente):
        def __init__(self,cpf,nome,email,telefone,senha,servicos):
                self.cpf = cpf
                self.nome = nome
                self.email = email
                self.telefone = telefone
                self.senha = senha
                self.horariosAgendados = []
                self.servicos = servicos
        

        def __repr__(self):
                return self.nome
        

        def printarAgenda(self, mes, dia):
                for i in range(len(horarioDeFuncionamento)):
                        apendice = "Livre!"
                        for horario in listaDeHorariosAgendados:
                                if horario.hora == horarioDeFuncionamento[i] \
                                and horario.mes == mes and horario.dia == dia:
                                        apendice = f"{horario.profissional} -> " + \
                                        f"{horario.cliente.nome}"
                                        break
                        print(f"[ {i} ] {horarioDeFuncionamento[i]} ({apendice})")


        def adicionarServico(self, servico):
                self.servicos.append(servico)
                for i in range(len(listaDeServicos)):
                        if listaDeServicos[i] == servico:
                                listaDeServicos[i].profissionaisResponsaveis.append(self)

"""
RELATÓRIO DO MÊS 12
Dia 1:
 * TOTAL: R$ 120, x horários
 * Corte: R$ 20; 1 horário(s)
 * Manicure: R$ 75; 3 horário(s)

Dia 2:
 * ...
 * ...
"""

class Administrador(Profissional):
        def __init__(self,cpf,nome,email,telefone,senha):
                self.cpf = cpf
                self.nome = nome
                self.email = email
                self.telefone = telefone
                self.senha = senha

        def gerarRelatorio(self,mes,diaDeInicio,diaDeFim):
                lucroTotal = 0
                demandasTotal = 0
                for horario in listaDeHorariosAgendados:
                        if horario.mes == mes and diaDeInicio <= int(horario.dia) <= diaDeFim:
                                lucroTotal += float(horario.valorTotal)
                                demandasTotal += 1
                print(f"RELATÓRIO DO MÊS {mes}, DIA {diaDeInicio}-{diaDeFim}")
                for i in range(diaDeInicio,diaDeFim):
                        print(f"Dia {i}:\n * TOTAL: R$ {lucroTotal}; {demandasTotal} horário(s)")
                        for j in range(listaDeServicos):





        def printarClientesCompleto(self):
                for i in range(len(listaDeClientes)):
                        print(f"[{i}] {listaDeClientes[i]}")


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


        def printarHorariosAgendados(self):
                i = 0
                for horario in listaDeHorariosAgendados:
                        print(f"[{i}] {horario.dia}/{horario.mes} {horario.hora} -- " + \
                                f"{horario.cliente.nome} "
                                f"({horario.servico.nome} com {horario.profissional.nome})"
                        )
                        i += 1


        def editarServico(self):
                self.printarServicosCompleto()
                indiceDoServico = int(input("Serviço: "))
                print("Você escolheu:",listaDeServicos[indiceDoServico].nome)
                nome = input("Nome: ")
                valor = input("Valor: ")
                profissionais = []
                self.printarProfissionaisCurto()
                indicesDosProfissionais = input("Profissionais (e.g. 12): ")
                for i in indicesDosProfissionais:
                        profissionais.append(listaDeProfissionais[int(i)])
                listaDeServicos[indiceDoServico] = Servico(nome,valor,profissionais)


        def cadastrarServico(self):
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
                        listaDeServicos[-1].adicionarProfissional(listaDeProfissionais[int(i)])


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

                self.printarServicosCurto()
                indiceDosServicos = input("Digite o(s) serviço(s) realizado(s) (e.g. 134): ")
                for i in indiceDosServicos:
                        servicos.append(listaDeServicos[int(i)])

                listaDeProfissionais.append(
                        Profissional(cpf,nome,email,telefone,senha,servicos)
                )
                for i in indiceDosServicos:
                        listaDeServicos[int(i)].adicionarProfissional(listaDeProfissionais[-1])
                print("Cadastrado.")


        def editarHorario(self):
                self.printarHorariosAgendados()
                indiceDoHorario = int(input("Horario: "))
                horarioAntigo = listaDeHorariosAgendados[indiceDoHorario]
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

                horarioNovo = HorarioAgendado(mes,dia,hora,servico,cliente,profissional)
                # Atualizar o horário do cliente
                i = 0
                for horario in cliente.horariosAgendados:
                        if horario.mes == horarioAntigo.mes \
                        and horario.dia == horarioAntigo.dia \
                        and horario.hora == horarioAntigo.hora:
                                listaDeClientes[indiceDoCliente].horariosAgendados[i] = horarioNovo
                                break
                        i += 1
                # Atualizar o horário do Profissional
                i = 0
                for horario in profissional.horariosAgendados:
                        if horario.mes == horarioAntigo.mes \
                        and horario.dia == horarioAntigo.dia \
                        and horario.hora == horarioAntigo.hora:
                                listaDeProfissionais[indiceDoProfissional].horariosAgendados[i] \
                                = horarioNovo
                                break
                        i += 1
                # Atualizar o horário em si
                listaDeHorariosAgendados[indiceDoHorario] = horarioNovo




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
                for i in range(len(listaDeProfissionais)):
                        if listaDeProfissionais[i] == profissional:
                                listaDeProfissionais[i].servicos.append(self)



class HorarioAgendado:
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
        Cliente("012.012","John Cliente","john@email","012","john"),
        Cliente("117.117","Cristiano Ronaldo","CR7@email","117","cr7"),
        Cliente("211.211","Waltrik","waltrik@email","211","waltrik"),
        Cliente("343.343","Karyna","karyna@email","343","karyna"),
        Cliente("465.465","Sabrina","sabrina@email","465","sabrina"),
        Cliente("512.512","Alguém","alguem@email","512","alguem")
]
listaDeServicos = [
        Servico("Corte de cabelo",20.0,[]),
        Servico("Barba",15.0,[]),
        Servico("Manicure",20.0,[]),
        Servico("Progressiva",70.0,[]),
        Servico("Cílios",30.0,[])
]
listaDeProfissionais = [
        Profissional("000.000","Jane Cortes","jane@email","111","jane",[]),
        Profissional("111.111","Fulano Mãos","Fulano@email","222","fulano",[]),
        Profissional("222.222","Kauan","kauan@email","333","kauan",[]),
        Profissional("333.333","Faz-tudo da Silva","faztudo@email","333","faztudo",[])
]
contaDoAdmin = Administrador("admin","Admin","admin@penaareia","0","admin")

listaDeProfissionais[0].adicionarServico(listaDeServicos[0])
listaDeProfissionais[0].adicionarServico(listaDeServicos[3])
listaDeProfissionais[0].adicionarServico(listaDeServicos[4])

listaDeProfissionais[1].adicionarServico(listaDeServicos[2])

listaDeProfissionais[2].adicionarServico(listaDeServicos[3])
listaDeProfissionais[2].adicionarServico(listaDeServicos[4])

listaDeProfissionais[3].adicionarServico(listaDeServicos[0])
listaDeProfissionais[3].adicionarServico(listaDeServicos[1])
listaDeProfissionais[3].adicionarServico(listaDeServicos[2])
listaDeProfissionais[3].adicionarServico(listaDeServicos[3])
listaDeProfissionais[3].adicionarServico(listaDeServicos[4])

listaDeHorariosAgendados = [
        HorarioAgendado(
        "12","1","10:00",listaDeServicos[0],listaDeClientes[0],listaDeProfissionais[0]
        ),
        HorarioAgendado(
        "12","1","11:00",listaDeServicos[0],listaDeClientes[1],listaDeProfissionais[0]
        ),
        HorarioAgendado(
        "12","1","11:30",listaDeServicos[1],listaDeClientes[2],listaDeProfissionais[3]
        ),
        HorarioAgendado(
        "12","1","16:30",listaDeServicos[2],listaDeClientes[4],listaDeProfissionais[1]
        ),
        HorarioAgendado(
        "12","1","17:30",listaDeServicos[2],listaDeClientes[1],listaDeProfissionais[0]
        ),
        HorarioAgendado(
        "12","2","14:00",listaDeServicos[2],listaDeClientes[1],listaDeProfissionais[0]
        ),
        HorarioAgendado(
        "12","2","15:30",listaDeServicos[3],listaDeClientes[1],listaDeProfissionais[0]
        ),
        HorarioAgendado(
        "12","2","16:30",listaDeServicos[3],listaDeClientes[1],listaDeProfissionais[0]
        ),

]
listaDeClientes[0].horariosAgendados.append(listaDeHorariosAgendados[0])
listaDeProfissionais[0].horariosAgendados.append(listaDeHorariosAgendados[0])


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
                print("  =======================================  ")
                print("||         Você é administrador!         ||")
                print("||                                       ||")
                print("||---------------------------------------||")
                print("||                                       ||")
                print("|| [1] Ver clientes                      ||")
                print("|| [2] Ver serviços                      ||")
                print("|| [3] Ver agenda                        ||")
                print("||                                       ||")
                print("|| [4] Editar serviço                    ||")
                print("|| [5] Editar horario                    ||")
                print("||                                       ||")
                print("|| [6] Cadastrar profissional            ||")
                print("|| [7] Cadastrar serviço                 ||")
                print("||                                       ||")
                print("|| [8] Relatório de demandas             ||")
                print("|| [9] Relatório de lucros               ||")
                print("||                                       ||")
                print("|| [0] Sair                              ||")
                print("||                                       ||")
                print("  =======================================  ")
                key = input("Opção: ")
                match key:
                        case "1":
                                contaDoAdmin.printarClientesCompleto()
                        case "2":
                                contaDoAdmin.printarServicosCompleto()
                        case "3":
                                contaDoAdmin.printarAgenda(input("Mês: "),input("Dia: "))
                        case "4":
                                contaDoAdmin.editarServico()
                        case "5":
                                contaDoAdmin.editarHorario()
                        case "6":
                                contaDoAdmin.cadastrarProfissional()
                        case "7":
                                contaDoAdmin.cadastrarServico()
                        case "8":
                                contaDoAdmin.gerarRelatorio(input("12"),input("1"),input("7"))
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

