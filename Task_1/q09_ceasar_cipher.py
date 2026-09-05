# Q9-Write a python function to encrypt a string using Ceasar's Cipher

def encrypt(w, n):
    result = ""
    for i in w:
        if i.isalpha():
            if i.islower():
                position = ord(i) - ord('a')
                shifted = (position + n) % 26
                new_char = chr(shifted + ord('a'))
                result += new_char
            elif i.isupper():
                position = ord(i) - ord('A')
                shifted = (position + n) % 26
                new_char = chr(shifted + ord('A'))
                result += new_char
        else:
            result += i
    return result


word = input("Enter the word to be encrypted using ceasars cipher:")
num = int(input("Enter the value of n:"))
print(encrypt(word, num))
