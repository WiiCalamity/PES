class Motor:
        def __init__(self, potenciaCv: float):
                self.potenciaCv = potenciaCv
                self.ligado = False

        def __repr__(self):
                return f"\n * Motor potência: {self.potenciaCv}\n * Ligado: {self.ligado}"

        def ligar(self):
                self.ligado = True

        def desligar(self):
                self.ligado = False

        def estaLigado(self):
                return self.ligado


class Carro:
        def __init__(self, modelo: str, ano: int, potenciaDoMotor: float):
                self.modelo = modelo
                self.ano = ano
                self.motorDoCarro = Motor(potenciaDoMotor)

        def __repr__(self):
                return f"Modelo: {self.modelo}\nAno: {self.ano}\nMotor: {self.motorDoCarro}"

        def ligarCarro(self):
                self.motorDoCarro.ligar()

        def desligarCarro(self):
                self.motorDoCarro.desligar()

        def estaLigado(self):
                return self.motorDoCarro.estaLigado()


# Criar um Carro
m = input("Digite o modelo: ")
a = int(input("Digite o ano: "))
p = float(input("Digite a potência (CV): "))
carrinho = Carro(m, a, p)

print("\nSeu carro\n")
print(carrinho)

print("\nLigando o carro...\n")
carrinho.ligarCarro()
print(carrinho)

print("\nDesligando o carro...\n")
carrinho.desligarCarro()
print(carrinho)
