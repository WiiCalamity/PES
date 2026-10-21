class CarteiraDeMotorista:
        def __init__(self,numero,categoria):
                self.numero = numero
                self.categoria = categoria

        def __repr__(self):
                return f"<CNH n° {self.numero}, categoria {self.categoria}>"


class Pessoa:
        def __init__(self,nome):
                self.nome = nome
                self.cnh = None

        def __repr__(self):
                return f"<Pessoa: {self.nome}; CNH: {self.cnh}>"

        def ehHabilitada(self):
                if self.cnh:
                        return True
        
        def tirarHabilitacao(self,numero,categoria):
                if self.ehHabilitada():
                        return
                self.cnh = CarteiraDeMotorista(numero, categoria)



sujeitoA=Pessoa("John Python")
print(f"Criando pessoa {sujeitoA}...")

print(f"{sujeitoA} tem habilitação?: {sujeitoA.ehHabilitada()}")

print(f"Criando carteira para {sujeitoA}...")
sujeitoA.tirarHabilitacao(123,"A")
print(f"{sujeitoA}")