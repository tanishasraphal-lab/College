import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import statsmodels.api as sm

np.random.seed(42)

# Generate sample data
X = np.random.uniform(1,20,150).reshape(-1,1)
noise = np.random.normal(0,4,150)
y = 5 + 3 * X[:,0] + noise

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Regression Line
idx = np.argsort(X_test[:,0])

plt.scatter(X_test, y_test)
plt.plot(X_test[idx], y_pred[idx], color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.show()

# Statistical Summary
X_sm = sm.add_constant(X)
results = sm.OLS(y, X_sm).fit()
print(results.summary())