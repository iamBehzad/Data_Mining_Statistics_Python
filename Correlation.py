# -*- coding: utf-8 -*-
"""
Created on 1401/01/04

@author : Behzad
"""

# Libraries
import statistics as st
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import pandas as pd

# Data
x = [1 ,2 ,4 ,5 ,7, 8]
y = [2 ,4 ,8 ,10 ,14, 16]

plt.scatter(x, y)
plt.show()

a=pearsonr(x, y)
print("Pearson1 : ", a)
print("-----------------------------------")
b=spearmanr(x, y)
print("Spearman1 : ", b)
print("-----------------------------------")

# Data
x = [1 ,2 ,4 ,5 ,7, 8]
y = [-2 ,-4 ,-8 ,-10 ,-14, -16]

plt.scatter(x, y)
plt.show()

a=pearsonr(x, y)
print("Pearson2 : ", a)
print("-----------------------------------")
b=spearmanr(x, y)
print("Spearman2 : ", b)
print("-----------------------------------")

# Data
x = [1 ,2 ,4 ,5 ,7, 8]
y = [2 ,4 ,-8 ,10 ,-14, -16]

plt.scatter(x, y)
plt.show()

a=pearsonr(x, y)
print("Pearson3 : ", a)
print("-----------------------------------")
b=spearmanr(x, y)
print("Spearman3 : ", b)
print("-----------------------------------")

