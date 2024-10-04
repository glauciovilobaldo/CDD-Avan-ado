'''Faça um sistema de login, pedindo a  senha do usuário e mostrando seu nome e a mensagem,
login efetuado com sucesso.'''

#Não lembro exatamente como era para ser a atividade
user = [0] * 2
senha = [0] * 2
tam = len(user)
t = 0
while t != 4:
    login = False
    t = int(input(f'Menu\n1-Cadastro\n2-Login\n3-Mostrar usuário\n4-Sair: '))
    if t == 1:
        for i in range (tam):
            user[i] = input("Digite seu nome de usuário: ")
            senha[i] = input("Digite sua senha: ")
    elif t == 2:
        userlog = input("Digite o nome do usuário: ")
        senhalog = input("Digite a Senha: ")
        for k in range (tam):
            if userlog == user[k] and senhalog == senha[k]:
                print(f"Login efetuado com sucesso {user[k]}")
                login = True
                break
        if not login:
            print("Usuário e/ou senha inválidos")

    elif t == 3:
        print("Usuários cadastrados: ")
        for n in range (tam):
            print(user[n])

