# Um código para ler 5 nomes de usuários e suas senhas e imprimir nome senha e posição no array
user = [''] * 5
pas = [''] * 5
tam = len(user)

for i in range(tam):
    user[i] = input("Digite seu nome: ")
    pas[i] = input("Digite sua senha: ")
for n in range(tam):
    print(f'Usuário: {user[n]} (Array: {n})\nSehna: {pas[n]} (Array: {n})')
