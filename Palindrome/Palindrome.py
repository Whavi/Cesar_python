message = input("Veuillez donner un mot ou une phrase palindrome : ") 
strin = ""
sansEspace = message.replace(" ", "").lower() #Remplace les espaces par du vide
sansEspaceReverse = strin.join(reversed(sansEspace)) # inverse la chaine de caractère

if(sansEspace == sansEspaceReverse):  #condition if,else
    print("Le message est un palindrome")
else:
    print("Le message n'est un pas palindrome")
