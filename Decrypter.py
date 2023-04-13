message = input("Veuillez donner votre message à décrypter :")
text = ''
for char in message:
    if not char.isalpha():
        continue
    char = char.upper() #mettre en maj le message
    lettre = ord(char) - 1 #décrementer de 1 les lettres
    if lettre < ord('Z'): #si le message depasse le A sa revien en Z
        lettre = ord('A')
    text += chr(lettre)
print(text) #Affichage du resultat
