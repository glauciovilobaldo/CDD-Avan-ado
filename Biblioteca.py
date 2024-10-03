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