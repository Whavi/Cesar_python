message = input("Veuillez donner votre message à hacher :")
text = ''
for char in message:
    if not char.isalpha():
        continue
    char = char.upper() #mettre en maj le message
    lettre = ord(char) + 1 #incrementer de 1 les lettres
    if lettre > ord('Z'): #si le message depasse le Z sa revien en A
        lettre = ord('A')
    text += chr(lettre)
print(text) #Affichage du resultat
