import numpy as np

X = np.array( [ [ 1.0, 2.0, 3.0 ], [ 4.0, 5.0, 6.0 ] ] )
Y = X.T
Y
array([[ 1.,  4.],
       [ 2.,  5.],
       [ 3.,  6.]])


# matric addition


X = np.array( [ [  1.0,  2.0,  3.0 ], [  4.0,  5.0,  6.0 ] ] )
Y = np.array( [ [ 10.0, 20.0, 30.0 ], [ 40.0, 50.0, 60.0 ] ] )
Z = X + Y
Z
array([[ 11.,  22.,  33.],
       [ 44.,  55.,  66.]])

# Matrix Hadamard Product:

X = np.array( [ [  1.0,  2.0,  3.0 ], [  4.0,  5.0,  6.0 ] ] )
Y = np.array( [ [ 10.0, 20.0, 30.0 ], [ 40.0, 50.0, 60.0 ] ] )
Z = X * Y
Z
array([[  10.,   40.,   90.],
       [ 160.,  250.,  360.]])


# Matrix Multiplication:

X = np.array( [ [ 2, -4, 6 ], [ 5, 7, -3 ] ] )
Y = np.array( [ [ 8, -5 ], [ 9, 3 ], [ -1, 4 ] ] )
Z = np.dot( X, Y )
Z
array([[-26,   2],
       [106, -16]])
