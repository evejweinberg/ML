import numpy as np
import random
from IPython import embed
import sys

# data = sys.argv()

# IPython.start_ipython(argv=[])

# def sigmoid_fn(x): #domain 0-1, same basic s curve
# 	return 1.0 / ( 1.0 + np.exp( -x ) )

# def sigmoid_dfn(x): #derivative function
# 	y = sigmoid_fn( x )
# 	return y * ( 1.0 - y )

T = 1
F = -1

def tanh_fn(x): #domain -1 - 1
	return np.sinh( x ) / np.cosh( x )

def tanh_dfn(x): #derivative function
	return 1.0 - np.power( tanh_fn( x ), 2.0 )

def sign(x):
	if x > 0: # if summation is a positive number
		return 1
	elif x < 0: # if summation is a negative number
		return -1


class mlp(object):
	"""docstring for ClassName"""
	def __init__(self, data, sample_size, hidden_size, output_size): #this is where all the things go
		#super(ClassName, self).__init__()
		self.data = data
		self.sample_size = sample_size #argv
		self.hidden_size = hidden_size
		self.output_size = output_size

		#can also change to sigmoid
		self.activation_fn  = sign(data)
		self.activation_dfn = tanh_dfn

		self.epoch = 0
		self.max_epoch = 10
		self.reportFreq = 1000

		self.learning_rate = 0.01

		self.error = np.zeros( ( sample_size, 1 ) )

		# Initialize weights and biases:

		self.layer0_weights = np.random.rand( self.hidden_size, self.sample_size )
		self.layer0_bias = np.random.rand( self.hidden_size, 1 )

		self.layer1_weights = np.random.rand( self.output_size, self.hidden_size )
		self.layer1_bias = np.random.rand( self.output_size, 1 )



	def backpropogation(self):

		# # Choose a random input:
		# self.sample_vec = np.random.uniform( 0.0, np.pi * 2.0, (self.sample_size, 1 ) )
		self.sample_vec = random.choice(self.data)
		# embed()

		# Compute output:
		# self.output_vec = np.sin( self.sample_vec )
		self.output_vec = sign(self.data)

		# Feed forward (input to hidden):
		self.layer1_activations = np.dot( self.layer0_weights, self.sample_vec ) + self.layer0_bias

		self.layer1_outputs = self.activation_fn( self.layer1_activations )

		# Feed forward (hidden to output):
		self.layer2_activations = np.dot( self.layer1_weights, self.layer1_outputs ) + self.layer1_bias
		self.layer2_outputs = self.activation_fn( self.layer2_activations ) #predictions

		# Back propagate (output to hidden):
		self.layer2_deltas = self.activation_dfn( self.layer2_activations ) * ( self.layer2_outputs - self.output_vec )
		# embed()
		# Back propagate (hidden to input):
		# self.layer1_deltas = self.activation_dfn( self.layer1_activations ) * np.dot( self.layer1_weights.T, self.layer2_deltas )
		self.layer1_deltas = self.activation_dfn( self.layer1_activations ) * np.dot( self.layer1_weights.T, self.layer2_deltas )

		# Apply deltas (layer 0):
		# self.layer0_weights -= self.learning_rate * np.dot( self.layer1_deltas, self.sample_vec.T )
		self.layer0_weights -= self.learning_rate * np.dot( self.layer1_deltas, self.sample_vec )
		self.layer0_bias -= self.learning_rate * self.layer1_deltas

		# Apply deltas (layer 1):
		# self.layer1_weights -= self.learning_rate * np.dot( self.layer2_deltas, self.layer1_outputs.T )
		self.layer1_weights -= self.learning_rate * np.dot( self.layer2_deltas, self.layer1_outputs.T)
		self.layer1_bias -= self.learning_rate * self.layer2_deltas

		# Compute error:
		self.error += np.absolute( self.output_vec - self.layer2_outputs )

		# Report error rate:
		if self.epoch % self.reportFreq == 0:
			print( "Epoch: %d\nError: %f" % ( self.epoch, np.sum( self.error ) / float( self.sample_size ) / float( self.reportFreq ) ) )
			self.error = np.zeros( ( self.sample_size, 1 ) )

		# Advance epoch iterator:
		self.epoch += 1





my_mlp = mlp([[T,T],[T,F],[F,T],[F,F]], 4, 15, 4)


# Perform each epoch:
while my_mlp.epoch <= my_mlp.max_epoch: #equal to a million?
	my_mlp.backpropogation()
