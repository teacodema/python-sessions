# ex1 function 
def sequence (x):
    result =0
    if x==0 :
        result +=1
    elif x==1:
        result +=2
    elif x>=1:
        result +=(2*sequence(x-1)+(sequence(x-2))**2)

    return result    

# n=int(input("give a positive number: "))
# print(sequence(n))


# ex2 classes

class livre:
    def __init__(self,titre,nbpage,auteur):
       
        self.titre =titre
        self.nbpage = nbpage
        self.auteur =auteur
    def __str__(self):
        return "livre intitule "+self.titre+" contenant "+str(self.nbpage)+" pages de l'auteur "+self.auteur

# l1= livre('Espagnol d Amérique latine',250,'Berlitz')
# print (l1)

class Roman (livre):
    count=0
    def __init__(self,titre,nbpage,auteur,category):
        super().__init__(titre,nbpage,auteur)
        self.category = category
        Roman.count+=1
    def __str__(self):
        return "le Roman "+self.titre+" de l'auteur "+self.auteur+" contenant "+str(self.nbpage)+" pages classe dans la gategorie "+self.category
r1 = Roman('Chambre noire',200,'james Chase','drame' )
# print (r1)
# print(r1.count)


# ex3 Menu de commande 
print("-------------------------menu--------------------------")
print("pour excution de sequence enter 1 \npour excution de Romat enter 2 \npour execution de nombre de Roman enter 3 \npour exit enter 0  ")
m=int(input("enter le nomre choisie : "))
while m != 0 :

    if m ==1 :
        n=int(input("give a positive number between 0 and 10 : "))
        while (n<0 or n>10):
            n=int(input("give a positive number between 0 and 10 : "))
        print("le resultat de sequence est : "+str(sequence(n)))
    elif m==2:
        
        t=str(input("donner le nom du Roman : "))
        nb= int(input("donner le nombre de pages : "))
        auth= str(input("donner le nom de l'auteur : "))
        cat = str(input("donner la category du roman : "))
        r=Roman(t,nb,auth,cat)
        print (r)
    elif m==3:
        print("le nombre de roman est : "+str(Roman.count) )

    print("-------------------------menu--------------------------")
    print("pour excution de sequence enter 1 \npour excution de Romat enter 2 \npour execution de nombre de Roman enter 3 \npour exit enter 0  ")    
    m=int(input("enter le nomre choisie : "))
        
exit()      