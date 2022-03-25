# -*- coding: utf-8 -*-
"""
Created on 1401/01/05

@author: Behzad
"""

# Bernoulli Distribution

from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = bernoulli.rvs(size=400, p=0.15)
print(pd.Series(x).value_counts())
# plt.hist(x)
# plt.show()

# Bionomial Distribution

y = np.random.binomial(n=10, size=10000, p=0.5)
print(y)
print(pd.Series(y).value_counts())
#plt.hist(y)
#plt.show()

# Poisson distribution
# f(k; lambda) = Pr(X=k) = (lambda^k.e^{-lambda})/k!

import math

print(print("Poisson : ", (5 ** 3 * math.exp(-5)) / 6))

from numpy import random
x=random.poisson(lam = 1, size=10)
y=random.poisson(lam = 4, size=10)
print("x : ", x)
print("y : ", y)
print("x    Count\n", pd.Series(x).value_counts())
print("y    Count\n", pd.Series(y).value_counts())
#plt.hist(x)
#plt.hist(y)
#plt.show()

x=random.poisson(lam = 10, size=1000)
print("x : ", x)
print ("P(X=3) =" ,list(x).count(3)/len(x))
print ("P(X=5) =" ,list(x).count(5)/len(x))
#print("x    Count\n", pd.Series(x).value_counts())
#plt.hist(x)
#plt.show()

# Math Module

print("math.pi : " , math.pi)
print("math.sqrt(9) : ", math.sqrt(9))
print("math.exp(10): ", math.exp(10))
print("math.ceil(-4.2): ", math.ceil(-4.2))
print("math.floor(-4.2) : ", math.floor(-4.2))
print("math.sin(0) : ", math.sin(0))
print("math.cos(0) : ", math.cos(0))

# Uniform Distribution
x=random.uniform(size=10, low =1, high=3)
print("Uniform Distribution : " , x)

# Normal Distribution (Gaussian Or Bell Curve)

x=random.normal(size=10000, loc=175, scale=1.3)
y=random.normal(size=10000, loc=175, scale=13)
z=random.normal(size=10000, loc=184, scale=1.8)
#plt.hist(x, alpha=0.5)
#plt.hist(y, alpha=0.5)
#plt.hist(z, alpha=0.5)
#plt.show()

#Standard Normal Distribution (Z Distribution) (mu=0 and std=1)

x=random.normal(size=1000, loc=0, scale=1)
y=random.standard_normal(size=1000)
plt.hist(x, alpha=0.5)
plt.hist(y, alpha=0.5)
plt.show()