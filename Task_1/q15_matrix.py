# Q15 - Rotate an n*n matrix by 90° clockwise.Take a user input for a matrix and print the elements in spiral order
n = int(input("Enter the size n of the matrix: "))

matrix =[]
for i in range(n):
    row = input(f"Enter row {i+1} ({n} numbers separated by spaces:) ").split()
    row = [int(x) for x in row]
    matrix.append(row)
for i in range(0, n - 1):
    for j in range(i + 1, n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
for row in matrix:
    row.reverse()
    print(row)

top, bottom, left, right = 0, n-1, 0, n-1
result = []
while top <=bottom and left <= right:
    for col in range(left, right + 1):
        result.append(matrix[top][col])
    top += 1

    for row in range(top, bottom + 1):
        result.append(matrix[row][right])
    right -= 1

    if top <= bottom:
        for col in range(right, left - 1, -1):
            result.append(matrix[bottom][col])
        bottom -= 1

    if left <= right:
        for row in range(bottom, top - 1, - 1):
            result.append(matrix[row][left])
        left += 1

print(result)



