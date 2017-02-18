import cv2
import pickle
import numpy as np
import os, sys
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble.forest import RandomForestClassifier
from numpy.random import permutation

def getControls(pathToControl):
    import csv
    import numpy as np
    import os, sys
    
    #controlFile = open(pathToControl)
    
    #lines = controlFile.readlines()
    controls = list(csv.reader(open(pathToControl,'rt'), delimiter='\t'))
    return controls   


print("start")
controls = getControls("/media/niggins/Seagate Backup Plus Drive/data/14Apr2016_093054/control.txt")
print("got controls")
print(controls[0])
with open('histograms', 'rb') as f:
    hist = pickle.load(f)
print("got hists")
print(hist[0])
N = hist.shape[0]
I= permutation(N)
controls = np.array(controls)
Itr = I[:N//2]
Ite = I[N//2:]
Xtr = hist[Itr,:]
ttr = controls[Itr]

Xte = hist[Ite,:]
tte = controls[Ite]

print("split data", len(Xtr), len(Xte))
forest = RandomForestClassifier(n_estimators=2)
forest.fit(Xtr,ttr)
print("trained forest")


predictions = []
actual = []


for i in range(100):
    test = Xte[i]
    sum = 0
    for j in test:
        sum +=j
    print("sum", sum)
    test = np.reshape(test,(1,1764))
    pred = forest.predict(test)
    
    pred = np.reshape(pred, (9,))
    print(pred[1])
    act = tte[i]
    predictions.append(pred)
    actual.append(act)

predictions = np.array(predictions)
actual = np.array(actual)
plt.plot(predictions[:,1])
plt.plot(actual[:,1])
plt.show()

    
    