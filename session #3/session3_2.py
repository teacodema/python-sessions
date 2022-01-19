def factoriel(n):
    global resultat
    resultat = 1
    for x in range(1, n+1):
        resultat *= x
    # return resultat

factoriel(5)
print(resultat)