"""
3 – Crie uma classe chamada ContaBancaria com:
• Atributos: titular e saldo.
• Um método chamado depositar que recebe um valor e adiciona ao saldo.
• Um método chamado sacar que recebe um valor e subtrai do saldo (não precisa
validar o saldo).
• Um método chamado mostrar_saldo que retorna o saldo atual.
Teste criando uma conta, fazendo depósitos, saques e exibindo o saldo.
"""
class ContaBancaria:
        def __init__(self,titular,saldo):
                self.titular=titular
                self.saldo=saldo

        def depositar(self,deposito):
                self.saldo+=deposito

        def sacar(self,saque):
                self.saldo-=saque

        def mostrarSaldo(self):
                return self.saldo
        
        def descrever(self):
                return f"O titular {self.titular} tem um saldo de R$ {self.saldo}"

contaDoWaltrik=ContaBancaria("Waltrik",6.0)

print(contaDoWaltrik.descrever(),"\n")

v=12
print(f"Depositando R$ {v} ao saldo...")
contaDoWaltrik.depositar(v)
print(contaDoWaltrik.descrever(),"\n")

v=512
print(f"Sacando R$ {v} do saldo...")
contaDoWaltrik.sacar(v)
print(contaDoWaltrik.descrever())
