"""
Écrivez un programme qui permet d’insérer un élément dans un tuple.

"""

a_tuple = ("element1", "element2")
print(a_tuple)
new_element = ("element3",)
a_tuple = a_tuple + new_element

print(a_tuple)



###############################

def insertIntoTuple(tup, index, value):
    toList = list(tup)
    toList.insert(index,value)
    toList= tuple(toList)
    return toList
tup = (1,2,3)
insertIntoTuple(tup, 1, "new")
print(tup)
