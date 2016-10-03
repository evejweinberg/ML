from random import choice
from numpy import array, dot, random
from pylab import plot, ylim
import matplotlib.pyplot as plt

#activation function, or step function
unit_step = lambda x: 0 if x < 0 else 1

training_data = [ (array([0,0,1]), 0), (array([0,1,1]), 1), (array([1,0,1]), 1), (array([1,1,1]), 1), ]

w = random.rand(3)

errors = []
eta = 0.1  #learning rate
n = 100

for i in xrange(n):
    x, expected = choice(training_data)
    result = dot(w, x)
    error = expected - unit_step(result)
    errors.append(error)
    w += eta * error * x


for x, _ in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))


ylim([-1,1])
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.plot(errors)
plt.show()
