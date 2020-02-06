matrix=[[1,2,3],[2,3,4],[5,6,7]]
matrix[0][2]
print(matrix[1][2])
matrix[0][1]=20
print(matrix)

for row in matrix:
    for item in row:
        print(item)