def typeerror():
    try:
        a = [0] * 4
        for i in range(a, 5):
            print(i)
    except TypeError:
        print("Lista não pode ser interpretado como inteiro.")

def indexerror():
    try:
        a = 'aaaaaaaaaaa'
        tam = len(a)
        for i in range(tam):
           print(a[-600])
    except IndexError:
        print("Erro de index.")
try:
    a = {1: 'Eliabe', 2:"Sega", 3: 'Atari'}
    print(a[4])
except KeyError:
    print("Não existe no dicionário.")