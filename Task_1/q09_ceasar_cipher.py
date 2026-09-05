def encrypt(w,n):
    result=""
    for i in w:
        if i.isalpha():
            if i.islower():
                position = ord(i) - ord('a')
                shifted = (position + n)%26
                new_char=chr(shifted + ord('a'))
                result += new_char
            elif i.isupper():
                position = ord(i) - ord('A')
                shifted = (position + n)%26
                new_char=chr(shifted + ord('A'))
                result += new_char
        else:
            result += i
    return result
print(encrypt("Hello World!",3))