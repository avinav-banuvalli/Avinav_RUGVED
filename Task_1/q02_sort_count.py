# Q2: Write a python program to sort a string alphabetically and print the count of each character.

# Below method accepts a string and returns the sorted version of the string and a dictionary with char and count of char in the sorted string
def sort_count(s):
    sorted_string = "".join(sorted(s.lower()))

    char_count = {}
    for char in s.lower():
        char_count[char] = char_count.get(char, 0) + 1

    return sorted_string, char_count

# Taking the input string from the user
input_string = input("Enter a string: ")
sorted_string, char_count = sort_count(input_string)

print("Sorted String: ", sorted_string)
print("Count of characters in the Sorted String:")
for char in char_count:
    if char_count[char] > 1:
        print(f"{char} appears {char_count[char]} times")
    else:
        print(f"{char} appears {char_count[char]} time")
