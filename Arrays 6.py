"""Faça um código para ler dez números e guardar num vetor. Após isto, ler mais um número qulaquer,
calcular e escrever quantas vezes esse número aparece no vetor."""
num = [0] * 10
tam = len(num)
for i in range(tam):
    num[i] = int(input("Digite um número: "))

num2 = int(input('Digite um outro número: '))
cont = 0

for r in range(tam):
    if num2 == num[r]:
        cont += 1


print(f'O número {num2} apareçe {cont} vezes.')