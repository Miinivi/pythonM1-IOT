##Exo 1.1

a = 2
b = 3
c = a
a = b
b = c
print("a = ", a) #Check value a
print("b = ", b) #Check value b

##Exo 1.2

nbDem = int(input())
print("Carré de ", nbDem, " = ", nbDem * nbDem)

##Exo 1.3

nbDemBis = int(input())
if (nbDemBis < 0):
    print(nbDemBis, " est négatif")
else:
    print(nbDemBis, " est positif")

##Exo 1.4

nbD = int(input())
nbDb = int(input())
if ((nbD * nbDb) < 0):
    print("Produit négatif")
else:
    print("Produit positif")

##Exo 1.5

nbDD = int(input())
for i in range(10):
    print(nbDD+i+1)

##Exo 1.6

nbbDD = int(input())
somme = 0
sommeStr = "0"
for i in range(nbbDD+1):
    somme += i
    sommeStr += " + " + str(i)
print(sommeStr)
print(somme)
