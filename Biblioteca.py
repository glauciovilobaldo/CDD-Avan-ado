def pira(num):
    for i in range(1, num + 1):
        for n in range(1,i+1):
            print(i, end= ' ')
        print()

def pirasim(num):
    for i in range(1, num + 1):
        for n in range(1,i+1):
            print(n, end= ' ')
        print()

def vogais(vow):
    cont = 0
    letras = 'aeiouAEIOU'
    for i in vow:
      if i in letras:
        cont +=1
    print(cont)

def somar(n1, n2, n3, n4, n5):
    soma = n1 +n2 +n3 + n4 + n5
    print(soma)
def soma(*numeros):
    plus = 0
    tam = len(numeros)
    for x in range(tam):
        plus += numeros[x]
    print(plus)

def letras(texto):
    cont = 0
    tam = len(texto)
    for i in texto:
        if i not in " ":
            cont += 1
    print(cont)
    for x in range(tam-1, -1,-1):
        print(texto[x], end="")

