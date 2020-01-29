answer = [[i*j for i in range(1, j+1)] for j in range(1,8)]

# print the matrix 
for j in answer:
    print(j)



# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for row in range(0,5)]

# print the matrix 
for row in matrix:
    print(row)