from sklearn import tree
# Author Jeevith. 
# This code is in response to the code challenge for the video - https://www.youtube.com/watch?v=T5pRlIbr6gg  of Siralogy (Youtube). Thank you Sirajology for introducing such concepts in a easy manner from a newbie! 

clf = tree.DecisionTreeClassifier()
#Importing modules
from sklearn import tree
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neural_network import MLPClassifier

## CHALLENGE - create 3 more classifiers...
#1
#2
#3

#[height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
#Feature set - Data: [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

#Label set - Gender
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']


#CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)
# Calling decision tree classifier and fitting
clf1 =tree.DecisionTreeClassifier()
clfDT =clf1.fit(X, Y) 

#Calling support vector machine and fitting
clf2 = svm.SVC(probability=True)
clfSVC =clf2.fit(X, Y)  

#Calling KNeighbors classifier and fitting 
clf3 = KNeighborsClassifier(n_neighbors=3)
clfKN =clf3.fit(X, Y)  

#Calling gaussian_process classifier and fitting 
clf4 = GaussianProcessClassifier()
clfGP = clf4.fit(X, Y)

##Calling MLPClassifier and fitting 
clf5 = MLPClassifier(learning_rate='constant', learning_rate_init=0.001,)
clfMLP = clf5.fit(X, Y)

test = [[180, 80, 42]]
#Storing results 
predictionDT = clfDT.predict (test) 
predictionSVC = clfSVC.predict (test) 
predictionKN = clfKN.predict (test) 
predictionGP = clfGP.predict (test) 
predictionMLP = clfMLP.predict (test) 

#Storing probabilities
probaDT = clfDT.predict_proba (test)
probaSVC = clfSVC.predict_proba (test) 
probaKN = clfKN.predict_proba (test) 
probaGP = clfGP.predict_proba (test) 
probaMLP = clfMLP.predict_proba (test)  


print "DT Classifier test data {} is predicted as {} with probability of {}".format(test, predictionDT, probaDT)

print "SV Classifier test data {} is predicted as {} with probability of {}".format(test, predictionSVC, probaSVC)

print "KN classifier test data {} is predicted as {} with probability of {}".format(test, predictionKN, probaKN)

print "GP classifier test data {} is predicted as {} with probability of {}".format(test, predictionGP, probaGP )

prediction = clf.predict([[190, 70, 43]])
print "MLPClassifier test data {} is predicted as {} with probability of {}".format(test, predictionDT, probaDT)

#CHALLENGE compare their reusults and print the best one!

print prediction