
# exercice 3
# declarer la variable qui contiendra l'entree user
number = int(input("Entrez un entier : "))
# declarer le compteur
count = 0

for z in range(2, number):
    # verifier le modulo de la division du nombre(number) par le compteur z
    if(number % z == 0):
        # incrementer la variable count de 1
        count = count + 1
        # quitter la boucle
        break

if count > 0:
    print("Non premier")
else:
    print("premier")

