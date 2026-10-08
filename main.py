#CaesarCipher Encrypter and Decrypter

#This program will allow you to put any message in, and it with encrypt it in CaeserCipher.
#This program will also take any encrypted message in CaeserCipher, and decrypt it.
#This program will also show you all key possibilities from your encrypted message.

# Global variables
import string
numbers = ["12345678910"]
possibleCharacters = ( string.ascii_uppercase + string.ascii_lowercase + string.digits  + string.punctuation + " ")



# Run code

# Introduction 
print("\nHello, this program will encrypt or decrypt your message using the Caesar cipher. It can also show you all the encrypted message possibilties! \nLets Start!\n")
input("Press Enter to continue\n") 

while True:
    Decision = input(" \nWould you like to 'A.' Encrypt and Decrypt, 'B' Show all possible encrypted messages or 'C' I dont want to continue.\n").upper()


    # Encrypt or decrypt the message
    #Encrypt or Decrypt Variables
    initialPosition = 0
    shiftedPosition = 0
    shiftedMessage = ""

    if Decision == "A":
        initialMessage = input("What is your message?\n ")

        while True:
            key = input("What is the key? Choose one between 0 and 25 please. \n")

            if key.isdigit():
                key = int(key)
            if int(key) >= 0 and int(key) <= 26:
                break
            
            else:
                print("\nSorry, this input is invalid. Try again!\n")

        while True:
            mode = input("Do you want to encrypt or decrypt?\n ").lower()

            if mode != "encrypt" and mode != "decrypt":
                print("\nSorry, this input is invalid. Try again!\n")
            
            else:
                break

        for character in initialMessage:
            if character in possibleCharacters:
                initialPosition = possibleCharacters.find(character)
            
            
                if mode.lower() == "encrypt":
                    shiftedPosition = initialPosition + key
            
                elif mode.lower() == "decrypt":
                    shiftedPosition = initialPosition - key
            
                if shiftedPosition >= len(possibleCharacters):
                    shiftedPosition = shiftedPosition - len(possibleCharacters)
                elif shiftedPosition < 0:
                    shiftedPosition = shiftedPosition + len(possibleCharacters)
                
                shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]
            else:
                shiftedMessage = shiftedMessage + character
                


        # Print the shifted message
        print("Your " + mode.lower() + "ed message is: " + shiftedMessage)


    # Show possible key encrypted message
    # Possible Encrypt Key Variables
    elif Decision == "B":
    
        
            initialMessage = input("What is your encrypted message? ")
            input("\nPress enter to generate all of the key possibilities for your encrypted message.\n")

            # Look through all possible keys
            for key in range(len(possibleCharacters)):

                shiftedMessage = ""

                # Decrypt the message
                for character in initialMessage:
                    if character in possibleCharacters:
                        initialPosition = possibleCharacters.find(character)

                        shiftedPosition = initialPosition - key

                        if shiftedPosition < 0:
                            shiftedPosition = shiftedPosition + len(possibleCharacters)
                        
                        shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]
                    
                    else: 
                        shiftedMessage = shiftedMessage + character
                    
                # Print the shifted message
                print("Key #%s: %s" % (key, shiftedMessage))

            # Closing message
            print("\nNow scroll through all of the key possibilities above and find the readable plaintext message.\n")
            

    # Doesnt want to do it
    elif Decision == "C":
        print("\nThank you for your time!")
        break

    else:
        print("\nSorry, this input is invalid. Try again! \n")
