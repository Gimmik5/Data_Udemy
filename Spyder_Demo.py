# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
dataset = pd.read_csv("C:/Users/Gideon Bergbaum/Python_Udemy/HR_file.csv")

#createa a visual
plt.figure(figsize=(10,5))
sns.countplot(data=dataset,x='Departments',palette='tab10', hue='salary')

#Create a jointplot
sns.jointplot(data=dataset, x='satisfaction_level', y='last_evaluation',kind='kde',hue='salary')
sns.jointplot(data=dataset, x='satisfaction_level', y='last_evaluation',kind='hex')