import sys
import random
import math

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
    l2.append(1)
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
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] +=1


##################
##Initialize w
##################
w = []
for i in range(0,cols,1):
    w.append(random.uniform(-0.01,0.01))

#########################################################
#########################################################
#########################################################
#########################################################

##################
#Gradient Descent#
##################

###Initializations

# eta = 0.001
#for breast cancer
#eta = 0.000000001
#for climate
#eta = 0.001
#for qsar
#eta = 0.000001
#for ionosphere
eta = 0.0001
#for hill valley
#eta = 0.001

dellf = []
for j in range(0, cols, 1 ):
    dellf.append(0)

prevobj = 100000000
obj = prevobj - 10

###########Main Iteration Loop############
# while(abs(prevobj - obj)> 0):
# while(prevobj - obj> 0.001):
# while(prevobj - obj> 0):
while(abs(prevobj - obj)> 0.001):
# while(abs(prevobj - obj)> 0.00001):
# while(abs(prevobj - obj)> 0.000000001):
# while(abs(prevobj - obj)> 0 and iter < 10000):
# while(iter < 1):
    prevobj = obj
    ################ Reset dellf to 0 #################
    for j in range(0,cols,1):
        dellf[j] = 0
    
    ###############Compute dellf ################
    for i in range(0,rows,1):
        if(trainlabels.get(i) != None):
            dp = dotproduct(w,data[i])
            for j in range(0,cols,1):
                dellf[j]+= (trainlabels.get(i) - dp)*data[i][j]

    ##########Update w ####################
    for j in range(0, cols, 1):
        w[j] += eta * dellf[j]
    
    error = 0

    ############ Compute error ###################
    for i in range(0,rows,1):
        if(trainlabels.get(i) != None):
            error += (trainlabels.get(i) - dotproduct(w,data[i]))**2
    obj = error
    print("Objective is ", error)


print(w)
wlen = math.sqrt(w[0]**2 + w[1]**2)
dist_to_origin = abs(w[2])/wlen
print("Distance to Origin", dist_to_origin)

wlen = 0
for i in range(0, len(w), 1):
    wlen += w[i]**2
wlen = math.sqrt(wlen)
print("wlen = ", wlen)                

#####################################
#####Classify Unlabbled Points########
####################################
for i in range(0,rows,1):
    if(trainlabels.get(i) == None):
    # if(trainlabels.get(i) != None):
    #if(1):
        dp = dotproduct(w,data[i])
        if(dp<0):
            print("0 ", i)
        else:
            print("1 ", i)