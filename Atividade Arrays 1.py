'''Faça um sistema de login, pedindo a  senha do usuário e mostrando seu nome e a mensagem,
login efetuado com sucesso.'''


user = [0] * 5
senha = [0] * 5
tam = len(user)
t = 0
while t != 4:
    t = int(input(f'Menu\n1-Cadastro\n2-Login\n3-Mostrar usuário\n4-Sair: '))
    if t == 1:
        for i in range (tam):
            user[i] = input("Digite seu nome de usuário: ")
            senha[i] = input("Digite sua senha: ")
    elif t == 2:
        userlog = input("Digite o nome do usuário: ")
        for k in range (tam):
            if userlog == user[k]:
                print(f"Bem vindo {user[k]}")
                senhalog = input("Digite a Senha: ")
                if senhalog == senha[k]:
                    print("Login efetuado com sucesso!")
                    break
                else:
                    print("Senha incorreta.")
            else:
                print("Usuário inválido.")
                break
    elif t == 3:
        print("Usuários cadastrados: ")
        for n in range (tam):
            print(user[n])
