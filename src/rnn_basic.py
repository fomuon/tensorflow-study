import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn
import pprint

pp = pprint.PrettyPrinter(indent=4)
sess = tf.InteractiveSession()

h = [1,0,0,0]
e = [0,1,0,0]
l = [0,0,1,0]
o = [0,0,0,1]

'''
#One cell RNN input_dim (4) -> output_dim (2)
hidden_size = 2
cell = rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)

x_data = np.array([[h,e,l,l,o]], dtype=np.float32)
print(x_data)
outputs, _states = tf.nn.dynamic_rnn(cell, x_data, dtype=tf.float32)

sess.run(tf.global_variables_initializer())
pp.pprint(outputs.eval())
'''


# One cell RNN input_dim (4) -> output_dim (2). sequence: 5, batch 3
# 3 batches 'hello', 'eolll', 'lleel'
cell = rnn.BasicLSTMCell(num_units=2, state_is_tuple=True)

x_data = np.array([[h, e, l, l, o],[e, o, l, l, l],[l, l, e, e,l]], dtype = np.float32)
pp.pprint(x_data)
outputs, states = tf.nn.dynamic_rnn(cell, x_data, dtype=tf.float32)

sess.run(tf.global_variables_initializer())
pp.pprint(outputs.eval())