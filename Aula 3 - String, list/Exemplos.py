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






















