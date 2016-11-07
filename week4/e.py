#!/usr/bin/python

# Learning Machines
# Taught by Patrick Hebron at NYU ITP

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

# Activation function definitions:

def sigmoid_fn(x):
	return 1.0 / ( 1.0 + np.exp( -x ) )

def sigmoid_dfn(x):
	y = sigmoid_fn( x )
	return y * ( 1.0 - y )

def tanh_fn(x):
	return np.sinh( x ) / np.cosh( x )

def tanh_dfn(x):
	return 1.0 - np.power( tanh_fn( x ), 2.0 )

# MLP Layer Class:

class MlpLayer:
	def __init__(self,input_size,output_size):
		self.weights = np.random.rand( output_size, input_size ) * 2.0 - 1.0
		self.bias    = np.zeros( ( output_size, 1 ) )

# MLP Class:

class Mlp:
	def __init__(self,layer_sizes,activation_fn_name):
		# Create layers:
		self.layers = []
		for i in range( len( layer_sizes ) - 1 ):
			self.layers.append( MlpLayer( layer_sizes[ i ], layer_sizes[ i + 1 ] ) )
		# Set activation function:
		if activation_fn_name == "tanh":
			self.activation_fn  = tanh_fn
			self.activation_dfn = tanh_dfn
		else:
			self.activation_fn  = sigmoid_fn
			self.activation_dfn = sigmoid_dfn

	def predictSignal(self,input):
		# Setup signals:
		activations = [ input ]
		outputs     = [ input ]
		# Feed forward through layers:
		for i in range( 1, len( self.layers ) + 1 ):
			# Compute activations:
			curr_act = np.dot( self.layers[ i - 1 ].weights, outputs[ i - 1 ] ) + self.layers[ i - 1 ].bias
			# Append current signals:
			activations.append( curr_act )
			outputs.append( self.activation_fn( curr_act ) )
		# Return signals:
		return activations, outputs

	def predict(self,input):
		# Feed forward:
		#grab the two outputs from the predictSignal return#this is used after the trianing is done

		activations, outputs = self.predictSignal( input )
		# Return final layer output:
		#last item in outputs array
		# -1 means last item, or -2 is second to last
		return outputs[ -1 ]

	def trainEpoch(self,input,target,learn_rate):
		#input sgnal - thing user is trying to predict
		#train one wephoch then use a wrapper function to train them applicable
		#this function is just iteration
		#start with a fast learning rate then it gest slower.

		#numver of units we're dealing with, number of dims in putput data
		#number of examples
		num_outdims  = target.shape[ 0 ]
		num_examples = target.shape[ 1 ]
		# Feed forward:
		activations, outputs = self.predictSignal( input )
		# Setup deltas:
		deltas = []
		#number of layers
		#we're in back propogration so,
		#last layer is a special case, all the rest are the same
		# final layer from feed forward was the difference of correct vs predicted answers, all other layers were taking the weights and multiplying the deltas
		count  = len( self.layers )
		# Back propagate from final outputs:
		#do final layer first (then enter the loop in the 4 loop)
		#add to deltas array
		deltas.append( self.activation_dfn( activations[ count ] ) * ( outputs[ count ] - target ) )
		# Back propagate remaining layers:
		# do 4 loop in reverse the third parameter of -1 makes it decrement i
		for i in range( count - 1, 0, -1 ):
			deltas.append( self.activation_dfn( activations[ i ] ) * np.dot( self.layers[ i ].weights.T, deltas[ -1 ] ) )
			#if we needed to reverse this list , we could say "deltas.reverse()"
		# Compute batch multiplier:

		#learn in groups of 10 or so, instead of all at once, batch them
		batch_mult = learn_rate * ( 1.0 / float( num_examples ) )
		# Apply deltas:
		#iterating in the forwards direction, we have the array called count (deltas array)
		#we want to prepend, not append
		for i in range( count ):
			# the -1 flips the indexies , this lets us push backwards
			self.layers[ i ].weights -= batch_mult * np.dot( deltas[ count - i - 1 ], outputs[ i ].T )
			#expand_dims is a numpy function. representing a vector,
			#takes it from one form to another
			self.layers[ i ].bias    -= batch_mult * np.expand_dims( np.sum( deltas[ count - i - 1 ], axis=1 ), axis=1 )
		# Return error rate:
		#error rate tells us if have a good learning rate, so let's export that data
		#we could do this with euclidean distance (from predicted to target).
		#this is a bit fancier
		return ( np.sum( np.absolute( target - outputs[ -1 ] ) ) / num_examples / num_outdims )

#higher level function, still want input data, we're gonna do as many epohcs as we want, batching, how often we want to see the error rate
	def train(self,input,target,learn_rate,epochs,batch_size = 10,report_freq = 10):
		num_examples = target.shape[ 1 ]
		# Setup visualizer:
		vis = MlpVisualizer( np.amin( input ), np.amax( input ), np.amin( target ), np.amax( target ), report_freq )
		# Iterate over each training epoch:
		for epoch in range( epochs ):
			error = 0.0
			# Iterate over each training batch:
			for start in range( 0, num_examples, batch_size ):
				# Compute batch stop index:
				stop = min( start + batch_size, num_examples )
				# Perform training epoch on batch:
				#take all rows
				#colon means a range
				batch_error = self.trainEpoch( input[ :, start:stop ], target[ :, start:stop ], learn_rate )
				# Add scaled batch error to total error:
				#scale something back
				error += batch_error * ( float( stop - start ) / float( num_examples ) )
			# Report error, if applicable:

			if epoch % report_freq == 0:
				# Print report:
				print "Epoch: %d\nError: %f\n" % ( epoch, error )
				# Update visualizer:
				vis.update( epoch, error, input, target, self.predict( input ) )
		# Save final training visualization to image:
		vis.saveImage( 'mlp_training_process.png' )

# MLP Visualization Class:

class MlpVisualizer:
	def __init__(self,data_xmin,data_xmax,data_ymin,data_ymax,report_freq,buffer_size = 100):
		self.report_freq  = report_freq
		self.error_buffer = buffer_size
		# Setup plotter data:
		self.error_xdata = []
		self.error_ydata = []
		# Setup plotter:
		plt.ion()
		self.fig = plt.figure( 1 )
		self.fig.subplots_adjust( hspace = 0.3 )
		# Add subplots:
		self.datav_plot = self.fig.add_subplot( 2, 1, 1 )
		self.error_plot = self.fig.add_subplot( 2, 1, 2 )
		# Setup predictions subplot:
		self.datav_plot.set_title( 'Predictions' )
		self.datav_targ_line = Line2D( [], [], color='green', marker='+', linestyle='None' )
		self.datav_pred_line = Line2D( [], [], color='red', marker='x', linestyle='None' )
		self.datav_plot.add_line( self.datav_targ_line )
		self.datav_plot.add_line( self.datav_pred_line )
		self.datav_plot.set_xlim( data_xmin, data_xmax )
		self.datav_plot.set_ylim( data_ymin, data_ymax )
		# Setup error rate subplot:
		self.error_plot.set_xlabel( 'Epoch' )
		self.error_plot.set_ylabel( 'Error' )
	 	self.error_line = Line2D( [], [], color='black' )
		self.error_plot.add_line( self.error_line )
		self.error_plot.set_ylim( 0.0, 1.0 )
		# Show plot:
		plt.show()

	def saveImage(self,filepath):
		plt.savefig( filepath )

	def update(self,epoch,error,input,target,output):
		# Update error plotter data:
		if len( self.error_xdata ) == self.error_buffer:
			self.error_xdata.pop( 0 )
			self.error_ydata.pop( 0 )
		self.error_xdata.append( epoch )
		self.error_ydata.append( error )
		#
		title = 'Epoch: %d, Error: %f' % ( epoch, error )
		self.error_plot.set_title( title )
		# Compute error plotter x-range:
		mlen = self.report_freq * self.error_buffer
		xmin = np.amin( self.error_xdata )
		xmax = max( xmin + mlen, np.amax( self.error_xdata ) )
		# Update error plotter:
		self.error_line.set_data( self.error_xdata, self.error_ydata )
		self.error_plot.set_xlim( xmin, xmax )
		# Update predictions plotter:
		self.datav_targ_line.set_data( input, target )
		self.datav_pred_line.set_data( input, output )
		# Draw plot:
		plt.draw()
		plt.pause( 0.01 )

# Usage Example:

# Set hyperparameters:
sample_size = 1
output_size = 1
example_cnt = 300
batch_size  = 10
epoch_cnt   = 10000
report_freq = 10
learn_rate  = 0.05

# Construct MLP:
mlp = Mlp( [ sample_size, 15, output_size ], "tanh" )

# Construct dataset:
training_inputs  = np.random.uniform( 0.0, np.pi * 2.0, ( sample_size, example_cnt ) )
training_outputs = np.sin( training_inputs )

# Train MLP:
mlp.train( training_inputs, training_outputs, learn_rate, epoch_cnt, batch_size, report_freq )

# Make predictions:
training_guesses = mlp.predict( training_inputs )

# Print correct and predicted outputs:
print ( "Outputs: %s\nGuesses: %s\n" ) % ( training_outputs, training_guesses )



#linked list, each unit could be called a node
