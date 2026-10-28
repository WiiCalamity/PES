"""
2 - Exercício 2: Computador e CPU (1..1).
Objetivo: Implementar um relacionamento obrigatório (Composição).
Classes: CPU e Computador.
Regras:
A classe CPU deve ter atributos fabricante (ex: "Intel") e modelo (ex: "i7-12700K").
• A classe Computador deve ter um atributo tipo (ex: "Desktop" ou "Notebook").
• Um Computador deve ter exatamente uma CPU para ser criado (1..1).
• O __init__ do Computador deve receber os dados necessários para criar sua
própria instância de CPU. O atributo computador.cpu nunca pode ser None.
Comprove o funcionamento da sua implementação no programa principal.
Veja, na figura abaixo, o Diagrama de Classes completo:
"""

class Processador:
        def __init__(self, fabricante: str, modelo: str):
                self.fabricante = fabricante
                self.modelo = modelo

        def __repr__(self):
                return f"\n  * Fabricante: {self.fabricante}\n  * Modelo: {self.modelo}\n"


class Computador:
        def __init__(self, tipo: str, fabricanteDoProcessador: str, modeloDoProcessador: str):
                self.tipo = tipo
                self.processador = Processador(fabricanteDoProcessador, modeloDoProcessador)

        def __repr__(self):
                return f"Tipo: {self.tipo}\nProcessador: {self.processador}"


tipo = input("Tipo do computador (desktop/notebook): ")
fabricante = input("Fabricante da CPU: ")
modelo = input("Modelo da CPU: ")

print("\n-- Esse é o seu computador --")
meuPc = Computador(tipo, fabricante, modelo)
print(meuPc)

