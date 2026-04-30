"""
House Price Prediction Assignment
Run this in VS Code
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("="*60)
print("HOUSE PRICE PREDICTION ASSIGNMENT")
print("="*60)

# Load data
print("\n📊 Loading California Housing dataset...")
housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['Price'] = housing.target

print(f"✅ Loaded {len(df)} records")
print(f"📋 Features: {', '.join(housing.feature_names)}")

# Prepare data
print("\n🔧 Preparing data for training...")
X = df.drop('Price', axis=1)
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"✅ Training set: {len(X_train)} records")
print(f"✅ Testing set: {len(X_test)} records")

# Train models
print("\n🤖 Training Linear Regression model...")
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

print("🤖 Training Random Forest model...")
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

# Evaluate
print("\n" + "="*50)
print("📈 MODEL RESULTS")
print("="*50)

for name, pred in [("Linear Regression", lr_pred), ("Random Forest", rf_pred)]:
    r2 = r2_score(y_test, pred)
    mae = mean_absolute_error(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    print(f"\n📊 {name}:")
    print(f"   R² Score (Accuracy): {r2:.2%}")
    print(f"   Mean Absolute Error: ${mae:.2f}00,000")
    print(f"   Root Mean Square Error: ${rmse:.2f}00,000")

# Determine best model
print("\n" + "="*50)
print("🏆 BEST MODEL")
print("="*50)

rf_r2 = r2_score(y_test, rf_pred)
lr_r2 = r2_score(y_test, lr_pred)

if rf_r2 > lr_r2:
    print("✅ Random Forest is the better model!")
    print(f"   {rf_r2 - lr_r2:.1%} better than Linear Regression")
else:
    print("✅ Linear Regression is the better model!")

print("\n" + "="*50)
print("✅ ASSIGNMENT COMPLETED SUCCESSFULLY!")
print("="*50)