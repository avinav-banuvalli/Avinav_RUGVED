# Q8-Write a python program to divide a given string into equal parts containing n(user input) characters of same sequence

# This is a function to divide the string
def dividing_string(original_string):
# The try and except block is used to ensure only valid integers are entered
    try:
         n = int(input("Enter the value of n: "))
    except ValueError:
         return "Error: n must be a valid Integer"

     
    if n <= 0 :
         return "Error: n must be a positive Integer"
         
    if n > len(original_string):
         return "Error: n cannot be more than the length of the string"
        
    if len(original_string) % n != 0:
         return "Error:String cannot be divided into equal parts"
    
         
    chunks = []
    for i in range(0, len(original_string), n):
         chunks.append(original_string[i:i+n])
    if len(set(chunks)) == 1:
         return chunks
    else:
         return "Sequence not same"

# Taking input and printing the result 
str = input("Enter a string: ")
result = dividing_string(str)
print(result)
    


