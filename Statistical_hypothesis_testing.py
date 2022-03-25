# -*- coding: utf-8 -*-
"""
Created on 1401/01/05

@author : Behzad
"""
#P_Value and Alpha
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [2, 4, 6, 8, 2, 12, 10, 16]
c = [1, 3, 5, 11, 5, 4, 8, 16]
alpha = 0.02;
# plt.plot(a, b, marker = 'o', color = 'red')
# plt.plot(a, c, marker = 'o', color = 'green')
# print(pearsonr(a, b))
# print(pearsonr(a, c))
# plt.show()

#One Sample t-test
x= [20, 21, 21.5, 20.5, 19.5, 19, 20, 20.2]
from scipy.stats import ttest_1samp
t, p1=ttest_1samp(x, popmean=19.0)
t, p2=ttest_1samp(x, popmean=20.2)
print("p1: ", p1, "p2:", p2)

#Anova Test
from numpy import random as r
x = r.randn(10)
y = r.randn(10)
z = r.randn(10)
s = r.randn(10) + 2
from scipy.stats import f_oneway
F, p1=f_oneway(x, y, z)
F, p2=f_oneway(x, y, s)
print("p1: ", p1, "p2:", p2)

#Chi-Square Test
from scipy.stats import chi2_contingency
data=pd.read_excel(r'E:\Behzad\Programming\Data_Mining_Statistics_Python\data.xlsx')
table= pd.crosstab(data.eye_color, data.gender)
chi2, p, dof, expected = chi2_contingency(table)
print(table)
print("P-Value: ", p)
print("Degree of Freedom: ", dof)