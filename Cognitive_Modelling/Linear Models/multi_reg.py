import pandas as pd
import numpy as np
import statsmodels.api as sm

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load Dataset
diabetes = load_diabetes()

X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = diabetes.target

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Intercept :", model.intercept_)
print("\nCoefficients")
print(pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}))

print("\nMAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))
print("RMSE :", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score :", r2_score(y_test, y_pred))

# Statistical Summary
X_sm = sm.add_constant(X)
results = sm.OLS(y, X_sm).fit()

print(results.summary())