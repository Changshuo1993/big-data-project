# -*- coding: utf-8 -*-
import csv
import random
import math
import numpy as np
import scipy as sp
from sklearn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
import sys

print(' ')
print('            Bigdata final project')
print('################### Decision Tree ###################')


def loadcsv(filename):
    dataset = []
    labels = []
    for line in open(filename):
        info = line.split(",")
        if info[2].strip() != '':
            time = info[1].split(":")
            hour = int(time[0])
            if (hour >22) or (hour <4):
                day = int(0)
            elif (8< hour <=10) or (16<= hour <22):
                day = int(1)
            else:
                day = int(2)
            if (info[3]!=''):
                zip = int(int(info[3])/10)
            else:
                zip = 1111
            if info[2] == 'QUEENS':
                area = float(0)
            elif info[2] == 'MANHATTAN':
                area = float(1)
            elif info[2] == 'BRONX':
                area = float(2)
            elif info[2] == 'STATEN ISLAND':
                area = float(3)
            elif info[2] == 'BROOKLYN':
                area = float(4)
            else:
                area = float(5)
            if (info[24] == 'LARGE COM VEH(6 OR MORE TIRES)')or(info[25] == 'LARGE COM VEH(6 OR MORE TIRES)'):
                type = float(0)
            elif (info[24] == 'PASSENGER VEHICLE')or(info[25] == 'PASSENGER VEHICLE'):
                type = float(1)
            elif (info[24] == 'SMALL COM VEH(4 TIRES)')or(info[25] == 'SMALL COM VEH(4 TIRES)'):
                type = float(2)
            elif (info[24] == 'SPORT UTILITY / STATION WAGON')or(info[25] == 'SPORT UTILITY / STATION WAGON'):
                type = float(3)
            elif (info[24] == 'BUS')or(info[25] == 'BUS'):
                type = float(4)
            elif (info[24] == 'VAN')or(info[25] == 'VAN'):
                type = float(5)
            elif (info[24] == 'TAXI')or(info[25] == 'TAXI'):
                type = float(6)
            elif (info[24] == 'OTHER')or(info[25] == 'OTHER'):
                type = float(7)
            elif (info[24] == 'UNKNOWN')or(info[25] == 'UNKNOWN'):
                type = float(8)
            elif (info[24] == 'LIVERY VEHICLE')or(info[25] == 'LIVERY VEHICLE'):
                type = float(9)
            elif (info[24] == 'AMBULANCE')or(info[25] == 'AMBULANCE'):
                type = float(10)
            elif (info[24] == 'FIRE TRUCK')or(info[25] == 'FIRE TRUCK'):
                type = float(11)
            elif (info[24] == 'PICK-UP TRUCK')or(info[25] == 'PICK-UP TRUCK'):
                type = float(12)
            else:
                type = float(13)
            if (info[18] == 'Unspecified')or(info[19] == 'Unspecified'):
                reason = float(0)
            elif (info[18] == 'Driver Inattention/Distraction')or(info[19] == 'Driver Inattention/Distraction'):
                reason = float(1)
            elif (info[18] == 'Prescription Medication')or(info[19] == 'Prescription Medication'):
                reason = float(2)
            elif (info[18] == 'Failure to Yield Right-of-Way')or(info[19] == 'Failure to Yield Right-of-Way'):
                reason = float(3)
            elif (info[18] == 'Physical Disability')or(info[19] == 'Physical Disability'):
                reason = float(4)
            elif (info[18] == 'Fatigued/Drowsy')or(info[19] == 'Fatigued/Drowsy'):
                reason = float(5)
            elif (info[18] == 'Lost Consciousness')or(info[19] == 'Lost Consciousness'):
                reason = float(6)
            elif (info[18] == 'Backing Unsafely')or(info[19] == 'Backing Unsafely'):
                reason = float(7)
            elif (info[18] == 'Outside Car Distraction')or(info[19] == 'Outside Car Distraction'):
                reason = float(8)
            elif (info[18] == 'Turning Improperly')or(info[19] == 'Turning Improperly'):
                reason = float(9)
            elif (info[18] == 'Oversized Vehicle')or(info[19] == 'Oversized Vehicle'):
                reason = float(10)
            elif (info[18] == 'Other Electronic Device')or(info[19] == 'Other Electronic Device'):
                reason = float(11)
            elif (info[18] == 'Failure to Yield Right-of-Way')or(info[19] == 'Failure to Yield Right-of-Way'):
                reason = float(12)
            elif (info[18] == 'Other Vehicular')or(info[19] == 'Other Vehicular'):
                reason = float(13)
            elif (info[18] == 'View Obstructed/Limited')or(info[19] == 'View Obstructed/Limited'):
                reason = float(14)
            elif (info[18] == 'Following Too Closely')or(info[19] == 'Following Too Closely'):
                reason = float(15)
            elif (info[18] == 'Unsafe Speed')or(info[19] == 'Unsafe Speed'):
                reason = float(16)
            elif (info[18] == 'Traffic Control Disregarded')or(info[19] == 'Traffic Control Disregarded'):
                reason = float(17)
            elif (info[18] == 'Driver Inexperience')or(info[19] == 'Driver Inexperience'):
                reason = float(18)
            elif (info[18] == 'Failure to Yield Right-of-Way')or(info[19] == 'Failure to Yield Right-of-Way'):
                reason = float(19)
            elif (info[18] == 'Illness')or(info[19] == 'Illness'):
                reason = float(20)
            else:
                reason = float(21)
            if sys.argv[1] == 'reason' and sys.argv[2] == 'area':
               if (reason!=float(0)) and (area!=int(5)) and (type!=float(8)):
                  dataset.append(reason)
                  labels.append(area)
            if sys.argv[1] == 'reason' and sys.argv[2] == 'day':
                if (reason!=float(0)) and (area!=int(5)) and (type!=float(8)):
                    dataset.append(reason)
                    labels.append(day)
            if sys.argv[1] == 'zip' and sys.argv[2] == 'day':
                if (reason!=float(0)) and (area!=int(5)) and (type!=float(8)):
                    dataset.append(zip)
                    labels.append(day)
            if sys.argv[1] == 'area' and sys.argv[2] == 'day':
                if (reason!=float(0)) and (area!=int(5)) and (type!=float(8)):
                    dataset.append(area)
                    labels.append(day)
            if sys.argv[1] == 'type' and sys.argv[2] == 'area':
                if (reason!=float(0)) and (area!=int(5)) and (type!=float(8)):
                    dataset.append(type)
                    labels.append(area)
            if sys.argv[1] == 'type' and sys.argv[2] == 'reason':
                if (reason!=float(0)) and (area!=int(5)) and (type!=float(8)):
                    dataset.append(type)
                    labels.append(reason)
            if sys.argv[1] == 'reason' and sys.argv[2] == 'type':
                if (reason!=float(0)) and (area!=int(5)) and (type!=float(8)):
                    dataset.append(reason)
                    labels.append(type)

    return dataset,labels

def main():
    filename = 'NYPD_Motor_Vehicle_Collisions.csv'
    dataset,labels = loadcsv(filename)
    x = np.array(dataset)
    y = np.array(labels)
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2)
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    print(clf)
    x_train=x_train.astype(float)
    x_train=np.resize(x_train,(len(x_train),1))
    print('--> Input_variable:{0}').format(sys.argv[1])
    print('--> Lable:{0}').format(sys.argv[2])
    print("train_input")
    print(x_train)
    print("train_classvalue")
    print(y_train)
    clf.fit(x_train, y_train)
    with open("tree.dot", 'w') as f:
        f= tree.export_graphviz(clf, out_file=f)
    answer = clf.predict(x_train)
    print("predic_classvalue")
    print(answer)
    print('Accuracy: {0}%').format(np.mean(answer == y_train)*100)
    #precision, recall, thresholds = precision_recall_curve(y_train, clf.predict(x_train))
    x=x.astype(float)
    x=np.resize(x,(len(x),1))
    answer = clf.predict_proba(x)
    print('################### Decision Tree ###################')
    print(' ')



main()
