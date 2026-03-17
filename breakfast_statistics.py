import numpy as np
import matplotlib.pyplot as plt

# Breakfast data (days per week)
breakfast_days = [
4,5,2,0,0,5,4,5,0,0,
0,0,5,4,1,0,5,5,0,4,
0,0,0,5,5,0,3,5,5,0,
5,5,0,0,0,0,5,1,5,5,
5,5,5,0,5,1,5,5,0,0,
0,5,0,5,5
]

# Replace with your actual GPA values (50 values)
gpa = [
3.9, 4.069, 3.1, 4.04, 5.23,
5.057, 5.03, 5.139, 4.33, 4.33,
4.5, 4.04, 4.4, 4.743, 3.89,
4.813, 4.6, 4.738, 4.2, 3.2,
4.787, 4.2, 4.711, 5.2, 4.9,
4.1, 4.76, 5.188, 4.7, 4.641,
3.4, 4.2, 4.2, 3.5, 4.4,
4.667, 4.6, 3.7, 5.145, 5.13,
4.95, 3.627, 3.7, 4.926, 4.2,
4.0, 4.222, 4.4, 3.7, 4.3,
3.8, 4.5, 4.0, 4.5, 2.889
]

# Convert to numpy arrays
x = np.array(breakfast_days)
y = np.array(gpa)

# Calculate correlation coefficient (r)
r = np.corrcoef(x, y)[0,1]

# Calculate r^2
r_squared = r**2

# Linear regression (best-fit line)
slope, intercept = np.polyfit(x, y, 1)

# Predicted values for regression line
y_pred = slope * x + intercept

# Scatterplot
plt.scatter(x, y)

# Regression line
plt.plot(x, y_pred)

plt.xlabel("Days Eating Breakfast Per Week")
plt.ylabel("GPA")
plt.title("Relationship Between Breakfast Frequency and GPA")
plt.scatter(x + np.random.normal(0,0.05,len(x)), y)
plt.show()

print("Correlation coefficient (r):", r)
print("Coefficient of determination (r^2):", r_squared)
print("Regression line: GPA =", slope, "* (Breakfast Days) +", intercept)

import numpy as np

data = [
4,5,2,0,0,5,4,5,0,0,
0,0,5,4,1,0,5,5,0,4,
0,0,0,5,5,0,3,5,5,0,
5,5,0,0,0,0,5,1,5,5,
5,5,5,0,5,1,5,5,0,0,
0,5,0,5,5
]

n = len(data)
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data, ddof=1)   # sample standard deviation
minimum = np.min(data)
maximum = np.max(data)

print("Sample size (n):", n)
print("Mean:", round(mean, 2))
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Minimum:", minimum)
print("Maximum:", maximum)

import math
from scipy.stats import norm

# Given values
n = 55                 # sample size
x =  24                 # number who selected 5 days (replace this)
p0 = 0.274             # national average
alpha = 0.05

# Sample proportion
phat = x / n

# Standard error under H0
SE = math.sqrt((p0 * (1 - p0)) / n)

# Test statistic
z = (phat - p0) / SE

# One-sided p-value (since Ha: p > 0.274)
p_value = 1 - norm.cdf(z)

print("Sample proportion:", phat)
print("Z-statistic:", z)
print("P-value:", p_value)

import numpy as np
from math import sqrt

# breakfast data
breakfast_days = [
4,5,2,0,0,5,4,5,0,0,
0,0,5,4,1,0,5,5,0,4,
0,0,0,5,5,0,3,5,5,0,
5,5,0,0,0,0,5,1,5,5,
5,5,5,0,5,1,5,5,0,0,
0,5,0,5,5
]

n = len(breakfast_days)

# number of successes (students eating breakfast 5 days)
successes = breakfast_days.count(5)

# sample proportion
p_hat = successes / n

# 95% confidence interval
z = 1.96
SE = sqrt((p_hat*(1-p_hat))/n)

lower = p_hat - z*SE
upper = p_hat + z*SE

print("Sample size:", n)
print("Successes:", successes)
print("Sample proportion:", p_hat)
print("95% CI:", (lower, upper))

import numpy as np
from scipy.stats import chi2_contingency

table = np.array([
[6,5],   # 9th
[4,11],  # 10th
[6,8],   # 11th
[8,7]    # 12th
])

chi2, p, dof, expected = chi2_contingency(table)

print("Chi-square statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)
print("Expected counts:")
print(expected)
