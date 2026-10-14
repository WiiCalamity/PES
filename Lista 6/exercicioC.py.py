class Estudante:
        def __init__(self,nome,idade):
                self.nome=nome
                self.idade=idade
        def __repr__(self):
                return f"Eu sou {self.nome} e eu tenho {self.idade} anos."

estudantes=[]

print("Adicionando estudantes...\n")
estudantes.append(Estudante("Kiara", 17))
estudantes.append(Estudante("Lourenço", 15))
estudantes.append(Estudante("Mariana", 17))
estudantes.append(Estudante("???", "??"))
for estudante in estudantes:
        print(estudante)

print("\nAlterando estudante 'Lourenço'...\n")
for estudante in estudantes:
        if estudante.nome!="Lourenço":
                continue
        estudante.nome="Lorenzo"
        estudante.idade=17
        break
for estudante in estudantes:
        print(estudante)

print("\nRemovendo estudante \"Kiara\"")
for estudante in estudantes:
        if estudante.nome=="Kiara":
                estudantes.remove(estudante)
for estudante in estudantes:
        print(estudante)