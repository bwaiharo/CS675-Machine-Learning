import sys

l = [1,20,40,30,2,5,4]

query = sys.argv[-1]

# print(query)

print(*[query if (int(query) in l) else "Not in the castle Mario" ])

# if(int(query) in l):
#     print('Exist '+str(query))
# else:
#     print('Doesn\'t exist '+str(query))