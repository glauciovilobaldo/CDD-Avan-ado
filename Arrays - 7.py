nomes = [''] * 5
tam = len(nomes)

for x in range(tam):
    nomes[x] = input('Digite seu nome: ')
print(nomes)
#nomes.reverse()
for i in range(tam-1,-1,-1):
    print(nomes[i])
