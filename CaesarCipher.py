def encrypt(message,distance):
    encryptedMessage=""
    for letter in message:
        if(letter!=' '):
            if(letter>='a' and letter<='z'):
                encryptedLetter=chr((((ord(letter)-ord('a'))+distance)%26)+ord('a'))
                encryptedMessage+=encryptedLetter
            elif(letter>='A' and letter<='Z'):
                encryptedLetter=chr((((ord(letter)-ord('A'))+distance)%26)+ord('A'))
                encryptedMessage+=encryptedLetter
        else:
            encryptedMessage+=' '
    print(encryptedMessage)

def decrypt(message,distance):
    decryptedMessage=""
    for letter in message:
        if(letter!=' '):
            if(letter>='a' and letter<='z'):
                decryptedLetter=chr((((ord(letter)-ord('a'))-distance)%26)+ord('a'))
                decryptedMessage+=decryptedLetter
            elif(letter>='A' and letter<='Z'):
                decryptedLetter=chr((((ord(letter)-ord('A'))-distance)%26)+ord('A'))
                decryptedMessage+=decryptedLetter
        else:
            decryptedMessage+=' '
    print(decryptedMessage)

option=input("Choose your option : \n1.Encrypt Message \n2.Decrypt Message\n")
message=input("Enter the message :- ")
distance=int(input("Enter the distance :- "))
if(option=="1"):
    encrypt(message,distance)
elif(option=="2"):
    decrypt(message,distance)
else:
    print("Error")



