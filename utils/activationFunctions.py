import numpy as np

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

def sigmoidPrime(z):
    return np.multiply(sigmoid(z),(1-sigmoid(z)))

def softmax(z):
   return np.exp(z)/np.sum(np.exp(z))

def softmaxPrime(z):
    return (softmax(z)*(1-softmax(z)))
