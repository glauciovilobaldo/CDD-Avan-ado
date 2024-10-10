# Receber 5 notas e mostar quantas notas estão acima da média
notas = [0.0] * 5
tam = len(notas)
soma = 0
cont = 0
for i in range(tam):
    notas[i] = float(input("Digite a notas: "))
for x in range(tam):
    soma = soma + notas[x]

media = soma / tam

for f in range(tam):
    if notas[f]>media:
        cont = cont + 1


print(f'A média da sala é {media} e {cont} alunos tem notas acima da média.')