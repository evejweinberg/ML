import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1.0 / ( 1.0 + np.exp( -x ) )

def dsigmoid(x):
    y = sigmoid( x )
    return y * ( 1.0 - y )

def tanh(x):
    return np.sinh( x ) / np.cosh( x )

def dtanh(x):
    return 1.0 - np.square( tanh( x ) )

#specif the range and the increments
#start stop increments
xData = np.arange( -10.0, 10.0, 0.1 )
ySigm = sigmoid( xData )
ySigd = dsigmoid( xData )
yTanh = tanh( xData )
yTand = dtanh( xData )

plt.axis( [ -10.0, 10.0, -1.1, 1.1 ] )
plt.plot( xData, ySigm, 'r', xData, ySigd, 'r--' )
plt.plot( xData, yTanh, 'g', xData, yTand, 'g--' )
plt.show()
