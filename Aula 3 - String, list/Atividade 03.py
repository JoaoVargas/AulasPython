#Atividade 03

listaDesafio1 = ["por", 1234-2211, "parabens", "ERROR", False, False, "responder", False, "ultimo item????????", "não", "esse é o ultimo item"]
listaDesafio2 = ["corretamente", False ,"desafio", False]

listaDesafio1.pop(-1)
listaDesafio1.pop(-1)
listaDesafio1.pop(-1)
listaDesafio1.remove("ERROR")
listaDesafio1.remove(False)
listaDesafio1.remove(False)
listaDesafio1.remove(False)
listaDesafio2.remove(False)
listaDesafio2.remove(False)
listaDesafio1.pop(1)
listaDesafio1.sort()
listaDesafio2.insert(1, "o")
listaDesafio1.extend(listaDesafio2)

print(listaDesafio1)