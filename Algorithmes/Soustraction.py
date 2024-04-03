minuend = int(input('Tapez un nombre: ')) #l'utilisateur doit entrer un nombre(minuend) auquel on va soustraire le subtrahend
subtrahend = int(input('Tapez un deuxieme nombre: '))
minuendbin = int(bin(minuend)[2:])#on transforme les deux nombres en binaire
subtrahendbin = int(bin(subtrahend)[2:]) 

def subtraction(minuendbin,subtrahendbin):
    l_minuend = list(str(minuendbin)) #on transforme les nombres en listes
    l_subtrahend = list(str(subtrahendbin))
    l_minuend = l_minuend[::-1] #on inverse le sens des listes, donc les chiffres de plus petit ordre de grandeur sont au début
    l_subtrahend = l_subtrahend[::-1]
    l_complement=[] #l_complement sera la liste contenant le complement de 1 du subtrahend
    p=0
    if len(l_minuend) > len(l_subtrahend): #si l_minuend est plus long que l_subtrahend, on ajoute des 0 à la fin de l_subtrahend jusqu'à ce qu'elles aient la même longueur
        o = int(len(l_minuend)-len(l_subtrahend))
        r = 0
        while r < o:
            r = r + 1
            l_subtrahend.append('0')
    while p < len(l_subtrahend): #cette boucle permet de trouver le complement de 1 du subtrahend
            if int(l_subtrahend[p]) == 0:
                l_complement.append('1')
            if int(l_subtrahend[p]) == 1:
                l_complement.append('0')
            p = p + 1
    result_addition = addition(l_minuend,l_complement)
    un = [1]
    if len(result_addition) > len(un): #si l_minuend est plus long que l_subtrahend, on ajoute des 0 à la fin de l_subtrahend jusqu'à ce qu'elles aient la même longueur
        o = int(len(result_addition)-len(un))
        t = 0
        while t < o:
            t = t + 1
            un.append('0')
    result_addition = addition(result_addition, un)
    return result(result_addition)

def addition(x,y): #cette fonction additionne l_minuend et l_complement
    q = 0
    result = []
    carry = 0
    while q < len(x): #avec des comparaisons, cette boucle va ajouter à result les chiffres de la somme
        if int(x[q]) == 0:
            if int(y[q]) == 0 and carry == 0:
                result.append(0)
                carry = 0
            if int(y[q]) == 1 and carry == 0:
                result.append(1)
                carry = 0
            if int(y[q]) == 0 and carry == 1:
                result.append(1)
                carry = 0
            if int(y[q]) == 1 and carry == 1:
                result.append(0)
                carry = 1
        else:
            if int(y[q]) == 0 and carry == 0:
                result.append(1)
                carry = 0
            if int(y[q]) == 0 and carry == 1:
                result.append(0)
                carry = 1
            if int(y[q]) == 1 and carry == 1:
                result.append(1)
                carry = 1
            if int(y[q]) == 1 and carry == 0:
                result.append(0)
                carry = 1
        q = q + 1
    if carry == 1: #si à la fin de toutes les comparaisons il reste un carry de 1, on l'ajoute à la fin de la liste de la somme
        result.append(1)
    return result

def result(result_addition): #on inverse la liste pour obtenir le résultat final dans l'ordre correct
    result_addition = result_addition[::-1]
    somme=''
    for x in range(1,len(result_addition),1): 
        somme = somme + str(result_addition[x])
    somme = int(somme, 2) #on transforme le résultat en nombre décimal 
    return somme

if minuend >= subtrahend: #si le minuend est supérieur ou égal au subtrahend, on effectue une soustraction et on obtient un résultat positif
    print(minuend, '-', subtrahend, '=', subtraction(minuendbin,subtrahendbin))
else: #si le minuend est inférieur au subtrahend, on effectue une soustraction avec inversion et on obtient un résultat négatif
    minuendbin = int(bin(subtrahend)[2:])
    subtrahendbin = int(bin(minuend)[2:])
    print (minuend, '-', subtrahend,'= -', subtraction(minuendbin,subtrahendbin)) #on affiche la différence avec un signe négatif
