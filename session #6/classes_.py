class Personne:
    count_=0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Personne.count_+=1
        
    def __str__(self):
        return "Hello " + self.name + ". You're " + str(self.age) +" years old."

personne1 = Personne('Hamzaoui', 30)
print(personne1)
print("1er appel")
print(personne1.count_)
personne2 = Personne('Tibari', 23)
print(personne2)
print("2eme appel")
print(personne1.count_)

print("Depuis la classe")
print(Personne.count_)

#############################################################

class Etudiant(Personne):
    def __init__(self, name, age, note):
        super().__init__(name, age)
        self.note=note        
        
    def __str__(self):
        
        return super().__str__() + '\nYour grade is : ' + str(self.note)


etd = Etudiant("Saad", 29, 9)
print(etd)
etd2 = Etudiant("Nouhaila", 26, 7)
print(etd2)




















