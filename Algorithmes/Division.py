dividende = int(input('Tapez un nombre: ')) #l'utilisateur doit entrer un dividende auquel on va diviser le diviseur
diviseur = int(input('Tapez un deuxieme nombre: '))

if diviseur == 0: #cette boucle affiche une erreur et demande à l'utilisateur d'entrer un nouveau diviseur si celui-ci était égal à 0
    print('ERREUR : DIVISION PAR 0')
    diviseur = int(input('Tapez un deuxieme nombre: '))

dividendebin = bin(dividende)[2:] #on transforme les nombres en binaire
diviseurbin = bin(diviseur)[2:]

def subtraction(minuendbin, subtrahendbin): #on prend la fonction de soutraction simplifiée
    minuend = int(minuendbin, 2)
    subtrahend = int(subtrahendbin, 2)
    return bin(minuend - subtrahend)[2:]

def division(dividendbin, diviseurbin): #on crée la fonction pour effectuer la division binaire
    quotient = '' #Le quotient commence vide
    tranche = dividendbin # La tranche est égale au dividende pour à la fin devenir le reste

    while int(tranche, 2) >= diviseur: #si la tranche est égale ou supérieur au diviseur
        l_quotient = '0'  # on réinitialise la liste de quotient à 0
        while int(tranche, 2) >= diviseur:
            l_quotient = bin(int(l_quotient, 2) + 1)[2:] #on augmente le quotient
            tranche = subtraction(tranche, diviseurbin) #on soustrait le diviseur de la tranche
        quotient += l_quotient # on ajoute le quotient à la la liste de quotient

    return int(quotient, 2), int(tranche, 2) #on convertit le quotient et la tranche en décimal

if dividende < diviseur: #si le dividende est inférieur au diviseur
    print(0, 'avec un reste de', dividende) #on affiche le résultat avec un quotient de 0 et un reste égal au dividende
else: #si le dividende est supérieur ou égal au diviseur
    quotient, tranche = division(dividendebin, diviseurbin) # on effectue la division
    print(dividende, '/', diviseur, '=', quotient, 'avec un reste de', tranche) # on affiche la division avec le résultat en tant que quotient et le reste
