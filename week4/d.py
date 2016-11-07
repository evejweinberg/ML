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
    #individual layer class
    #inializer function, pass inputs, inti weights, biases, initlaize biases to random or zero is ok
    def __init__(self,input_size,output_size):
        #these are now a range form -1 to 1 bc it's slightly better, thy're gonna move but lets start here
        self.weights = np.random.rand( output_size, input_size ) * 2.0 - 1.0
        self.bias    = np.zeros( ( output_size, 1 ) )

# MLP Class:

class Mlp:
#main class, constructor function:
#two inputs: an array with layer sizes
    def __init__(self,layer_sizes,activation_fn_name):
        # Create layers:
        self.layers = []
        for i in range( len( layer_sizes ) - 1 ):
            #outputs of first layer become inputs of the next, so we iterate in pairs
            #bc it's pairs, lets not go over the array, hence the minus 1
            self.layers.append( MlpLayer( layer_sizes[ i ], layer_sizes[ i + 1 ] ) )
            #this makes a layer object that we append into an array with all the layers


        # Set activation function:
        if activation_fn_name == "tanh":
            self.activation_fn  = tanh_fn
            self.activation_dfn = tanh_dfn
        else:
            self.activation_fn  = sigmoid_fn
            self.activation_dfn = sigmoid_dfn

#3 stages - feed forward, back propogation, appplication of deltas
#feedforward used two places - output of this process is a guess, then you take the sequence of activations and out puts
#use those to compute the error derivites, to back propogare them
# so we use the prediction process

#write this once and use it other places

    def predictSignal(self,input):
        # Setup signals:
        #two arrays
        #add users input, no if statement needed to know which layer we're on, no special cases
        activations = [ input ]
        #when we write the signal array we stick a previous value in there for the first time thorough
        outputs     = [ input ]
        # Feed forward through layers:
        for i in range( 1, len( self.layers ) + 1 ):
            print i
            # Compute activations:
            curr_act = np.dot( self.layers[ i - 1 ].weights, outputs[ i - 1 ] ) + self.layers[ i - 1 ].bias
            # Append current signals:
            #pass through activation function
            activations.append( curr_act )
            outputs.append( self.activation_fn( curr_act ) )
        # Return signals, two arrays:
        return activations, outputs

    def predict(self,input):
        # Feed forward:
        #start with the first layer, bc we need a previous layer to compute from
        activations, outputs = self.predictSignal( input )
        # Return final layer output:
        return outputs[ -1 ]

    def trainEpoch(self,input,target,learn_rate):
        num_outdims  = target.shape[ 0 ]
        num_examples = target.shape[ 1 ]
        # Feed forward:
        activations, outputs = self.predictSignal( input )
        # Setup deltas:
        deltas = []
        count  = len( self.layers )
        # Back propagate from final outputs:
        deltas.append( self.activation_dfn( activations[ count ] ) * ( outputs[ count ] - target ) )
        # Back propagate remaining layers:
        for i in range( count - 1, 0, -1 ):
            deltas.append( self.activation_dfn( activations[ i ] ) * np.dot( self.layers[ i ].weights.T, deltas[ -1 ] ) )
        # Compute batch multiplier:
        batch_mult = learn_rate * ( 1.0 / float( num_examples ) )
        # Apply deltas:
        for i in range( count ):
            self.layers[ i ].weights -= batch_mult * np.dot( deltas[ count - i - 1 ], outputs[ i ].T )
            self.layers[ i ].bias    -= batch_mult * np.expand_dims( np.sum( deltas[ count - i - 1 ], axis=1 ), axis=1 )
        # Return error rate:
        return ( np.sum( np.absolute( target - outputs[ -1 ] ) ) / num_examples / num_outdims )

    def train(self,input,target,learn_rate,epochs,batch_size = 10,report_freq = 10):
        num_examples = target.shape[ 1 ]
        # Iterate over each training epoch:
        for epoch in range( epochs ):
            error = 0.0
            # Iterate over each training batch:
            for start in range( 0, num_examples, batch_size ):
                # Compute batch stop index:
                stop = min( start + batch_size, num_examples )
                # Perform training epoch on batch:
                batch_error = self.trainEpoch( input[ :, start:stop ], target[ :, start:stop ], learn_rate )
                # Add scaled batch error to total error:
                error += batch_error * ( float( stop - start ) / float( num_examples ) )
            # Report error, if applicable:
            if epoch % report_freq == 0:
                # Print report:
                print "Epoch: %d\nError: %f\n" % ( epoch, error )


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
