ini = 1
fin= 6
quantidadeDeImpar = 0
lista = [2, 3, 4, 5]

for i in range(ini + 1, fin):
    if (i % 2 == 1):
        quantidadeDeImpar += 1
    
print(quantidadeDeImpar)