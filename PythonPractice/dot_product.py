# X = [6,5,4]
# Y = [3,2,1]
X = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0], [10.0, 10.0], [10.0, 11.0], [11.0, 10.0], [11.0, 11.0]]
Y = [-0.01, -0.01]
def dotproduct(X,Y):
	dotproduct=0
	for i,j in zip(X,Y):
		dotproduct += i*j
	return dotproduct



for i in range(len(X)):
	print(dotproduct(X[i],Y))

# print(X[])
