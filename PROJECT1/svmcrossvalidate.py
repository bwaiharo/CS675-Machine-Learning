from sklearn import svm
import random

def getbestC(train,labels):
                
        random.seed()
        allCs = [.001, .01, .1, 1, 10, 100]
        error = {}
        for j in range(0, len(allCs), 1):
                error[allCs[j]] = 0
        rowIDs = []
        for i in range(0, len(train), 1):
                rowIDs.append(i)
        nsplits = 5
        for x in range(0,nsplits,1):        
                #### Making a random train/validation split of ratio 90:10
                newtrain = []
                newlabels = []
                validation = []
                validationlabels = []

                random.shuffle(rowIDs) #randomly reorder the row numbers      
#                print(rowIDs)

                for i in range(0, int(.9*len(rowIDs)), 1):
                        newtrain.append(train[rowIDs[i]])
                        newlabels.append(labels[rowIDs[i]])
                for i in range(int(.9*len(rowIDs)), len(rowIDs), 1):
                        validation.append(train[rowIDs[i]])
                        validationlabels.append(labels[rowIDs[i]])

                #### Predict with SVM linear kernel for values of C={.001, .01, .1, 1, 10, 100} ###
                for j in range(0, len(allCs), 1):
                        C = allCs[j]
                        clf = svm.LinearSVC(C=C)
                        clf.fit(newtrain, newlabels)
                        prediction = clf.predict(validation)
                        
                        err = 0
                        for i in range(0, len(prediction), 1):
                                if(prediction[i] != validationlabels[i]):
                                        err = err + 1

                        err = err/len(validationlabels)
                        error[C]+=err
                        print("err=",err,"C=",C,"split=",x)


        bestC = 0
        minerror=100
        keys = list(error.keys())
        for i in range(0, len(keys), 1):
                key = keys[i]
                error[key] = error[key]/nsplits
                if(error[key] < minerror):
                        minerror = error[key]
                        bestC = key

        #print(bestC,minerror)
        return [bestC,minerror]

                                