import string
import random
import sys
# using string for filling alphabets
test_list1= list(string.ascii_uppercase)
test_list2 = list(string.ascii_lowercase)
alphabet = test_list1 + test_list2
def encryption(plain_text, shift_key):
        cipher_text=" "
        for char in plain_text:
                if char in alphabet:
                        position = alphabet.index(char)
                        new_position=(position+shift_key)%26
                        cipher_text +=alphabet[new_position]
                else:
                     cipher_text += char
        print(f"Here's is the text after encryption: {cipher_text}")

def decryption(cipher_text, shift_key):
        plain_text=" "
        for char in cipher_text:
                if char in alphabet:
                        position = alphabet.index(char)
                        new_position=(position - shift_key)%26
                        plain_text +=alphabet[new_position]
                else:
                     plain_text += char
        print(f"Here's is the text after encryption: {plain_text}")


want_to_end = False
while not want_to_end:

        user_input = input("Type 'encrypt' for Encryption, thpe 'decrypt' for Decryption: ")
        text = input("Type your message:\n")
        shift = int(input("Enter shift key:\n"))

        if user_input == 'encrypt':
                encryption(plain_text = text, shift_key = shift)
        elif user_input == 'decrypt':
                decryption(text, shift)
        play_again = input("Type 'yes' to continue, type 'no' to exit: ")
        if play_again == 'no':
                want_to_end = True
                print("Have a Nicee day! See You Soon...")