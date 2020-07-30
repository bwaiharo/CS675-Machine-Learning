# import math
# print("Enter the first point A")
# x1, y1 = map(int, input().split())
# print("Enter the second point B")
# x2, y2 = map(int, input().split())
# dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# print("The Euclidean Distance is " + str(dist))

import csv
import math

with open('vector.txt', 'r') as inf:
     data = list(csv.reader(inf, skipinitialspace=True))
     data = [i for i in data if i] ## add to deal w/ blank lines in data file
print(data)
for i in range(0,len(data)-1):
    print(data[i+1][::2])
    print(data[i+1][::-2])
    print("-----------------")
    print(data[i-1][::2])
    print(data[i-1][::-2])
    print("*****************")
# print(len(data[0]))

# for i in range(0,len(data),1):
#     print(data[i])

# ben = [[i ** j for j in range(3)] for i in range(3)]

# print(ben)

# for column in data:
#     for item in column:
#         print(item, end = " ")
#     print()