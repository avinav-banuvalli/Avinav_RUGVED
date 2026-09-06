# Q14-Given an array arr[], find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.
def repetition(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i] 

    return -1

print(repetition([10,5,3,4,3,5,6]))
print(repetition([1,2,3,4]))
print(repetition([5,5]))
print(repetition([]))
