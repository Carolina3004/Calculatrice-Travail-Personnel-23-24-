multiplicand = int(input('Tapez un nombre: '))#l'utilisateur doit entrer deux nombres pour les multiplier
multiplier = int(input('Tapez un deuxieme nombre: ')) 
multiplicandbin = int(bin(multiplicand)[2:])#on transforme les deux nombres en binaire
multiplierbin = int(bin(multiplier)[2:])

def multiplication(multiplicandbin,multiplierbin):
    l_multiplicand = list(str(multiplicandbin)) #on transforme les deux nombres en listes
    l_multiplier = list(str(multiplierbin))
    l_multiplier = l_multiplier[::-1] #on inverse le sens des listes
    l_multiplicand = l_multiplicand[::-1]
    product = 0
    for q in range(0,len(l_multiplier),1): #cette boucle multipliera les deux nombres
        partial_product = ''
        if int(l_multiplier[q]) == 0: #si le chiffre du multiplier est egal à 0, le produit partiel sera aussi égal à 0
            partial_product = 0
        else: #si le chiffre est égal à 1, le produit partiel sera égal au multiplicand
            partial_product = str(multiplicandbin)
            for n in range(0,q,1): #cette boucle permet de faire le deécalage des produits partiels en leur ajoutant des 0
                partial_product = partial_product + '0'
        partial_product = int(partial_product)
        addition(product,partial_product) #on additionne le produit partiel au produit
        product = result
    product = int(str(product),2) #on transforme le produit en nombre décimal
    return product

def addition(augendbin,addendbin): #cette fonction permet d'additionner le produit et le produit partiel
    l_augend = list(str(augendbin)) #chaque chiffre de augend a une case dans la liste l_augend
    l_addend = list(str(addendbin)) #chaque chiffre de addend a une case dans la liste l_addend
    l_augend = l_augend[::-1] 
    l_addend = l_addend[::-1]#on inverse le sens des listes
    sum = [] #on crée une liste vide
    q = 0 #on initialise un compteur 'q' à zéro
    
    if len(l_augend) != len(l_addend): #on assure que les deux listes ont la même longueur, en ajoutant des zéros à la fin de la liste la plus courte si nécessaire
        o = int(max(len(l_augend), len(l_addend)) - min(len(l_augend), len(l_addend)))
        s = 0
        while s < o:
            s = s + 1
            if len(l_augend) < len(l_addend):
                l_augend.append('0')
            else:
                l_addend.append('0')
    carry = 0
    while q < len(l_addend): #avec des comparaisons, cette boucle va ajouter à sum les chiffres de la somme (en chiffres binaires)
        if int(l_addend[q]) == 0:
            if int(l_augend[q]) == 0 and carry == 0:
                sum.append(0)
                carry = 0
            if int(l_augend[q]) == 1 and carry == 0:
                sum.append(1)
                carry = 0
            if int(l_augend[q]) == 0 and carry == 1:
                sum.append(1)
                carry = 0
            if int(l_augend[q]) == 1 and carry == 1:
                sum.append(0)
                carry = 1
        else:
            if int(l_augend[q]) == 0 and carry == 0:
                sum.append(1)
                carry = 0
            if int(l_augend[q]) == 0 and carry == 1:
                sum.append(0)
                carry = 1
            if int(l_augend[q])  == 1 and carry == 1:
                sum.append(1)
                carry = 1
            if int(l_augend[q]) == 1 and carry == 0:
                sum.append(0)
                carry = 1
        q = q + 1
    if carry == 1: #si à la fin de toutes les comparaisons il reste un carry de 1, on l'ajoute à la fin de la liste de sum
        sum.append(1)
    sum = sum[::-1]
    global result
    result = ''
    for x in range(0, len(sum), 1): # on inverse la liste pour obtenir le résultat final dans l'ordre correct
        result = result + str(sum[x])
    result = int(result) #on transforme le resultat en nombre decimal
    return result
print (multiplicand,'*',multiplier,'=',multiplication(multiplicandbin,multiplierbin))
