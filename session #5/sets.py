"""
Écrivez un programme Python pour afficher les éléments d'un ensemble donné qui ne sont pas dans un autre ensemble.

"""

set1 = {11, 22, 33, 44}
set2 = {22, 44, 66, 88}
print(set1-set2)


#############################################

"""
Écrivez un programme Python pour trouver la valeur maximale et la valeur minimale dans un ensemble.

"""


def MAXIMUM(setss):
    return(max(setss))


def MINIMUM(setss):
    return(min(setss))


myset1 = set([14, 32, 13, 21, 51])
print(MINIMUM(myset1))
print(MAXIMUM(myset1))
