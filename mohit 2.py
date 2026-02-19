import numpy as np
import matplotlib.pyplot as plt

# Given data (exclude x = 6 since y is unknown)
x = np.array([2, 3, 4, 5, 7, 8, 9, 10])
y = np.array([25, 33, 41, 53, 68, 80, 90, 110])

# Number of observations
n = len(x)

# Summations
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x**2)
sum_xy = np.sum(x*y)

# Least squares calculations
m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
c = (sum_y - m*sum_x) / n

# Predict missing value at x = 6
x_missing = 6
y_missing = m*x_missing + c

print("Slope (m):", m)
print("Intercept (c):", c)
print("Predicted y at x = 6:", y_missing)

# Regression line
x_line = np.linspace(2, 10, 100)
y_line = m*x_line + c

# Plot
plt.figure()
plt.scatter(x, y, label="Given data")
plt.plot(x_line, y_line, label="Regression line")
plt.scatter(x_missing, y_missing, label="Predicted point (x=6)")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression with Missing Value Prediction")
plt.legend()
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Given data (exclude x = 6 because y is unknown)
x = np.array([2, 3, 4, 5, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([25, 33, 41, 53, 68, 80, 90, 110])

# Create and train the model
model = LinearRegression()
model.fit(x, y)

# Get slope and intercept
m = model.coef_[0]
c = model.intercept_

print("Slope (m):", m)
print("Intercept (c):", c)

# Predict missing value at x = 6
x_missing = np.array([[6]])
y_missing = model.predict(x_missing)

print("Predicted value of y at x = 6:", y_missing[0])

# Generate regression line
x_line = np.linspace(2, 10, 100).reshape(-1, 1)
y_line = model.predict(x_line)

# Plot graph
plt.figure()
plt.scatter(x, y, label="Given data")
plt.plot(x_line, y_line, label="Regression line")
plt.scatter(x_missing, y_missing, label="Predicted point (x=6)")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression using scikit-learn")
plt.legend()
plt.show()
