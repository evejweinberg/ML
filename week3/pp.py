import numpy as np
import random
import matplotlib.pyplot as plt

data = [1,1,-1,-1,1,1,-1]
#where do I add the bias?
count = 0

def andGate(count):
    sum = 0



    if (count == 0):
        weights = []

        for item in range(len(data)):
            weight =  round(random.uniform(0.01, 1),10)
            weights.append(weight)
            val = data[item]*weight
            sum += val
            count = 1
            # print sum
    else:
        print 'another time through'
        for item in range(len(data)):
            print newWeights
            # weight =  round(random.uniform(0.01, 1),10)
            # weights.append(weight)
            val = data[item]*newWeights
            sum += val



    #run activation function
    if (cmp(sum, 0) == 1):
        print 'yes'

    else:

        print 'again'
        count = 1
        #error = outputexpected - outputGuessed
        error = 1 - cmp(sum, 0)
        weightChange = []
        newWeights = []
        for item in range(len(data)):
            #Weight
            weightDelta = error*data[item]
            weightChange.append(weightDelta)
            #WeightNew=
            newWeights.append(weights[item]+weightDelta*.1)

        # print weightChange
        print newWeights
        andGate(1)



        # weights





andGate(0)









#for the length of data, create random weights 0 through 1
#create inputs
