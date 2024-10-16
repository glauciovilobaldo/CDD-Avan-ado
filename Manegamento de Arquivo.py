def write(nome):
    with open('Nomes.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')
def read():
    with open('Nomes.txt', 'r') as arq:
        cont = arq.read()
        print(cont)

op = 0
while op != 3:
    op = int(input(f'Menu\n1 - Gravar\n2 - Mostrar\n3 - Sair:' ))
    if op == 1:
        write(input("Digite um nome: 0"))
    elif op == 2:
        read()
