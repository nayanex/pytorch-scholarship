import numpy as np
from math import log

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    cross_entropy = 0
    for event, prob in zip(Y, P):
        cross_entropy -= event*log(prob) + (1-event)*log(1-prob)
    return cross_entropy

print(cross_entropy([1, 1, 0], [0.8, 0.7, 0.1]))


"""
Trying for Y=[1,0,1,1] and P=[0.4,0.6,0.1,0.5]. The correct answer is 4.8283137373

UDACITY SOLUTION 

Y = np.float_(Y)
P = np.float_(P)
return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))

"""