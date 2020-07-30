# Program to multiply two matrices using nested loops

# 4x2 matrix
X = [[12,7,3,9],
    [4 ,5,6,8]]
# 3x4 matrix
Y = [[5,8,1],
    [6,7,3],
    [4,5,9],
    [8,1,5]]
# result is 2x3
result = [[0,0,0],
         [0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)