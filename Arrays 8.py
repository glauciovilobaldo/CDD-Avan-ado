num =[0]*10
tam= len(num)

for x in range(tam):
    num[x] = int(input("Digite um número: "))

pares = [num for num in num if num%2==0]

for t in pares:
    print(t)

maior = num[0] #max(num)
menor = num[0] #min(num)
soma = 0
for i in range(tam):
    if maior < num[i]:
        maior = num[i]
    elif menor > num[i]:
        menor = num[i]
    soma = soma + num[i]

media = soma / tam
cont = 0
for t in range(tam):
    if num[t] > media:
        cont +=1
print(f'Os números acima da média são:{cont}')
print(f'O menor número é: {menor} \nO maior número é: {maior}')