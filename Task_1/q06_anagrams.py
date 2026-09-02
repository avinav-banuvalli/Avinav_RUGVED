# Q6-Create a function that takes two strings as input and checks whether they are anagrams of each other.

# Method to check if strings are anagram or not
def anagrams(str1,str2):
    str1 = str1.replace(" ","")
    s1 = str1.lower()
    str2 = str2.replace(" ","")
    s2 = str2.lower()

    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    if s1 == s2:
        return True
    else:
        return False

# Taking input from the user
word1 = input("Enter the first string: ")
word2 = input("Enter the second string: ")

if (anagrams(word1,word2)):
   print("It is an Anagram")
else:
    print("It is not an Anagram")

    
