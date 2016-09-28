import numpy as np
import random
import matplotlib.pyplot as plt

input_value = np.array([[1,1],[-1,1],[1,-1], [-1,-1]])
output_value = [1,1,1,-1]
learningConst = .1
#this gives us an array of three
weights = 0.9 * np.random.random(2)+0.01
weight_bias = 0.9 * np.random.random(1)+0.01
# print weights
# StartingWeights = round(random.uniform(0.01, 1),10)
#where do I add the bias?


for i in range(100):
    for j in range(len(input_value)):
        actual_output = sum(input_value[j]*weights)
        expected_output = output_value[j]
        error = expected_output - actual_output
        # print error
        #create error delta
        delta_weight = error * input_value[j]
        weights = weights + delta_weight*learningConst
        print weights


print "WITH BIAS"


for i in range(100):
    for j in range(len(input_value)):
        actual_output = sum(input_value[j]*weights) + weight_bias
        expected_output = output_value[j]
        error = expected_output - actual_output
        # print error
        #create error delta
        delta_weight = error * input_value[j]
        weights = weights + delta_weight*learningConst
        #UPDATE THE WEIGHT_BIAS
        delta_weight_bias = error
        weight_bias = weight_bias + delta_weight_bias * learningConst
        print weights





#
#
# def andGate(count):
#     sum = 0
#
#
#
#     if (count == 0):
#         weights = []
#
#         for item in range(len(data)):
#             weight =  round(random.uniform(0.01, 1),10)
#             weights.append(weight)
#             val = data[item]*weight
#             sum += val
#             count = 1
#             # print sum
#     else:
#         print 'another time through'
#         for item in range(len(data)):
#             print newWeights
#             # weight =  round(random.uniform(0.01, 1),10)
#             # weights.append(weight)
#             val = data[item]*newWeights
#             sum += val
#
#
#
#     #run activation function
#     if (cmp(sum, 0) == 1):
#         print 'yes'
#
#     else:
#
#         print 'again'
#         count = 1
#         #error = outputexpected - outputGuessed
#         error = 1 - cmp(sum, 0)
#         weightChange = []
#         newWeights = []
#         for item in range(len(data)):
#             #Weight
#             weightDelta = error*data[item]
#             weightChange.append(weightDelta)
#             #WeightNew=
#             newWeights.append(weights[item]+weightDelta*.1)
#
#         # print weightChange
#         print newWeights
#         andGate(1)
#
#
#
#         # weights
#
#
#
#
#
# andGate(0)
#
#
#
#
#
#
#


#for the length of data, create random weights 0 through 1
#create inputs
