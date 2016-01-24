#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###

from sklearn.metrics import accuracy_score
from sklearn import svm

clf = svm.SVC(C=10000.0, kernel='rbf')

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
prediction = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(prediction, labels_test)

print "accuracy: {}".format(accuracy)

print "answer for {} was: {}".format(10, prediction[10])
print "answer for {} was: {}".format(26, prediction[26])
print "answer for {} was: {}".format(50, prediction[50])

mailsFromChris = [pred for pred in prediction if pred == 1]

print "{} emails from Chris".format(len(mailsFromChris))

#########################################################
