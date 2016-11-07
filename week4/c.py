#!/usr/bin/python

# Learning Machines
# Taught by Patrick Hebron at NYU ITP

import numpy as np


class multiLP(object):


	def __init__(self, data, sample_size, hidden_size, output_size):

		self.data = data
		self.sample_size = sample_size
		self.hidden_size = hidden_size
		self.output_size = output_size

	def sigmoid_fn(x):
		return 1.0 / ( 1.0 + np.exp( -x ) )

	def sigmoid_dfn(x):
		y = sigmoid_fn( x )
		return y * ( 1.0 - y )

	def tanh_fn(x):
		return np.sinh( x ) / np.cosh( x )

	def tanh_dfn(x):
		return 1.0 - np.power( tanh_fn( x ), 2.0 )

	activation_fn  = tanh_fn
	activation_dfn = tanh_dfn

	epoch = 0
	reportFreq = 1000

	learning_rate = 0.01

	sample_size = 1
	hidden_size = 15
	output_size = 1

	error       = np.zeros( ( sample_size, 1 ) )

	# Initialize weights and biases:

	layer0_weights = np.random.rand( hidden_size, sample_size )
	layer0_bias = np.random.rand( hidden_size, 1 )

	layer1_weights = np.random.rand( output_size, hidden_size )
	layer1_bias = np.random.rand( output_size, 1 )

	# Perform each epoch:
	while epoch <= 1e6:
		# Choose a random input:
		sample_vec = np.random.uniform( 0.0, np.pi * 2.0, ( sample_size, 1 ) )
		# Compute output:
		output_vec = np.sin( sample_vec )

		# Feed forward (input to hidden):
		layer1_activations = np.dot( layer0_weights, sample_vec ) + layer0_bias
		layer1_outputs = activation_fn( layer1_activations )

		# Feed forward (hidden to output):
		layer2_activations = np.dot( layer1_weights, layer1_outputs ) + layer1_bias
		layer2_outputs = activation_fn( layer2_activations )

		# Back propagate (output to hidden):
		layer2_deltas = activation_dfn( layer2_activations ) * ( layer2_outputs - output_vec )

		# Back propagate (hidden to input):
		layer1_deltas = activation_dfn( layer1_activations ) * np.dot( layer1_weights.T, layer2_deltas )

		# Apply deltas (layer 0):
		layer0_weights -= learning_rate * np.dot( layer1_deltas, sample_vec.T )
		layer0_bias -= learning_rate * layer1_deltas

		# Apply deltas (layer 1):
		layer1_weights -= learning_rate * np.dot( layer2_deltas, layer1_outputs.T )
		layer1_bias -= learning_rate * layer2_deltas

		# Compute error:
		error += np.absolute( output_vec - layer2_outputs )

		# Report error rate:
		if epoch % reportFreq == 0:
			print( "Epoch: %d\nError: %f" % ( epoch, np.sum( error ) / float( sample_size ) / float( reportFreq ) ) )
			error = np.zeros( ( sample_size, 1 ) )

		# Advance epoch iterator:
		epoch += 1
