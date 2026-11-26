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
Roteiro:
Criar uma conta
ver servicos
Marcar um horário
Logar como profissional
Ver meu horario
logar como admin
editar meu horario
gerar relatorio
ver mais coisas
POR FAVOR ARRUMA O AGENDARHORARIO QIE ESTÁ ATRELANDO A HORA ERRADO
"""


###################################
#  ____ _                         #
# / ___| | __ _ ___ ___  ___  ___ #
#| |   | |/ _` / __/ __|/ _ \/ __|#
#| |___| | (_| \__ \__ \  __/\__ \#
# \____|_|\__,_|___/___/\___||___/#
###################################

class Cliente:
        contagemDeInstancias = 0
        def __init__(self,cpf,nome,email,telefone,senha):
                self.id = Cliente.contagemDeInstancias
                self.cpf = cpf
                self.nome = nome
                self.email = email
                self.telefone = telefone
                self.senha = senha
                self.horariosAgendados = []
                Cliente.contagemDeInstancias += 1


        def __repr__(self):
                pad1 = " "*(15-len(self.nome))
                pad2 = " "*(15-len(self.email))
                return f"{self.cpf}: \"{self.nome}\"{pad1} {self.email}{pad2} {self.telefone}"


        def obterNomeDaClasse(self):
                return type(self).__name__


        def printarAgenda(self, mes, dia, servicoIndisponivel=True):
                j = -1
                k = 0
                for i in range(len(horarioDeFuncionamento)):
                        j += 1
                        skip = False
                        for horario in listaDeHorariosAgendados:
                                if horario.hora == horarioDeFuncionamento[i] \
                                and horario.servico == servicoIndisponivel \
                                and horario.mes == mes and horario.dia == dia:
                                        print("[ - ] --:-- (indisponível)")
                                        skip = True
                                        j -= 1
                                        k += 1
                                        break
                        if skip: continue
                        print(f"[ {j} ] {horarioDeFuncionamento[i]}")
                return k


        def agendarHorario(self):
                mesSelecionado = input("Digite o mês (e.g. 12): ")
                if int(mesSelecionado) <= 0 or int(mesSelecionado) > 12: print("NÃO"); return
                diaSelecionado = input("Digite o dia (e.g. 1): ")
                if int(diaSelecionado) <= 0 or int(diaSelecionado) > 31: print("NÃO"); return

                self.printarServicosCurto()
                servicoEscolhido = listaDeServicos[int(input("Selecione o serviço: "))]

                self.printarAgenda(mesSelecionado, diaSelecionado, servicoEscolhido)
                horaSelecionada = horarioDeFuncionamento[int(input("Selecione a hora: "))]

                menorQuantiaDeHorariosAgendados = float("inf")
                for profissional in listaDeProfissionais:
                        if not servicoEscolhido in profissional.servicos:
                                continue
                        if len(profissional.horariosAgendados) < menorQuantiaDeHorariosAgendados:
                                # Escolher o profissional menos ocupado
                                profissionalEscolhido = profissional
                                menorQuantiaDeHorariosAgendados=len(profissional.horariosAgendados)

                listaDeHorariosAgendados.append(
                        HorarioAgendado(
                               mesSelecionado,diaSelecionado,horaSelecionada,
                                servicoEscolhido,self,profissionalEscolhido
                        )
                )
                self.horariosAgendados.append(listaDeHorariosAgendados[-1])
                listaDeProfissionais[profissionalEscolhido.id].horariosAgendados.append(
                        listaDeHorariosAgendados[-1]
                )


        def agendarHorarioAntigo(self):
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
                print("Você escolheu:",servicoEscolhido.nome)

                for profissional in listaDeProfissionais:
                        for horario in profissional.horariosAgendados:
                                if servicoEscolhido in profissional.servicos \
                                and horario.mes != mes and horario.dia != dia \
                                and horario.hora != hora:
                                        profissionalEscolhido = profissional
                                        break
                listaDeHorariosAgendados.append(
                        HorarioAgendado(
                                mes,dia,hora,servicoEscolhido,self,profissionalEscolhido
                        )
                )
                self.horariosAgendados.append(listaDeHorariosAgendados[-1])


        def verMeusHorarios(self):
                print(f"Você tem {len(self.horariosAgendados)} horário(s).")
                for i in range(len(self.horariosAgendados)):
                        print(f"[{i+1}] Mês {self.horariosAgendados[i].mes} " +
                              f"dia {self.horariosAgendados[i].dia} " +
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
        contagemDeInstancias = 0
        def __init__(self,cpf,nome,email,telefone,senha,servicos):
                self.id = Profissional.contagemDeInstancias
                self.cpf = cpf
                self.nome = nome
                self.email = email
                self.telefone = telefone
                self.senha = senha
                self.horariosAgendados = []
                self.servicos = servicos
                Profissional.contagemDeInstancias += 1
        

        def __repr__(self):
                return self.nome
        

        def printarAgenda(self, mes, dia):
                for i in range(len(horarioDeFuncionamento)):
                        pad = " "*(3-len(str(i)))
                        apendice = "(Livre!)"
                        for horario in listaDeHorariosAgendados:
                                if horario.hora == horarioDeFuncionamento[i] \
                                and horario.mes == mes and horario.dia == dia:
                                        apendice = f"{horario.profissional}"
                                        break
                        print(f"[{i}]{pad}{horarioDeFuncionamento[i]} {apendice}")


        def adicionarServico(self, servico):
                self.servicos.append(servico)
                for i in range(len(listaDeServicos)):
                        if listaDeServicos[i] == servico:
                                listaDeServicos[i].profissionaisResponsaveis.append(self)



class Administrador(Profissional):
        def __init__(self,cpf,senha):
                self.cpf = cpf
                self.senha = senha


        def printarClientesCompleto(self):
                i = 0
                for cliente in listaDeClientes:
                        print(f"[{i}] {cliente}")
                        i += 1


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
                        print(f"[{i}] {horario.dia}/{horario.mes} {horario.hora} -- " +\
                        f"{horario.cliente.nome} " + \
                        f"({horario.servico.nome} com {horario.profissional.nome})"
                        )
                        i += 1


        def importarPickle(self):
                global listaDeClientes
                global listaDeProfissionais
                global listaDeServicos
                global listaDeHorariosAgendados
                listaDeClientes = pickle.load(open(
                        "DadosPickle/peNaAreia_clientes","wb")
                )
                listaDeProfissionais = pickle.load(open(
                        "DadosPickle/peNaAreia_profissionais","rb")
                )
                listaDeServicos = pickle.load(open(
                        "DadosPickle/peNaAreia_servicos","rb")
                )
                listaDeHorariosAgendados = pickle.load(open(
                        "DadosPickle/peNaAreia_horarios","rb")
                )
                print("Importado.")


        def exportarPickle(self):
                pickle.dump(listaDeClientes, open(
                        "DadosPickle/peNaAreia_clientes.pkl", "wb")
                )
                pickle.dump(listaDeProfissionais, open(
                        "DadosPickle/peNaAreia_profissionais.pkl", "wb")
                )
                pickle.dump(listaDeServicos, open(
                        "DadosPickle/peNaAreia_servicos.pkl", "wb")
                )
                pickle.dump(listaDeHorariosAgendados, open(
                        "DadosPickle/peNaAreia_horarios.pkl", "wb")
                )
                print("Exportado.")


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
                listaDeServicos.append(Servico(nome,valor,[]))

                for profissional in listaDeProfissionais:
                        print(f"[{profissional.id}] {profissional.nome} ({profissional.cpf})")
                idDosProfissionais = input(
                        "(em branco para nao atrelar)\n"
                        "Digite o(s) profissional(s) que realiza(m) o serviço (e.g. 134): ")
                for id in idDosProfissionais:
                        listaDeServicos[-1].adicionarProfissional(listaDeProfissionais[int(id)])


        def gerarRelatorio(self,mes,diaDeInicio,diaDeFim):
                print(f"\nRELATÓRIO DO MÊS {mes}, DIA {diaDeInicio} até {diaDeFim}")
                lucroTotal = 0
                horariosAgendados = 0
                horariosRelevantes = []
                for horario in listaDeHorariosAgendados:
                        if horario.mes == mes and diaDeInicio <= int(horario.dia) <= diaDeFim:
                                horariosRelevantes.append(horario)
                                lucroTotal += float(horario.valorTotal)
                                horariosAgendados += 1
                print(f"\nHorários agendados: {horariosAgendados}" + \
                        f"\nLucro total: R$ {lucroTotal}\n")
                for servico in listaDeServicos:
                        pad = " "*(20-len(servico.nome)) # Bom para os olhos
                        lucro = 0
                        horariosAgendados = 0
                        for horario in horariosRelevantes:
                                if horario.servico == servico:
                                        lucro += horario.valorTotal
                                        horariosAgendados += 1
                        print(f"{servico.nome}:{pad}{horariosAgendados} horário(s) -- R$ {lucro}")


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
                                listaDeClientes[indiceDoCliente].horariosAgendados[i]=horarioNovo
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
        contagemDeInstancias = 0
        def __init__(self,nome,valor,profissionaisResponsaveis):
                self.id = Servico.contagemDeInstancias
                self.nome = nome
                self.valor = valor
                self.profissionaisResponsaveis = profissionaisResponsaveis
                Servico.contagemDeInstancias += 1


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
        contagemDeInstancias = 0
        def __init__(self,mes,dia,hora,servico,cliente,profissional):
                self.id = HorarioAgendado.contagemDeInstancias
                self.mes = mes
                self.dia = dia
                self.hora = hora
                self.servico = servico
                self.valorTotal = servico.valor
                self.cliente = cliente
                self.profissional = profissional
                HorarioAgendado.contagemDeInstancias += 1


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
        Cliente("117.117","Cristiano","CR7@email","117","cr7"),
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
        Profissional("000.000","Jane Cortes","jane@email","000","jane",[]),
        Profissional("111.111","Fulano Mãos","Fulano@email","111","fulano",[]),
        Profissional("222.222","Kauan","kauan@email","222","kauan",[]),
        Profissional("333.333","Faz-tudo da Silva","faztudo@email","333","faztudo",[])
]
contaDoAdmin = Administrador("admin","admin")

# Isso aqui é muito feio por favor pula pro próximo cabeçalho

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
        "12","1","11:30",listaDeServicos[1],listaDeClientes[2],listaDeProfissionais[1]
        ),
        HorarioAgendado(
        "12","1","17:30",listaDeServicos[2],listaDeClientes[1],listaDeProfissionais[2]
        ),
        HorarioAgendado(
        "12","2","14:00",listaDeServicos[2],listaDeClientes[4],listaDeProfissionais[3]
        ),
        HorarioAgendado(
        "12","2","15:30",listaDeServicos[4],listaDeClientes[5],listaDeProfissionais[3]
        )

]
listaDeClientes[0].horariosAgendados.append(listaDeHorariosAgendados[0])
listaDeProfissionais[0].horariosAgendados.append(listaDeHorariosAgendados[0])

listaDeClientes[1].horariosAgendados.append(listaDeHorariosAgendados[1])
listaDeProfissionais[0].horariosAgendados.append(listaDeHorariosAgendados[1])

listaDeClientes[2].horariosAgendados.append(listaDeHorariosAgendados[2])
listaDeProfissionais[0].horariosAgendados.append(listaDeHorariosAgendados[2])

listaDeClientes[1].horariosAgendados.append(listaDeHorariosAgendados[3])
listaDeProfissionais[0].horariosAgendados.append(listaDeHorariosAgendados[3])

listaDeClientes[4].horariosAgendados.append(listaDeHorariosAgendados[4])
listaDeProfissionais[3].horariosAgendados.append(listaDeHorariosAgendados[4])

listaDeClientes[5].horariosAgendados.append(listaDeHorariosAgendados[5])
listaDeProfissionais[3].horariosAgendados.append(listaDeHorariosAgendados[5])


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


def gerarId(lista):
        return len(lista)


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
login = None

# Para pular o login
#login = listaDeClientes[0]
#login = listaDeProfissionais[0]
#login = contaDoAdmin
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

        while login == contaDoAdmin:
                clear()
                print("  ================================  ")
                print("||      Você é administrador!     ||")
                print("||                                ||")
                print("||--------------------------------||")
                print("||                                ||")
                print("|| [1]  Ver clientes 👥           ||")
                print("|| [2]  Ver serviços 💇           ||")
                print("|| [3]  Ver agenda 📒             ||")
                print("|| [4]  Ver horários ⏰           ||")
                print("||                                ||")
                print("|| [5]  Editar serviço 💇         ||")
                print("|| [6]  Editar horario ⏰         ||")
                print("||                                ||")
                print("|| [7]  Cadastrar profissional 👥 ||")
                print("|| [8]  Cadastrar serviço 💇      ||")
                print("||                                ||")
                print("|| [9]  Gerar relatório 📝        ||")
                print("||                                ||")
                print("|| [10]  Importar Pickle 🥒        ||")
                print("|| [11] Exportar Pickle 🥒        ||")
                print("||                                ||")
                print("|| [0]  Sair ◀️                    ||")
                print("||                                ||")
                print("  ===============================  ")
                key = input("Opção: ")
                match key:
                        case "1":
                                contaDoAdmin.printarClientesCompleto()
                        case "2":
                                contaDoAdmin.printarServicosCompleto()
                        case "3":
                                contaDoAdmin.printarAgenda(input("Mês: "),input("Dia: "))
                        case "4":
                                contaDoAdmin.printarHorariosAgendados()
                        case "5":
                                contaDoAdmin.editarServico()
                        case "6":
                                contaDoAdmin.editarHorario()
                        case "7":
                                contaDoAdmin.cadastrarProfissional()
                        case "8":
                                contaDoAdmin.cadastrarServico()
                        case "9":
                                contaDoAdmin.gerarRelatorio(
                                        input("Mês: "),
                                        int(input("Dia inicial: ")),
                                        int(input("Dia final: "))
                                )
                        case "10":
                                contaDoAdmin.importarPickle()
                        case "11":
                                contaDoAdmin.exportarPickle()
                        case "0":
                                break
                prosseguir()

        while login.obterNomeDaClasse() == "Profissional":
                clear()
                print(f"Olá, {login.nome}.         ")
                print(f"  ===========================  ")
                print(f"||                           ||")
                print(f"|| [1] Ver agenda 📒         ||")
                print(f"|| [2] Ver meus horários ⏰  ||")
                print(f"||                           ||")
                print(f"|| [3] Listar serviços 💇    ||")
                print(f"||                           ||")
                print(f"|| [0] Sair ◀️                ||")
                print(f"||                           ||")
                print(f"  ===========================  ")
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
                                login.printarServicosCompleto()
                        case "0":
                                break
                prosseguir()

        while login.obterNomeDaClasse() == "Cliente":
                clear()
                print(f"Olá, {login.nome}.         ")
                print(f"  ==========================  ")
                print(f"||                          ||")
                print(f"|| [1] Agendar horário 📝   ||")
                print(f"|| [2] Ver meus horários ⏰ ||")
                print(f"||                          ||")
                print(f"|| [3] Listar serviços 💇   ||")
                print(f"||                          ||")
                print(f"|| [0] Sair ◀️              ||")
                print(f"||                          ||")
                print(f"  ==========================  ")
                key = input("Opção: ")
                match key:
                        case "1":
                                login.agendarHorario()
                        case "2":
                                login.verMeusHorarios()
                        case "3":
                                login.printarServicosCompleto()
                        case "0":
                                break
                prosseguir()
        login = None

