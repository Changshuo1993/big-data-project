import csv
import random
import math
import sys

print(' ')
print('            Bigdata final project')
print('################### Decision Tree ###################')


def loadcsv(filename):
    dataset = []
    night = 0
    busy = 0
    other =0
    total =0
    for line in open(filename):
        info = line.split(",")
        if info[2].strip() != '':
            time = info[1].split(":")
            hour = int(time[0])
            if (hour >=22) or (hour <4):
                day = int(0)
                night+=1
            elif (8< hour <=10) or (16<= hour <22):
                day = int(1)
                busy+=1
            else:
                day = int(2)
                other+=1
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
 #           if reason!=0:
 #               if day==0:
 #                   night+=1
  #              elif day==1:
   #                 busy+=1
    #            else:
     #               other+=1
      #          total+=1
            if sys.argv[1] == 'zip' and sys.argv[2] == 'day':
                dataset.append([zip,day])
    total=night+busy+other
    Ck1=night/(total*1.0)
    Ck2=busy/(total*1.0)
    Ck3=other/(total*1.0)

    ckpro = []
    ckpro.append(float(Ck1))
    ckpro.append(float(Ck2))
    ckpro.append(float(Ck3))
    # print dataset
    return [dataset,ckpro]


def splitdataset(dataset, splitRatio):
    trainsize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainsize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]


def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    #print separated
    return separated


def mean(numbers):
    return sum(numbers) / float(len(numbers))


def stdev(numbers):
    avg = mean(numbers)
    if len(numbers) == 1:
        variance = 1
    else:
        variance = math.sqrt(sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1))
    return variance


def summarize(dataset):
    #print dataset
    #print len(dataset)
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    #print summaries
    return summaries


def summarizeByClass(dataset):
    #print len(dataset)
    separated = separateByClass(dataset)
    summaries = {}
    #print len(separated)
    for classValue, instances in separated.iteritems():
        summaries[classValue] = summarize(instances)
        # print "I am here"
        #print classValue, instances
        #print('classvalue {0}:{1}').format(classValue,summaries[classValue])
    return summaries


def calculateProbability(x, mean, stdev):
    # x = float(x)
    # mean = float(mean)
    # stdev = float(stdev)
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent


def calculateClassProbabilities(summaries, inputVector,ckpro):
    probabilities = {}
    for classValue, classSummaries in summaries.iteritems():
        classValue=int(classValue)
        probabilities[classValue] = ckpro[classValue]
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
    return probabilities

#def calcckposibility(summaries, classValue):
    #ckposibility = len(summaries[classValue])/len(summaries)
    #print(ckposibility)
    #return ckposibility

def predict(summaries, inputVector, ckpro):
    probabilities = calculateClassProbabilities(summaries, inputVector, ckpro)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.iteritems():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel


def getPredictions(summaries, testSet, ckpro):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i], ckpro)
        predictions.append(result)
    return predictions

def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


def main():
    filename = 'NYPD_Motor_Vehicle_Collisions.csv'
    # filename = 'try.csv'
    splitRatio = 0.67
    dataset, ckpro = loadcsv(filename)
    #print(ckpro)
    trainingSet, testSet = splitdataset(dataset, splitRatio)
    print('Split {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainingSet), len(testSet))
    # prepare model
    summaries = summarizeByClass(trainingSet)
    #print('Summary by class value:\n {0}').format(summaries)
    # test model
    predictions = getPredictions(summaries, testSet, ckpro)
    accuracy = getAccuracy(testSet, predictions)
    print('--> Input_variable:{0}').format(sys.argv[1])
    print('--> Lable:{0}').format(sys.argv[2])
    print('-- Accuracy: {0}% --').format(accuracy)
    print('################### Decision Tree ###################')
    print(' ')



main()
