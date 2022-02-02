"""
Écrivez un programme Python pour compter les éléments d'une 
liste jusqu'à ce qu'un élément soit un tuple.
"""

def findtuple(lists):
    count =0
    for x in lists:
        if type(x)==tuple:
            break
        count+=1
    return  count  

malist =['range',11,True,(23,"chine"),88]

print(findtuple(malist))