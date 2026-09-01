def hill_number(num):
    digits=[]
    while num!=0:
     rem=num%10
     digits.append(rem)
     num=num//10

    digits.reverse()

    if len(digits)<3:
       return False

    peak_value=max(digits)
    peak_index=digits.index(peak_value)

    if peak_index==0 or peak_index==len(digits) - 1:
        return False

    left=digits[0:peak_index+1]
    right=digits[peak_index:]

    return is_increasing(left) and is_decreasing(right)

def is_increasing(list1):
    for i in range(len(list1)-1):
       if list1[i]>=list1[i+1]:
          return False
    return True

def is_decreasing(list1):
    for i in range(len(list1)-1):
        if list1[i]<=list1[i+1]:
            return False
    return True

print(hill_number(12345431))
print(hill_number(12345))
print(hill_number(1231))
print(hill_number(54321))
print(hill_number(13241))
print(hill_number(12332))

    
    