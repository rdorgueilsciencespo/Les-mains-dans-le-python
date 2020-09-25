#Notes moyennes

#Bibliothèques

#Initialisations
nbNotes = int(input("Bonjour ! Nous allons calculer votre moyenne générale. Combien avez vous eu de notes ? "))
i=1
j=1
note=10
notes=[]
coefs=[]

erreurNote = False

#Boucle pour récupérer les notes, et les stocker dans un fichier "notes", gestion des erreurs
while i < nbNotes+1 and erreurNote is False :
    
    note = int(input("Entrez votre note " + str(i) +"\n"))
    coef = int(input("Entrez son coefficient \n"))
    
    #Erreurs d'inputs
    if not 0<=note<=20 :
        erreurNote = True
        while erreurNote is True : 
            note = int(input("Votre note doit être comprise entre 0 et 20. Rééssayez : "))
            if 0<=note<=20 :
                erreurNote = False
                
    if isinstance(note, int)==False :
        erreurNote = True
        while erreurNote is True : 
            note = int(input("Votre note doit entrée en chiffres. Rééssayez : "))
            if 0<=note<=20 :
                erreurNote = False
         
    #Append list
    notes.append(note)
    coefs.append(coef)
    
    #incrémentation
    i = i + 1
   
#Calcul de la moyenne pondérée
    
#Somme des coefs   
sumCoefs= sum(coefs)
#Multiplication des termes deux à deux dans une liste
MoyennePondere0 = [a * b for (a,b) in zip(notes,coefs)]
#Somme de cette liste
MoyennePondere= sum(MoyennePondere0)
# Division par la somme des coefs et résultat final
print("Votre moyenne générale pondérée est de ", (MoyennePondere/sumCoefs))






