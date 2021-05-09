#Mostrar a palavra mais frequente de uma frase
z = []
y = []
x = input("Digite uma frase: ").split(" ")
x.sort()
print(x)

for i in range(len(x)):    
    y.append(x.count(x[i]))
    if x.count(x[i]) == max(y):
        z.append(x[i])

print("A palavra que mais se repete é:",max(z))        
print("Ela se repete",max(y),"vezes")

    