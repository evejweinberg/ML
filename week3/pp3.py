from random import choice
from numpy import array, dot, random
from pylab import plot, ylim
import matplotlib.pyplot as plt

#activation function, or step function
# unit_step = lambda x: 0 if x < 0 else 1
unit_step = lambda x: -1 if x < 0 else 1

# training_data = [
# (array([0,0,1]), 0),
# (array([0,1,1]), 1),
# (array([1,0,1]), 1),
# (array([1,1,1]), 1),
# ]

training_data = [
(array([-1,-1,1]), -1),
(array([-1,1,1]), 1),
(array([1,-1,1]), 1),
(array([1,1,1]), 1),
]

#create 3 random weights, 2 plus the bias weight
w = random.rand(3)
errors = []
eta = 0.1  #learning rate
n = 200 # of iterations

for i in xrange(n):
    #choice comes from random module, it picks randomly selected items
    #choose a random item form the learning
    #unpack the tupple as x and expected
    x, expected = choice(training_data)
    #take the dot product of the three weights, and the 3 x values
    # this gives us one scalar and iterates through the two arrays
    result = dot(w, x)
    #send the result to the activation function
    #take reult and send it through unit_step
    #then get the difference from expected to result of that
    error = expected - unit_step(result)
    #append to an array
    errors.append(error)
    w += eta * error * x


for x, _ in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))

# print ----*10
ylim([-1,1])
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.plot(errors)
plt.show()
