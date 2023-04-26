#Listas
#Declarando

#   [0] [1]   [2]     [3]
m = [1, 2.0, "tres", True]

print(m)
print(m[0])
print(m[-1])

n = [123, 1.23, True, m]

print(n)
print(n[-1][0])




#Tamanho de uma List

#   [0] [1]   [2]     [3]
m = [1, 2.0, "tres", True]

print(m)
print( len(m) )




#Checar item dentro da lista

#   [0] [1]   [2]     [3]
m = [1, 2.0, "tres", True]

print(1 in m)
print("tres" in m)
print(3 in m)




#Parte da List

m = [1, 2.0, "tres", True]

print(m[  0  ])
print(m[0 : 2])
print(m[  : 2])
print(m[2 :  ])
print(m[ -1  ])
print(m[0 :-2])
print(m[-2: 0])

n = m[0 :-2]

print(n)




#Modificando valores da lista

m = [1, 2.0, "tres", True]

m[0] = 0

print(m)

m[1:3] = [1, "dois"]

print(m)

m[:3] = [False]

print(m)




#Adicionando e removendo itens

m = [1, 2.0, "tres", True]

m.insert(1, 1.5)
print(m)

m.append(False)
print(m)

m.extend([3, "dois", 1.0])
print(m)

m.remove(1)
print(m)

m.pop(0)
print(m)

m.clear()
print(m)




#Organizando Lists

n = [2, 1, 3, 5, 0, 4]
o = ["laranja", "maçã", "banana", "Banana", "abacaxi"]

n.sort()
o.sort()

print(n)
print(o)

n.sort( reverse=True )

print(n)




########################################################################
#Strings
#Diferenças entre aspas simples e duplas

a = "Teste teste"
b = 'Teste teste'

print(a)
print(b)




#Aspas triplas


c = """Teste com
tres aspas
nomeio"""


print(c)




#Caractere especifico numa String

d = "Palavra"

print(d[0])
print(d[1])
print(d[-1])
print(d[-2])




#Tamanho de uma String

e = "Quantos caracteres que essa frase tem?"

print(e)
print( len(e) )




#Palavra dentro de uma Sring

f = "Maçãs são melhores que bananas"

print("Maçãs" in f)
print("Laranjas" in f)
print("Bananas" in f)




#Cortando Strings

g = "Frase grande e complexa"

print(g[:12])      # print(g[0:12])

g = g[6:-11]

print(g)




#Mudando o conteudo

h = " Uma frase complexa com NUM3R05 "

print( h.upper() )
print( h.lower() )
print( h.strip() )
print( h.replace("o", "0") )
print( h.split(" com ") )




#Juntando duas Strings em uma só
i = "Olá"
j = "Mundo"

k = i + j
l = i + ", " + j

print(k)
print(l)
