# Receber dez números multiplicar por outro número guardar em um vetor m e imprimir m

a = [0] * 10
m = [0] * 10
tam = len(a)
for i in range(tam):
    a[i] = int(input('Digite um número: '))

x = int(input("Digite um multiplicador: "))

for g in range(tam):
    m[g] = a[g] * x

for o in range(tam):
    print(m[o], end=" ")
