import numpy as np


@np.vectorize
def sigmoid(x):
    sigmoid_range = 34.538776394910684
    if x <= -sigmoid_range:
        return 1e-15
    if x >= sigmoid_range:
        return 1.0 - 1e-15
    return 1.0 / (1.0 + np.exp(-x))


@np.vectorize
def difsigmoid(x):
    sigmoid_range = 34.538776394910684
    if x <= -sigmoid_range:
        y = 1e-15
    elif x >= sigmoid_range:
        y = 1.0 - 1e-15
    else:
        y = 1.0 / (1.0 + np.exp(-x))

    return (1.0 - y) * y
