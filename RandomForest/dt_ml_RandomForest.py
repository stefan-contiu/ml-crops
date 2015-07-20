__author__ = 'Stefan Contiu'

# RESULTS LOG : July 20th, 2015
# Accuracy :  0.993837304848
# Confusion Matrix :
# [[3044   11    2    1]
# [   2   83    0    0]
# [   0    0  766   13]
# [   0    0    1  945]]
from time import time

###############################################
# load from csv training and testing sets
from numpy import genfromtxt
features_test = genfromtxt('d:/CODE/ml-crops/preproc/dataset/features_train.csv', delimiter=',')
classes_test = genfromtxt('d:/CODE/ml-crops/preproc/dataset/classes_train.csv', delimiter=',')

features_train = genfromtxt('d:/CODE/ml-crops/preproc/dataset/features_test.csv', delimiter=',')
classes_train = genfromtxt('d:/CODE/ml-crops/preproc/dataset/classes_test.csv', delimiter=',')

###############################################
# perform Random Forest classification
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
fit_start_time = time()
clf.fit(features_train, classes_train)
fit_end_time = time()
print "\nTraining time : ", round(fit_end_time - fit_start_time, 3), "s"

###############################################
# predict
predict_start_time = time()
classes_predicted = clf.predict(features_test)
predict_end_time = time()
print "Preciting time : ", round(predict_end_time - predict_start_time, 3), "s"

###############################################
# get accuracy
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
print "\nAccuracy : ", accuracy_score(classes_test, classes_predicted)
print "Confusion Matrix : \n", confusion_matrix(classes_test, classes_predicted)