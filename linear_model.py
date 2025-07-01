#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using Python to model Salary based on Years of Experience!! :)

# In[1]:


import pandas as pd
dataset = pd.read_csv("regression_data.csv")


# In[2]:


import matplotlib.pyplot as plt
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


# In[3]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[4]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[5]:


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[6]:


model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared


# yay i think i did it wooooooo

# I'm now beginning assignment 3. First I'm going to plot again with Matplotlib

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 4.3, 6.1, 8.0, 10.1])

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)

# Plot
plt.plot(x, y_pred, 'r-', label='Fitted Line')
plt.text(1.5, max(y) - 1,
         f"y = {slope:.2f}x + {intercept:.2f}\n"
         f"r = {r_value:.2f}\nMSE = {mse:.2f}",
         fontsize=12)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regression")
plt.legend()
plt.savefig("regression_plot_python.png")
plt.show()


# Here we can see the plot from the data! MSE is 0.01 for this, which is the error between the predictions and the actual values. 

# The code is reading the script and then interpreting the data to show this regression plot.

# In[ ]:




