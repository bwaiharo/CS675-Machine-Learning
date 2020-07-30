import math, collections

l = [1,20,40,30,2,5,4]

def mean(num):
    return sum(num) / len(num)

def mode(num):
    data = (collections.Counter(num))
    data_list = dict(data)
    m = max(list(data_list.values()))
    mode_val = [n for n, freq in data_list.items() if freq == m]
    if len(mode_val) == len(num):
        return "No mode in the list"
    else:
        return "Mode : " + ', '.join(map(str, mode_val))
     

def median(num):
    s = sorted(num)
    m = len(s)/2
    if (m % 2 == 0) :
        first_m = num[int(m)//2]
        second_m = num[int(m)//2 - 1]
        return (first_m + second_m) /2
    else:
        return num[int(m-0.5)]

def sumofDifferencessqrd(num):
    return sum((xi - mean(num)) ** 2 for xi in num)

def variance(num):
    return  sumofDifferencessqrd(num) / len(num)

def standardDeviation(num):
    return math.sqrt(variance(num))



print(f"Mean: {mean(l)}")
print(f"Mode: {mode(l)}")
print(f"Median: {median(l)}")
print(f"Max: {float(max(l))}")
print(f"Min: {float(min(l))}")
print(f"Sum of Differences^2: {sumofDifferencessqrd(l)}")
print(f"Variance: {variance(l)}")
print(f"Standard Variation: {standardDeviation(l)}")
