import numpy as np


a = np.array( [ 0, 2, 4, 6, 8 ] )
# b = array([0, 2, 4, 6, 8])

print a
# print b

print np.zeros( 5 )
# array([ 0.,  0.,  0.,  0.,  0.])
#
print np.ones( 5 )
# array([ 1.,  1.,  1.,  1.,  1.])
#
print np.zeros( ( 5, 1 ) )
# array([[ 0.],
#        [ 0.],
#        [ 0.],
#        [ 0.],
#        [ 0.]])
#
print np.zeros( ( 1, 5 ) )
# array([[ 0.,  0.,  0.,  0.,  0.]])
#
print np.arange( 5 )
#array([0, 1, 2, 3, 4])
#

# start, end, and extent of interval
print np.arange( 0, 1, 0.1 )
# array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])
#
# from zero to 1 and 5 values in it (number of units)
np.linspace( 0, 1, 5 )
# array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
#
# start with random perceptions of the world
np.random.random( 5 )
