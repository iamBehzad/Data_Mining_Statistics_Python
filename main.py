# -*- coding: utf-8 -*-
"""
Created on 1401/01/04

@author : Behzad
"""

# libraries
import statistics as st
import numpy as np
from scipy import stats

# data
Scores = [20, 20, 18, 18, 20, 17, 17, 18, 14, 12, 18, 20]

# Mean
a = st.mean(Scores)
print("Mean Calculation with Stats : ", a)
print("-----------------------------------")
a = np.mean(Scores)
print("Mean Calculation with Numpy : ", a)
print("-----------------------------------")

# Mode
c = stats.mode(Scores)  # in scipy one's that is smaller choose as mode
print("Mode Calculation with Stats : ", c)
print("-----------------------------------")
d = st.mode(Scores)  # in Statistics one's that is first finding, chosen as mode
print("Mode Calculation with statistics : ", d)
print("-----------------------------------")
print("Count Of 20 : ", Scores.count(20))
print("-----------------------------------")
print("Count Of 18 : ", Scores.count(18))
print("-----------------------------------")

# Median
e = st.median(Scores)  # in scipy one's that is smaller choose as mode
print("Median Calculation with Statistics : ", e)
print("-----------------------------------")
f = np.median(Scores)  # in Statistics one's that is first finding, chosen as mode
print("Median Calculation with Numpy : ", f)
print("-----------------------------------")

# Sort Scores
Scores.sort()
print("Sorted Scores : ", Scores)
print("-----------------------------------")

# Quantiles
Q2 = np.quantile(Scores, 0.5)
Q1 = np.quantile(Scores, 0.25)
Q3 = np.quantile(Scores, 0.75)
print("Q1 : ", Q1)
print("Q2 : ", Q2)
print("Q3 : ", Q3)
print("-----------------------------------")

# Variance
g = np.var(Scores)
print("Variance Calculation with Numpy : ", g)
print("-----------------------------------")
h = st.variance(Scores)
print("Variance Calculation with Statistics (Scores as a Sample): ", h)
print("-----------------------------------")
h = st.pvariance(Scores)
print("Variance Calculation with Statistics (Scores as a Population): ", h)
print("-----------------------------------")

#Standard Deviation
i = np.std(Scores)
print("Standard Deviation Calculation with Numpy : ", i )
print("-----------------------------------")
k = st.stdev(Scores)
print("Standard Deviation Calculation with Statistics (Scores as a Sample): ", k)
print("-----------------------------------")
j = st.pstdev(Scores)
print("Standard Deviation Calculation with Statistics (Scores as a Population): ", j)
print("-----------------------------------")
