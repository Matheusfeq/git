ins = int(input("Insira '1' se quiser converter um número gray para binário ou '2' se quiser converter um número binário para gray: "))
lista = []
def split(a):
    return[char for char in a]

if ins == 1:
    x = input("Digite o número gray: ")
    
    for i in range(0,len(x) - 1):
        if x[i] == 1:
            lista.append(x[i])
            print(lista)
        elif x[i] == 0:
            pass
            
