# Q9-Write a python function to encrypt a string using Ceasar's Cipher

def encrypt(w, n):
    result = ""
    for i in w:
        if i.isalpha():
            if i.islower():
                # convert letter to 0-25 index
                position = ord(i) - ord('a')
                # if the number goes beyond 25 this shifts it back to 1
                shifted = (position + n) % 26
                new_char = chr(shifted + ord('a'))
                result += new_char
            elif i.isupper():
                # convert letter to 0-25 index
                position = ord(i) - ord('A')
                # if the number goes beyond 25 this shifts it back to 1
                shifted = (position + n) % 26
                new_char = chr(shifted + ord('A'))
                result += new_char
        else:
            result += i
    return result

# Taking input from the user and printing the encrypted string
word = input("Enter the word to be encrypted using ceasars cipher:")
num = int(input("Enter the value of n:"))
print(encrypt(word, num))
