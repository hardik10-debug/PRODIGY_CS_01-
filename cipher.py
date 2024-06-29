from flask import Flask, render_template, request

app = Flask(__name__)

# Your existing code goes here
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
        return cipher_text

def decryption(cipher_text, shift_key):
        plain_text=" "
        for char in cipher_text:
                if char in alphabet:
                        position = alphabet.index(char)
                        new_position=(position - shift_key)%26
                        plain_text +=alphabet[new_position]
                else:
                    plain_text += char
        return plain_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        text = request.form['text']
        shift = int(request.form['shift'])
        
        if user_input == 'encrypt':
            result = encryption(text, shift)
        elif user_input == 'decrypt':
            result = decryption(text, shift)
        
        return render_template('cipher.html', result=result)
    
    return render_template('cipher.html')

if __name__ == '__main__':
    app.run(debug=True)