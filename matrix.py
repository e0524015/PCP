matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print("Initial Matrix:")
for row in matrix:
    print(row)
matrix[0][1] = 5
matrix[2][2] = 9
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] += 5
print("\nMatrix After Updates and Adding 5:")
for row in matrix:
    print(row)