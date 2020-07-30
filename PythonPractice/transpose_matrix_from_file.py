#read from file
with open('matrix.txt', 'r') as f:
    l = [[int(num) for num in line.split(',')] for line in f]

#transpose matrix
result = map(list, zip(*l))
for r in result:
   print(r)