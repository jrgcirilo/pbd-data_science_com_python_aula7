from collections import defaultdict
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np
import math
import random

def scalar_multiply (scalar, vector):
    return [scalar * i for i in vector]

def vector_sum (vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = [result[i] + vector[i] for i in range(len(vector))]
    return result

def vector_mean(vectors):
    return scalar_multiply(1/len(vectors), vector_sum(vectors))

def dot (v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def vector_subtract (v, w):
    return [v_i - w_i for v_i, w_i in zip (v, w)]

def sum_of_squares (v):
    return dot (v, v)

def squared_distance (v, w):
    return sum_of_squares (vector_subtract(v, w))

def distance (v, w):
    return math.sqrt(squared_distance(v, w))

class KMeans:
    def __init__ (self, k, means = None):
        self.k = k
        self.means = means

    def classify (self, point):
        return min (range (self.k), key = lambda i: squared_distance(point, self.means[i]))

    def train (self, points):
        
        assignments = None
        while True:
            new_assignments = list(map (self.classify, points))
            if new_assignments == assignments:
                return
            assignments = new_assignments
            for i in range (self.k):
                i_points = [p for p, a in zip (points, assignments) if a == i] 
                if i_points:
                    self.means[i] = vector_mean (i_points)

def gets_better_k (base, i, threshold):
    x = 2
    y = 0
    data_base = base[0]
    chosen_data = base[1]

    lower_index_k = x
    while x <= i:
        kmeans = KMeans(x, chosen_data)
        kmeans.train(data_base)
        km = kmeans.means
        y = vector_mean(km)
        if (y[0] < threshold):
            lower_index_k = x
        x += 1
        print(y)
    return lower_index_k

def test_data_k_means ():
    i = 4
    threshold = 30
    data = [[1], [3], [6], [9], [12], [15], [18], [21], [24], [27], [30]]
    chosen_data = [[1], [6], [12], [18]]
    
    base = [data, chosen_data]
    lower_k = gets_better_k (base, i, threshold)
    print(f'If threshold is {threshold}, the lower K is: {lower_k}')
   
test_data_k_means()
