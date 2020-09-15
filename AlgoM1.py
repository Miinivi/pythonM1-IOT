##Exo 1.1

a = 2
b = 3
#c = a
#a = b
#b = c
a,b = b,a 
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

##Exo 2.1

liste = [i for i in range(5)]
sommeListe = 0
for i in range(len(liste)):
    sommeListe += liste[i]
    #print("Liste, valeur de i, i = ", i, " : ", liste[i]) #Check list values
print(sommeListe) #Or sum(liste)

##Exo 2.2

liste2 = [i for i in range(5)]
liste3 = [0 for i in range(5)]
for i in range(len(liste)):
    liste3[i] = liste[i] + liste2[i]
print(liste3)

##Exo 2.3

liste4 = [0 for i in range(5)]
for i in range(len(liste)):
    liste4[i] = liste[i] * liste2[i]
print(sum(liste4))

##Exo 2.4

liste5 = [0 for i in range(3)]
for i in range(3):
    liste5[i] = int(input())

max = liste5[0]
for i in range(len(liste5)):
    if (liste5[i] > max):
        max = liste5[i]
print(max)





















