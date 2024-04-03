augend = int(input("Tapez le premier nombre: ")) #augend est le premier nombre auquel on va additionner le addend
addend = int(input("Tapez un deuxième nombre: "))
addendbin = int(bin(addend)[2:]) #on transforme les deux nombres en binaire
augendbin = int(bin(augend)[2:])

def addition(augendbin, addendbin):
    l_augend = list(str(augendbin)) #on crée une liste, nommée l_augend pour les chiffres de augend
    l_addend = list(str(addendbin)) #on crée une liste, nommée l_addend pour les chiffres de addend
    l_augend = l_augend[::-1] #on inverse le sens des listes
    l_addend = l_addend[::-1] 
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
            if int(l_augend[q]) == 1 and carry == 1:
                sum.append(1)
                carry = 1
            if int(l_augend[q]) == 1 and carry == 0:
                sum.append(0)
                carry = 1
 
        q = q + 1
    if carry == 1: #si à la fin de toutes les comparaisons il reste un carry de 1, on l'ajoute à la fin de la liste de sum
        sum.append(1)
    return sum
 
def result(sum):
    sum = sum[::-1]
    result =''
    for x in range(0,len(sum),1): # on inverse la liste pour obtenir le résultat final dans l'ordre correct
        result = result + str(sum[x])
    result = int(result, 2) #on transforme le resultat en nombre decimal
    return result
 
print(augend, '+', addend, '=', result(addition(augendbin, addendbin)))