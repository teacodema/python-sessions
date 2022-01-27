def factoriel(n):
    resultat = 1
    for x in range(1, n+1):
        resultat *= x
    return resultat

print(factoriel(5))