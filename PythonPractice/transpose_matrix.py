A = [[5,8,1],
    [6,7,3],
    [4,5,9],
    [8,1,5]]


#using zip()

#Original Matrix

result = map(list, zip(*A))
for r in result:
   print(r)