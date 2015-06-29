__author__ = 'Stefan Contiu'

# RESULTS LOG : June 29th, 2015
# Accuracy :  0.974074074074
# Confusion Matrix :
# [[341   2   0   0]
# [  0  13   0   0]
# [  0   0  84   1]
# [  0   0  11  88]]

###############################################
# load from csv training and testing sets
from numpy import genfromtxt
features_train = genfromtxt('d:/CODE/ml-crops/preproc/dataset/features_train.csv', delimiter=',')
classes_train = genfromtxt('d:/CODE/ml-crops/preproc/dataset/classes_train.csv', delimiter=',')
features_test = genfromtxt('d:/CODE/ml-crops/preproc/dataset/features_test.csv', delimiter=',')
classes_test = genfromtxt('d:/CODE/ml-crops/preproc/dataset/classes_test.csv', delimiter=',')

###############################################
# perform classification
from sklearn.naive_bayes import GaussianNB
from time import time
clf = GaussianNB()
fit_start_time = time()
clf.fit(features_train, classes_train)
GaussianNB()
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