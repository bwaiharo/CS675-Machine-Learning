import csv

with open('timelog.txt', 'r') as inf:
     data = list(csv.reader(inf, skipinitialspace=True))
     data = [i for i in data if i] ## add to deal w/ blank lines in data file

print(data)