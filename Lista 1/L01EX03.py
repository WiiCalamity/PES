'''
3 – Construa um algoritmo que solicite o nome de usuário e a senha. Se o nome de
usuário for igual a "admin" e a senha for igual a "12345", exiba "Login bem-sucedido".
Caso contrário, exiba "Nome de usuário ou senha incorretos".
'''

usuario = str(input("usuário: "))
senha = str(input("senha: "))

while loginSucedido == 0:
    if usuario == "admin" and senha == "12345":
     print("Login bem-sucedido!")
     loginSucedido=1
    else:
        print("Nome de usuário ou senha incorreto(s). Tente novamente")