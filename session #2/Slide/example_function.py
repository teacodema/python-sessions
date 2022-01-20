# fonction ne retournant pas de valeurs
def salutation(name):
    print("Bonsoir, ", name)

salutation("Afaf")

#################################################

# fonction retournant une valeur
def multiplication(a, b):

    return a * b

resultat = multiplication(4, 3)
print(resultat)

#################################################

def puissance(a, b = 1):
    return a ** b

print(puissance(3))
print(puissance(b = 3, a = 2))

