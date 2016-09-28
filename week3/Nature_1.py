class Perceptron:

    def __init__(self,num):
        self.n = num
    #step #1 - seed random weights
        weights = [{} for i in range(num)]
        print weights
    # weights = []
    # weights.len = num;
        for (item in weights):
            weights[item] = random(-1,1)

    def feedForward(input):
        #recieve its input array and return the output
        #step 1: all up all the (input*weight)to one sum
        sum = 0;
        for (item in weights):
            sum+=imputs[item]*weights[item]
        #step2 get the sign of the sum bc that is
        #our activation function in this example
        return cmp(sum,0)

    # print feedForward(input)

test = Perceptron(3)
test.feedForward()
print test;
