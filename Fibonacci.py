#Atividade 2
N = int(input("Digite um número: "))
an = 0
ln = 0

#Cálculo da sequência
if N > 0:
    for x in range (0, N + 1):

        if an != 0:
            print(str(an),end = " ")
        an += ln
        ln = an - ln

        if an == 0:
            an =+ 1                        
else:
    print("Número inválido")