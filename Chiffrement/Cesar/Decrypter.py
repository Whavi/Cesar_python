text = input('Veuillez donner votre message à décrypter :')
message = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    lettre = ord(char) - 1
    if lettre < ord('A'):
        lettre = ord('Z')
    message += chr(lettre)
print(message)
