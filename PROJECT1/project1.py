import sys
import svmcrossvalidate
from sklearn import svm

from sklearn.feature_selection import f_regression
from array import array

from sklearn.model_selection import cross_val_score

datafile = sys.argv[1]
#datafile = "alldata"
f = open(datafile, 'r')
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

print("Read data")

######################
## Read training labels
##################
labelfile = sys.argv[2]
#labelfile = "trueclass"
f = open(labelfile)
trainlabels = []
trainlabels_d = {}
traindata = []
testdata = []
l = f.readline()
while():
    a = l.split()
    traindata.append(data[int(a[1])])
    trainlabels.append(int(a[0]))
    trainlabels_d[int(a[1])] = int(a[0])
    l=f.readline()

for i in range(0, rows, 1):
    if(trainlabels_d.get(i) == None):
        testdata.append(data[i])
print("read training labels")

### Rank the features in traindata with Pearson correlation (f_regression)

f_output = f_regression(traindata, trainlabels)
indices = []
for i in range(0,cols,1):
    indices.append(i)
fscores = f_output[0]
fscores_dict = {}
for i in range(0,len(f_output[0]), 1):
    fscores_dict[i] =fscores[i]

sorted_indices = sorted(indices, key=fscores_dict.__getitem__, reverse=True)

print("Ranked features")
for j in range(0, 1000, 1):
    k = sorted_indices[j]
    print(k)

### Pick the top 15 features and eliminate the rest from the data
traindata_topk = []
for i in range(0,len(traindata), 1):
    l=[]
    for j in range(0, 1000, 1):
        k= sorted_indices[j]
        l.append(traindata[i][k])
    traindata_topk.append(l)

testdata_topk = []
for i in range(0,len(testdata), 1):
    l=[]
    for j in range(0, 1000, 1):
        k= sorted_indices[j]
        l.append(testdata[i][k])
    testdata_topk.append(l)

traindata = traindata_topk
testdata = testdata_topk

f = open("traindata.topk", 'w')
for i in range(0, len(traindata), 1):
    for j in range(0, len(traindata[0]), 1):
        f.write(str(traindata[i][j]) + ' ')
        f.write('\n')
f.close()

f = open("testdata.topk", 'w')
for i in range(0, len(testdata), 1):
    for j in range(0, len(testdata[0]), 1):
        f.write(str(testdata[i][j]) + ' ')
        f.write('\n')
f.close()

#### Predict SVM linear kernel and C =.01 ###########
bestC = svmcrossvalidate.getbestC(traindata, trainlabels)
print("Best C and Error =", bestC)

'''
clf = svm.LinearSVC(c = bestC[0])

clf = svm.LinearSVC(C=.01)
scores = cross_val_score(clf, traindata, trainlabels, cv=10)
print(scores)

clf = svm.LinearSVC(C=.1)
scores = cross_val_score(clf, traindata, trainlabels, cv=10)
print(scores)
'''



