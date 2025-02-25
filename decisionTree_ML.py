import pandas as pd
import ast
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

#  Step 1: Load CSV File
df = pd.read_csv("circuit_features2.csv")

#  Step 2: Extract Features (X) and Target (y)
X = df[["Max Fan-in", "Max Fan-out", "Number of Gates", "AND", "OR", "XOR","NOT", "wires"]]  
y = df["Combinational Depth"]  # Target variable

#  Step 3: Split Data into Train & Test Sets (Stratify if More Data Available)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Step 4: Initialize and Train Decision Tree Model
model = DecisionTreeRegressor(max_depth=4, random_state=42)  # Limit depth to avoid overfitting
model.fit(X_train, y_train)

#  Step 5: Cross-Validation for Small Data (Ensures Better Generalization)
scores = cross_val_score(model, X, y, cv=5, scoring="neg_mean_squared_error")
print(f"Cross-Validation MSE: {-scores.mean()}")

#  Step 6: Make Predictions
y_pred = model.predict(X_test)

#  Step 7: Evaluate Model Performance
mse = mean_squared_error(y_test, y_pred)
print(f"Test Mean Squared Error: {mse}")

#  Step 8: Predict for New Circuit (Example)
sample_data = [[2, 2, 7, 2, 2, 2,1, 11]]  # Example: (Fan-in, Fan-out, Gates, AND, OR, XOR,NOT, wires)
prediction = model.predict(sample_data)
print(f"Predicted Combinational Depth: {prediction[0]}")
