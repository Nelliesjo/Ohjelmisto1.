gram = 1
luoti = gram * 13.3
naula = luoti * 32
leivisk = naula * 20

A_str = float(input("Anna luodit?"))
B_str = float(input("Anna naulat?"))
C_str = float(input("Anna leiviskt?"))

painpG = (int(A_str * leivisk) + int(B_str * luoti) + int(C_str * naula))

