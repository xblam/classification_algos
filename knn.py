# first need to set up some random data points

import numpy as np
# the first thing that I need to do is to set up some random data points

# need to set the dimension of the datapoints as well
def generate_random_data(num_points=100, num_features=2):
    X = np.random.rand(num_points, num_features) 
    y = np.random.rand(num_points, num_features)
