def declare_global():
    global nombre
    nombre=23

try:
    print("try bloc")
    print(nombre)
except Exception as e:
    print(e)
    print(type(e))
    print("except bloc")
    declare_global()
    
print(nombre+7)