# Q4-Write a python function to perform selection sort on a given string.

#Below method to sort numbers using selection sort
def selection_sort(num):
    n=len(num)

    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if num[j]<num[min_index]:
                min_index=j
        num[i],num[min_index]=num[min_index],num[i]
    return num

#Taking input from user and priting sorted numbers
numbers=input("Enter numbers separated by space: ").split()
print("Original numbers:",numbers)
sorted_numbers=selection_sort(numbers)
print("Sorted numbers:",sorted_numbers)