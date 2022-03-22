#%%
import tensorflow as tf
import numpy as np

a = tf.constant(np.array([1., 2., 3.]))
b = tf.constant(np.array([4., 5., 6.]))
c = tf.tensordot(a, b, 1)

c
#%%
