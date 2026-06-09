'''
3 – Construa um algoritmo que solicite o nome de usuário e a senha. Se o nome de
usuário for igual a "admin" e a senha for igual a "12345", exiba "Login bem-sucedido".
Caso contrário, exiba "Nome de usuário ou senha incorretos".
'''
import time
loginSucedido = bool() # Vazio significa falso

while not loginSucedido:
    usuario = str(input("Usuário: "))
    senha = str(input("Senha: "))
    time.sleep(1.5)

    if usuario == "admin" and senha == "12345":
     print("Login bem-sucedido!")
     loginSucedido = bool("true")
    else:
        print("Desculpe, Tente novamente.")
        time.sleep(1)
        print("(ctrl+c para interromper)")
        time.sleep(1)
time.sleep(1) # Eu amo o sleep!