## Correction ##

## Exo 2.2

#V1

tab1=[1,2,3,4,5]
tab2=[2,3,3,4,5]
tab3=[0,0,0,0,0]
for i in range(len(tab3)):
    tab3[i]=(tab1[i]+tab2[i])
    print("Tab3 value : ",tab3[i])

#V2

liste = [i for i in range(5)]
liste2 = [i for i in range(5)]
liste3 = [0 for i in range(5)]
for i in range(len(liste)):
    liste3[i] = liste[i] + liste2[i]
print(liste3)

#V3

ttab1 = [2,2,4]
ttab2 = [4,5,6]
ttab3 = []
for i in range(len(ttab1)):
    ttab3.append(ttab1[i] + ttab2[i])
print(ttab3)

#V4

T,U = [0,2,7,3,1,8,100],[11,32,45,89,10,1,9]
[T[i]+U[i] for i in range(len(T))]

#V5

lliste1 = [1, 2, 3]
lliste2 = [4, 5, 6]
lliste3 = []
cmp = 0while (len(lliste1) > cmp) :
    lliste3.append(lliste1[cmp] + lliste2[cmp])
    cmp +=1print(lliste3)

## Exo 2.3

#V1

t1 = [x for x in range (5)]
t2 = [x for x in range (5)]for x in t2 :
        R = x*t1[x]
        print(R)

#V2

def fact_prod(liste1 : list, liste2 : list) -> float :     cmp = 0
    sum = 0
    while ((len(liste1) > cmp) and (len(liste2) > cmp)) :
        sum += (liste1[cmp] * liste2[cmp])
        cmp += 1
        if (len(liste1) == cmp and len(liste2) > cmp) :
            while (len(liste2) > cmp) :
                sum += liste2[cmp]
                cmp += 1
            print(sum)
        elif (len(liste2) == cmp and len(liste1) > cmp) :
            while (len(liste1) > cmp) :
                sum += liste1[cmp]
                cmp += 1
            print(sum)
        else :
        print(sum)

#V3

T,U = [0,2,7,3,1,8,100],[11,32,45,89,10,1,9]
R = [T[i]*U[i] for i in range(len(T))]
sum(R)

#V4

listInt = [1, 2, 3, 4, 5]
listInt2 = [9, 8, 7, 6, 5]
somme = 0
for indice, integer in enumerate(listInt):
    somme = integer + listInt2[indice]
    print(somme)

#V5

i = 0
facProduct = 0
for i in range(len(tab)):
    facProduct += tab[i] * tab2[i]print("FacProduct : {0}".format(facProduct))

#V6

def facproduct(t1: list, t2: list) ->float:
    N=0
    for i in range (len(t1)):
        N+=t1[i]*t2[i]
    return N

#V7

l1, l2 = [1, 3, 2, 4], [5, 7, 6, 8]
somme = 0for i in range(len(l1)):
    somme += l1[i] * l2[i]print(somme)

#V8

facproduit =0
for j in range(len(tab3)):
    tab3[j]+=(tab1[j]*tab2[j])
    print("Tab3 value : ",tab3[j]) 
    facproduit=sum(tab3)
    print("facproduit : {0}".format(facproduit))

#V9

def fact_prod() :
    b=0
    tab1= [i for i in range(2,12)]
    tab2= [i for i in range(10)]
    for i in range (len(tab1)):
        a=0
        a=tab1[i]*tab2[i]
        b+=a
    return b

#V10

def facProduct(tab : list, tab2 : list) -> float : 
    facProduct = 0
    i = 0
    for i in range(len(tab)):
        facProduct += tab[i] * tab2[i]
    return facProducttab = [1,2,3]
tab2 = [0,1,2]print("FacProduct : {0}".format(facProduct(tab, tab2)))

## Exo 2.4

#V1

def grand(taille: int,*nb: float)->float:
    g=0
    if(taille==len(nb)):
        for i in range (0,taille):
            if(g<nb[i]):
                g=nb[i]
        return g,i
    else : print("Taille differente du nombre d'arguments")

grand(6,1,34,3,12,5,38)

#V2

def Biggest_Input() -> float :    liste = []
    cmpWhile = 0
    cmp = 0
    result = 0
    print("Entrez les valeurs")
    while cmpWhile != 5 :
        liste.append(int(input("entrez un nombre : ")))
        cmpWhile += 1
        while (len(liste) > cmp) :
            if (liste[cmp] > result) :
                result = liste[cmp]
            cmp += 1
    return "Le nombre le plus élevé est : {}".format(result)

#V3

def getMax() -> float : 
    a = int(input("Entrer un nombre : "))
    b = int(input("Entrer un nombre : "))
    c = int(input("Entrer un nombre : "))
    tab = [a,b,c]
    maxi =tab[0]
    for i in range(len(tab)-1) :
        if tab[i+1] > maxi:
            maxi = tab[i+1]
    return maxiprint("Maximum : {0}".format(getMax()))

#V4

def grand(nbr:int)-> list:
    nbrmax,pos = 0,0
    for i in range(nbr):
        a = int(input())
        if a > nbrmax:
            nbrmax,pos=a,i
    return [nbrmax,pos]
grand(5)

