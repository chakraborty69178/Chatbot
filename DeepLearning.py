# contains the logic of the Deep Neural Network
import tensorflow as tf
import numpy as np
# creating the Tensorflow Place Holders

def model_input():
    inputs = tf.compat.v1.placeholder(tf.int32,[None,None] ,name ='input')
    targets = tf.compat.v1.placeholder(tf.int32,[None,None] ,name ='target')
    lr = tf.compat.v1.placeholder(tf.flot32 ,name ='Learning Rate')
    keep_prob = tf.compat.v1.placeholder(tf.flot32 ,name ='keep_prob') # plave holder that controlls the dropout rate
    return inputs,targets,lr,keep_prob

#preprocess the targets
    
def preprocess_targets(targets, word2int,batch_size):
    left_side =tf.fill([batch_size,1],word2int['<SOS>'])
    right_side = tf.strided_slice(target,[0,0],[batch_size,-1])
    
    