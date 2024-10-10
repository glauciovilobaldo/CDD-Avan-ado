num = [0] * 5
tam = len(num)
for i in range(tam):
    num[i] = int(input("Digite um número: "))

for x in range(tam-1, -1, -1):
    print(num[x])