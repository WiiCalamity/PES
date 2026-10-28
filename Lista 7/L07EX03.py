"""
3 - VagaDeEstacionamento e Carro (0..1 - Associação Simples)
Objetivo: Modelar um relacionamento 0..1 onde a "parte" (Carro) vem de fora
(Agregação/Associação).
Classes: Carro e VagaDeEstacionamento.
Regras:
A classe Carro é simples, tem apenas placa e modelo.
• A classe VagaDeEstacionamento tem um id_vaga (ex: "A-101").
• Uma VagaDeEstacionamento pode estar ocupada por zero ou um Carro (0..1). O
atributo carro_estacionado começa como None.
• Crie um método ocupar_vaga(carro_obj). Este método deve verificar se a vaga já
está None. Se estiver livre, associa o carro_obj (vindo de fora) à vaga e retorna
True. Se já estiver ocupada, não faz nada e retorna False.
• Crie um método liberar_vaga() que simplesmente seta carro_estacionado de volta
para None.
Seu programa principal deve ter um menu interativo onde se possa testar todos os
métodos de um objeto do tipo VagaDeEstacionamento. Faça, também, o Diagrama de
Classes da sua implementação final.
"""

class Carro:
        def __init__(self, placa: str, modelo: str):
                self.placa = placa
                self.modelo = modelo

        def __repr__(self):
                return f"{self.modelo} ({self.placa})"


class Vaga:
        def __init__(self, id: str):
                self.id = id
                self.carroEstacionado = None

        def __repr__(self):
                return f"{self.id}: {self.carroEstacionado}"

        def ocuparVaga(self, placa: str, modelo: str):
                if self.carroEstacionado:
                        return False
                self.carroEstacionado = Carro(placa, modelo)
                return True

        def liberarVaga(self):
                self.carroEstacionado = None



def estacionar():
        vaga = input("Vaga (e.g. A-101): ").upper()
        placa = input("Placa do carro: ").upper()
        modelo = input("Modelo do carro: ")
        for indice in range(len(listaDeVagas)):
                if listaDeVagas[indice].id == vaga:
                        break
        else:
                print("Vaga inválida...")
                return
        listaDeVagas[indice].ocuparVaga(placa, modelo)

def remover():
        vaga = input("Vaga (e.g. A-101): ").upper()
        for indice in range(len(listaDeVagas)):
                if listaDeVagas[indice].id == vaga:
                        break
        else:
                print("Vaga inválida...")
                return
        listaDeVagas[indice].liberarVaga()
        print("Carro removido.")


def listarVagas():
        for vaga in listaDeVagas:
                print(vaga)


def diagrama():
        print(" +--------------+                 +--------------------+ ")
        print(" |    Carro     |                 |        Vaga        | ")
        print(" |--------------|                 |--------------------| ")
        print(" | + placa      |  0           1  | + id               | ")
        print(" | + modelo     |=================|--------------------| ")
        print(" |--------------|                 | + __init__()       | ")
        print(" | + __init__() |                 | + __repr__()       | ")
        print(" | + __repr__() |                 | + ocuparVaga()     | ")
        print(" +--------------+                 | + liberarVaga()    | ")
        print("                                  +--------------------| ")


listaDeVagas = [Vaga("A-100"), Vaga("A-101"), Vaga("A-102"), Vaga("B-100"), Vaga("B-101")]
listaDeVagas[0].ocuparVaga("ABC1234", "Fusca do Rodolfo")
while True:
        print("\n  Estacionamento 🚗  ")
        print(" ------------------ ")
        print("1. Estacionar carro ")
        print("2. Remover carro    ")
        print("3. Listar vagas     ")
        print("4. Mostrar diagrama ")
        print("0. Sair             \n")
        opcao = input("Opção: ")

        match opcao:
                case "1":
                        estacionar()
                case "2":
                        remover()
                case "3":
                        listarVagas()
                case "4":
                        diagrama()
                case "0":
                        break
                case _:
                        print("\nOpção inválida! @w@")
        input("\n<Enter> para continuar... ")
