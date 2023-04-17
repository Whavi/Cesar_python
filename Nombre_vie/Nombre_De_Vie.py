message = input("Quelle est votre date de naissance en format JJ-MM-AAAA : ")

while(len(message)!=8):  #boucle while lorsque la date est different de 8 chiffres
    message = input("Erreur de saisie, quelle est votre date de naissance en format JJ-MM-AAAA : ")

listInt = [int(i) for i in str(message)]#crée une list de nombre
total = sum(listInt) #somme total de la liste

while(total>10): #boucle while pour arriver à un chiffre
    listInt = [int(i) for i in str(total)]
    total = sum(listInt)
print(total) #print du chiffre

"""
Input : 19991229
Ouput : 6
"""

