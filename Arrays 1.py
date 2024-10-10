# Cria uma lista de nome de 5 alunos informados pelo usuário
Nome = ['','','','','']
tamanho = len(Nome)
for i in range (tamanho):
    Nome[i] = input("Digite o nome do aluno: ")
for x in range(tamanho):
    print(Nome[x],x)