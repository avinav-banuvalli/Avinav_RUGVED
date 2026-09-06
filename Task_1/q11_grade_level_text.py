# Q11-Write a Python program that prints the grade level of a given text using Coleman-Liau formula.

# Function to count letters
def count_letters(text):
    count = 0
    for character in text:
        if character.isalpha():
            count+=1
    return count   

# Function to count words
def count_words(text):
    return len(text.split())

# Function to count sentences
def count_sentences(text):
    count = 0
    for character in text:
        if character in ".!?":
            count+=1
    return count

# The main function using coleman liau's formula 
def coleman_liau(text):
    letters = count_letters(text)
    words = count_words(text)
    sentence = count_sentences(text)
    L = (letters/words) * 100
    S = (sentence/words)  * 100
    index = ((0.0588 * L) - (0.296 * S) - 15.8)
    grade = round(index)
    if grade < 1:
        result = "Before Grade 1"
    elif grade >= 16:
        result = "Grade 16+"
    else:
        result = "Grade " + str(grade)
    return result

# Taking input from the user and printing the grade of the text
text = input("Enter some text:\n")
print("\nThe readability as a US school grade level is", coleman_liau(text), "\n")


    



