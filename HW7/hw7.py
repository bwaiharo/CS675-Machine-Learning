<<<<<<< HEAD
<<<<<<< HEAD
import sys
import random
import math

def bestsplit(data, labels, col):
    colvals = {}
    indices = []
    rows = 0
    minus = 0
    for i in range(0,len(data),1):
        if(labels.get(i) != None):
            colvals[i]=data[i][col]
            indices.append(i)
            rows +=1
            if(labels[i] == 0):
                minus += 1
    
    sorted_indices = sorted(indices, key=colvals.__getitem__)

    lsize = 1
    rsize = rows - 1
    lp = 0
    rp = minus
    if(labels[sorted_indices[0]] == 0):
        lp += 1
        rp -= 1

    best_s = -1
    bestgini = 10000
    for i in range(1,len(sorted_indices), 1):
        s=(colvals[sorted_indices[i]] + colvals[sorted_indices[i-1]] )/2
        gini = (lsize/rows)*(lp/lsize)+(1 - lp/lsize)*(rsize/rows)*(rp/rsize)*(1 - rp/rsize)
        #print(lp,lsize,rp,rsize)
        if(gini < bestgini):
            bestgini = gini
            best_s = s
        if(labels[sorted_indices[i]] == 0):
            lp += 1
            rp -= 1
        lsize +=1
        rsize -=1

    return(best_s, bestgini)

#####################################
####################################
##################################

def dotproduct(u , v):
    assert len(u) == len(v), "dotproduct: u and v must be of same length"
    dp = 0
    for i in range(0,len(u), 1):
        dp += u[i] * v[i]
    return dp


datafile = sys.argv[1]
f = open(datafile)
data = []
i = 0
l = f.readline()

##############
#Read Data#
##############
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    # l2.append(1)
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

##############
#read labels#
##############

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = []
n.append(0)
n.append(0)

l = f.readline()
while(l != ''):
    a = l.split()
    # if(int(a[0]) == 0):
    #     trainlabels[int(a[1])] = -1
    # else:
    #     trainlabels[int(a[1])] = int(a[0])
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] +=1

##############################
####### Main ###############
########################
# print(cols)
# print(data)

boots = 100
test_predictions = {}
for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        test_predictions[i] = 0

for k in range(0, boots, 1):

    #make bootsraped dataset and lables
    i=0
    boot_data = []
    boot_trainlables={}
    while(i < len(data)):
        r = random.randint(0, rows-1)
        if(trainlabels.get(r) != None):
            boot_data.append(data[r])
            boot_trainlables[i] = trainlabels[r]
            i +=1
    best_split = -1
    best_col = -1
    best_gini = 100000
    for j in range(0,cols,1):
        [s,gini] = bestsplit(data, trainlabels, j)
        #print(s, gini)
        if(gini < best_gini):
            best_gini = gini
            best_split = s
            best_col = j

    m=0
    p=0
    for i in range(0,rows,1):
        if(trainlabels.get(i) != None):
            if(data[i][best_col] < best_split):
                if(trainlabels[i] == 0):
                    m += 1
                else:
                    p += 1

    if(m > p):
        left = -1
        right = 1
    else:
        left = 1
        right = -1
    #print(best_gini, best_split, best_col)

    for i in range(0, rows, 1):
        if(trainlabels.get(i) == None):
            if(data[i][best_col] < best_split):
                test_predictions[i] += left
            else:
                test_predictions[i] += right

for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        if(test_predictions[i] > 0):
            print("1 ", i)
        else:
            print("0 ", i)

=======
import sys
import random
import math

def bestsplit(data, labels, col):
    colvals = {}
    indices = []
    rows = 0
    minus = 0
    for i in range(0,len(data),1):
        if(labels.get(i) != None):
            colvals[i]=data[i][col]
            indices.append(i)
            rows +=1
            if(labels[i] == 0):
                minus += 1
    
    sorted_indices = sorted(indices, key=colvals.__getitem__)

    lsize = 1
    rsize = rows - 1
    lp = 0
    rp = minus
    if(labels[sorted_indices[0]] == 0):
        lp += 1
        rp -= 1

    best_s = -1
    bestgini = 10000
    for i in range(1,len(sorted_indices), 1):
        s=(colvals[sorted_indices[i]] + colvals[sorted_indices[i-1]] )/2
        gini = (lsize/rows)*(lp/lsize)+(1 - lp/lsize)*(rsize/rows)*(rp/rsize)*(1 - rp/rsize)
        #print(lp,lsize,rp,rsize)
        if(gini < bestgini):
            bestgini = gini
            best_s = s
        if(labels[sorted_indices[i]] == 0):
            lp += 1
            rp -= 1
        lsize +=1
        rsize -=1

    return(best_s, bestgini)

#####################################
####################################
##################################

def dotproduct(u , v):
    assert len(u) == len(v), "dotproduct: u and v must be of same length"
    dp = 0
    for i in range(0,len(u), 1):
        dp += u[i] * v[i]
    return dp


datafile = sys.argv[1]
f = open(datafile)
data = []
i = 0
l = f.readline()

##############
#Read Data#
##############
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    # l2.append(1)
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

##############
#read labels#
##############

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = []
n.append(0)
n.append(0)

l = f.readline()
while(l != ''):
    a = l.split()
    # if(int(a[0]) == 0):
    #     trainlabels[int(a[1])] = -1
    # else:
    #     trainlabels[int(a[1])] = int(a[0])
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] +=1

##############################
####### Main ###############
########################
# print(cols)
# print(data)

boots = 100
test_predictions = {}
for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        test_predictions[i] = 0

for k in range(0, boots, 1):

    #make bootsraped dataset and lables
    i=0
    boot_data = []
    boot_trainlables={}
    while(i < len(data)):
        r = random.randint(0, rows-1)
        if(trainlabels.get(r) != None):
            boot_data.append(data[r])
            boot_trainlables[i] = trainlabels[r]
            i +=1
    best_split = -1
    best_col = -1
    best_gini = 100000
    for j in range(0,cols,1):
        [s,gini] = bestsplit(data, trainlabels, j)
        #print(s, gini)
        if(gini < best_gini):
            best_gini = gini
            best_split = s
            best_col = j

    m=0
    p=0
    for i in range(0,rows,1):
        if(trainlabels.get(i) != None):
            if(data[i][best_col] < best_split):
                if(trainlabels[i] == 0):
                    m += 1
                else:
                    p += 1

    if(m > p):
        left = -1
        right = 1
    else:
        left = 1
        right = -1
    #print(best_gini, best_split, best_col)

    for i in range(0, rows, 1):
        if(trainlabels.get(i) == None):
            if(data[i][best_col] < best_split):
                test_predictions[i] += left
            else:
                test_predictions[i] += right

for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        if(test_predictions[i] > 0):
            print("1 ", i)
        else:
            print("0 ", i)

>>>>>>> b6c1b81e2708ba630321cb6808b030be24d6c16e
=======
import sys
import random
import math

def bestsplit(data, labels, col):
    colvals = {}
    indices = []
    rows = 0
    minus = 0
    for i in range(0,len(data),1):
        if(labels.get(i) != None):
            colvals[i]=data[i][col]
            indices.append(i)
            rows +=1
            if(labels[i] == 0):
                minus += 1
    
    sorted_indices = sorted(indices, key=colvals.__getitem__)

    lsize = 1
    rsize = rows - 1
    lp = 0
    rp = minus
    if(labels[sorted_indices[0]] == 0):
        lp += 1
        rp -= 1

    best_s = -1
    bestgini = 10000
    for i in range(1,len(sorted_indices), 1):
        s=(colvals[sorted_indices[i]] + colvals[sorted_indices[i-1]] )/2
        gini = (lsize/rows)*(lp/lsize)+(1 - lp/lsize)*(rsize/rows)*(rp/rsize)*(1 - rp/rsize)
        #print(lp,lsize,rp,rsize)
        if(gini < bestgini):
            bestgini = gini
            best_s = s
        if(labels[sorted_indices[i]] == 0):
            lp += 1
            rp -= 1
        lsize +=1
        rsize -=1

    return(best_s, bestgini)

#####################################
####################################
##################################

def dotproduct(u , v):
    assert len(u) == len(v), "dotproduct: u and v must be of same length"
    dp = 0
    for i in range(0,len(u), 1):
        dp += u[i] * v[i]
    return dp


datafile = sys.argv[1]
f = open(datafile)
data = []
i = 0
l = f.readline()

##############
#Read Data#
##############
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    # l2.append(1)
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

##############
#read labels#
##############

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = []
n.append(0)
n.append(0)

l = f.readline()
while(l != ''):
    a = l.split()
    # if(int(a[0]) == 0):
    #     trainlabels[int(a[1])] = -1
    # else:
    #     trainlabels[int(a[1])] = int(a[0])
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] +=1

##############################
####### Main ###############
########################
# print(cols)
# print(data)

boots = 100
test_predictions = {}
for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        test_predictions[i] = 0

for k in range(0, boots, 1):

    #make bootsraped dataset and lables
    i=0
    boot_data = []
    boot_trainlables={}
    while(i < len(data)):
        r = random.randint(0, rows-1)
        if(trainlabels.get(r) != None):
            boot_data.append(data[r])
            boot_trainlables[i] = trainlabels[r]
            i +=1
    best_split = -1
    best_col = -1
    best_gini = 100000
    for j in range(0,cols,1):
        [s,gini] = bestsplit(data, trainlabels, j)
        #print(s, gini)
        if(gini < best_gini):
            best_gini = gini
            best_split = s
            best_col = j

    m=0
    p=0
    for i in range(0,rows,1):
        if(trainlabels.get(i) != None):
            if(data[i][best_col] < best_split):
                if(trainlabels[i] == 0):
                    m += 1
                else:
                    p += 1

    if(m > p):
        left = -1
        right = 1
    else:
        left = 1
        right = -1
    #print(best_gini, best_split, best_col)

    for i in range(0, rows, 1):
        if(trainlabels.get(i) == None):
            if(data[i][best_col] < best_split):
                test_predictions[i] += left
            else:
                test_predictions[i] += right

for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        if(test_predictions[i] > 0):
            print("1 ", i)
        else:
            print("0 ", i)

>>>>>>> b6c1b81e2708ba630321cb6808b030be24d6c16e
