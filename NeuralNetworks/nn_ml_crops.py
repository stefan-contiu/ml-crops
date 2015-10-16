__author__ = 'Stefan Contiu'

# RESULTS LOG : October 16th, 2015
# Accuracy :  TODO
# Confusion Matrix : TODO

from time import time

###############################################
# load from csv training and testing sets
from numpy import genfromtxt
features_test = genfromtxt('d:/CODE/ml-crops/preproc/dataset/features_train.csv', delimiter=',')
classes_test = genfromtxt('d:/CODE/ml-crops/preproc/dataset/classes_train.csv', delimiter=',')

features_train = genfromtxt('d:/CODE/ml-crops/preproc/dataset/features_test.csv', delimiter=',')
classes_train = genfromtxt('d:/CODE/ml-crops/preproc/dataset/classes_test.csv', delimiter=',')

# 0 index the classes
classes_test = classes_test - 1
classes_train = classes_train - 1

#import matplotlib.pyplot as pl
#pl.scatter(features_train[:,7], features_train[:,1], c=classes_train) #features_train[:8])
#pl.show()

###############################################
# import pybrain stuff
from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
from numpy import ravel

# Build classification data set
train_data = ClassificationDataSet(9, 1, nb_classes=4)
for i in range(len(features_train)):
    train_data.addSample(ravel(features_train[i]), classes_train[i])
train_data._convertToOneOfMany( )

test_data = ClassificationDataSet(9, 1, nb_classes=4)
for i in range(len(features_test)):
    test_data.addSample(ravel(features_test[i]), classes_test[i])
test_data._convertToOneOfMany( )

# build and train the network
print("Input dimension : " + str(train_data.indim) + ". Out dimenssion : " + str(train_data.outdim))
fnn = buildNetwork( train_data.indim, 25, train_data.outdim, outclass=SoftmaxLayer )
trainer = BackpropTrainer( fnn, dataset=train_data, momentum=0.05, learningrate=0.01, verbose=True, weightdecay=0.1)

trnerr,valerr = trainer.trainUntilConvergence(dataset=train_data,maxEpochs=150)
import matplotlib.pyplot as pl
pl.plot(trnerr,'b',valerr,'r')
pl.show()

out = fnn.activateOnDataset(test_data).argmax(axis=1)
print(percentError(out, test_data['class']))
from sklearn.metrics             import precision_score,recall_score,confusion_matrix
print(confusion_matrix(out, test_data['class']))

#trainer.trainEpochs(150)
    #trnresult = percentError(trainer.testOnClassData(), train_data['class'])

#print 'Error percent on test set : ', percentError(trainer.testOnClassData(dataset=test_data), test_data['class'])

    #print("epoch: %4d" % trainer.totalepochs,
        #"  train error: %5.2f%%" % trnresult,
        #"  test error: %5.2f%%" % tstresult)


#predicted_data=trainer.testOnClassData(dataset=test_data)
#NetworkWriter.writeToFile(fnn, 'oliv.xml')
#from sklearn.metrics             import precision_score,recall_score,confusion_matrix
#print("The precision is "+str(precision_score(classes_test,predicted_data)))
#print(confusion_matrix(classes_test,predicted_data))
#print(len(classes_test))
#print(len(predicted_data))