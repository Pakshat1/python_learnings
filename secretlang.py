# Note: This code implements a simple encoding and decoding scheme.
# The encoding adds random letters to the start and end of each word,   
# while the decoding removes these letters and reconstructs the original word.
# The encoding is reversible, allowing for easy decoding of the message.
# The program prompts the user to choose between encoding and decoding a message,
# and processes the input accordingly. It handles words of different lengths,
# ensuring that shorter words are reversed instead of encoded.
# The use of random letters adds a layer of complexity to the encoding, 
# making it less predictable while still allowing for straightforward decoding.
# The program is designed to be user-friendly, guiding the user through the encoding or decoding process    
# and providing clear output for the results.

# secretlang.py
import os    
import random

# Function to encode a word
def encode_word(word):
    if len(word) >= 3:
        first_letter = word[0]
        rest = word[1:] + first_letter
        start = ""
        end = ""
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(3):
            start += random.choice(letters)
            end += random.choice(letters)
        return start + rest + end
    else:
        return word[::-1]

# Function to decode a word
def decode_word(word):
    if len(word) < 3:
        return word[::-1]
    else:
        middle = word[3:-3]
        last_letter = middle[-1]
        rest = middle[:-1]
        return last_letter + rest

# Start of the program
print("Do you want to encode or decode?")
choice = input("Type 'encode' or 'decode': ").lower()

if choice == "encode":
    message = input("Enter your message to encode: ")
    words = message.split()
    encoded_result = ""
    for word in words:
        encoded_result += encode_word(word) + " "
    encoded_result = encoded_result.strip()
    print("Encoded message:", encoded_result)

    # Ask if user wants to decode it back
    ask = input("Do you want to decode this message too? (yes/no): ").lower()
    if ask == "yes":
        decoded_result = ""
        for word in encoded_result.split():
            decoded_result += decode_word(word) + " "
        print("Decoded message:", decoded_result.strip())

elif choice == "decode":
    message = input("Enter your message to decode: ")
    words = message.split()
    decoded_result = ""
    for word in words:
        decoded_result += decode_word(word) + " "
    decoded_result = decoded_result.strip()
    print("Decoded message:", decoded_result)

    # Ask if user wants to encode it again
    ask = input("Do you want to encode this message again? (yes/no): ").lower()
    if ask == "yes":
        encoded_result = ""
        for word in decoded_result.split():
            encoded_result += encode_word(word) + " "
        print("Encoded message:", encoded_result.strip())

else:
    print("Invalid choice. Please type only 'encode' or 'decode'.")

