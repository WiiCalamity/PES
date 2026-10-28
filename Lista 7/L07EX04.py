"""
4 - Exercício: Funcionario e ContratoDeTrabalho (1..1).
Objetivo: Modelar um 1..1 onde a "parte" (Contrato) é obrigatória e contém a lógica de
cálculo que o "todo" (Funcionario) utiliza.
Classes: ContratoDeTrabalho e Funcionario.
Regras:
• A classe ContratoDeTrabalho deve ter salario_bruto (float) e percentual_impostos
(float, ex: 0.11 para 11% de INSS).
• O ContratoDeTrabalho deve ter um método chamado valor_impostos que calcula e
retorna o valor exato do desconto (ex: salario_bruto * percentual_impostos).
• A classe Funcionario deve ter nome e cargo.
• Um Funcionario deve ter exatamente um ContratoDeTrabalho para ser criado
(1..1).
• O __init__ do Funcionario deve receber nome, cargo, e também o salario_bruto e o
percentual_impostos necessários para criar sua própria instância de
ContratoDeTrabalho (Composição). O atributo funcionario.contrato nunca pode ser
None.
• Crie um método chamado salario_liquido na classe Funcionario. Este método deve:
◦ Acessar o salario_bruto do seu contrato.
◦ Acessar o valor_impostos calculado pelo seu contrato.
◦ Retornar o salario_bruto menos o valor_impostos.
Seu programa principal deve ter um menu interativo onde se possa testar todos os
métodos de um objeto do tipo Funcionario. Faça, também, o Diagrama de Classes da sua
implementação final.
"""

class Contrato:
        def __init__(self, salarioBruto: float, taxaDeImposto: float):
                self.salarioBruto = salarioBruto
                self.taxaDeImposto = taxaDeImposto
        
        def obterValorDoImposto(self):
                return self.salarioBruto * self.taxaDeImposto


class Funcionario:
        def __init__(self, nome: str, cargo: str, salarioBruto: float, taxaDeImposto: float):
                self.nome = nome
                self.cargo = cargo
                self.contrato = Contrato(salarioBruto, taxaDeImposto)
        
        def __repr__(self):
                return f"Eu sou {self.nome}, "+\
                f"meu cargo é {self.cargo} "+\
                f"e eu ganho R$ {self.obterSalarioLiquido()}"

        def obterSalarioLiquido(self):
                return self.contrato.salarioBruto - self.contrato.obterValorDoImposto()


listaDeFuncionarios = [Funcionario("Thiago Waltrik", "Técnico do Campus", 3200, 0.11)]


while True:
        print("\n.---------------------------.")
        print("| 🏢 Minha Super Empresa 🛠️  | ")
        print("| [1] Cadastrar funcionário |  ")
        print("| [2] Listar funcionários   |  ")
        print("| [3] Listar salários       |  ")
        print("| [4] Mostrar diagrama      |  ")
        print("| [0] Sair                  |  ")
        print("'---------------------------'\n")
        opcao = input("Opção: ")
        
        match opcao:
                case "1":
                        nome = input("Nome: ")
                        cargo = input("Cargo: ")
                        salarioBruto = float(input("Salário bruto: "))
                        taxaDeImposto = float(input("Taxa de imposto: "))
                        listaDeFuncionarios.append(Funcionario(nome,cargo,salarioBruto,taxaDeImposto))
                        print("Cadastrado!")
                case "2":
                        indice = 0
                        for funcionario in listaDeFuncionarios:
                                indice += 1
                                print(f"[{indice}] {funcionario}")
                case "3":
                        indice = 0
                        for funcionario in listaDeFuncionarios:
                                indice += 1
                                print(f"[{indice}] {funcionario.obterSalarioLiquido()}")
                case "4":
                        print(" +-------------------------+            +-------------------------+")
                        print(" |        Contrato         |            |       Funcionário       |")
                        print(" |-------------------------|            |-------------------------|")
                        print(" | + salarioBruto          | 1        1 | + nome                  |")
                        print(" | + taxaDeImposto         |============| + cargo                 |")
                        print(" |-------------------------|            |-------------------------|")
                        print(" | + __init__()            |            | + __init__()            |")
                        print(" | + obterValorDoImposto() |            | + __repr__()            |")
                        print(" +-------------------------+            | + obterSalarioLiquido() |")
                        print("                                        +-------------------------+")
                case "0":
                        break

        input("<Enter> para continuar...")
