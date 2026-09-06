# Q10-Write a python function to check if a given credit card number is valid or not using Luhn's Algorithm


def is_valid(card_number):
    # removes spaces and dashes so that "4434 5423 5421 3412" works
    digits_str = card_number.replace(" ", "").replace("-", "")

    # a valid number should have only digits
    if not digits_str.isdigit():
        return False

    print("Digits_str = ",digits_str)
    digits = [int(d) for d in digits_str]
    print("Digits array",digits)

    
    # walk the digits from right to left
    total = 0
    for index, digit in enumerate(reversed(digits)):
        if index % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0

# take input from the user and print whether the nummber is valid  
number = input("Enter the credit card number:")
if is_valid(number):
    print("The card number is valid")
else:
    print("The card number is not valid")



