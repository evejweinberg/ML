import numpy as np
import random
import matplotlib.pyplot as plt
#or gate
input_value = np.array([[1,1],[-1,1],[1,-1], [-1,-1]])
output_value = [1,1,1,-1]
learningConst = .1
#this gives us an array of three
weights = 0.9 * np.random.random(2)+0.01
# print weights
weight_bias = 0.9 * np.random.random(1)+0.01
# print weights
# StartingWeights = round(random.uniform(0.01, 1),10)
#where do I add the bias?
errorsWithBias = []
errorsNoBias = []


for i in range(20):
    for j in range(len(input_value)):
        # print 'j is ' + str(input_value[j])
        actual_output = input_value[j][0]*weights[0] +input_value[j][1]*weights[1]+weight_bias
        #normalize the actual output
        # print actual_output
        expected_output = output_value[j]
        error = expected_output - actual_output
        # print error
        #create error delta
        delta_weight0 = error * input_value[j][0]
        delta_weight1 = error * input_value[j][1]
        # print delta_weight0
        weights[0] = weights[0] + delta_weight0*learningConst
        weights[1] = weights[1] + delta_weight1*learningConst
        # print 'new weights'
        print weights[0]
        # print weights[1]
        # print 'error'
        # print error
        # print weights
        errorsNoBias.append(error)


print "WITH BIAS"


# for i in range(100):
#     for j in range(len(input_value)):
#         actual_output = sum(input_value[j]*weights) + weight_bias
#         expected_output = output_value[j]
#         error = expected_output - actual_output
#
#         # print error
#         #create error delta
#         delta_weight = error * input_value[j]
#         weights = weights + delta_weight*learningConst
#         #UPDATE THE WEIGHT_BIAS
#         delta_weight_bias = error
#         weight_bias = weight_bias + delta_weight_bias * learningConst
#         print weights
#     errorsWithBias.append(error)

def plotThing(num,thing,label):
    # plt.subplot(num)
    plt.xlabel('Iteration')
    plt.ylabel(label)
    plt.plot(thing)
    plt.show()



# plotThing(211,errorsWithBias,'error with bias')
plotThing(212,errorsNoBias, 'error no bias')
