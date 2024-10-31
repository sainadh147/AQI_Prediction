import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
import joblib  # Importing joblib for saving the model

# Load dataset
data = pd.read_csv("aqi_data.csv")

# Defining features and target variable
train = data.drop(['AQI Value'], axis=1)  # Drop target column to create feature set
target = data['AQI Value']  # Target variable

# Splitting data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(train, target, test_size=0.2, random_state=42)

# Creating and fitting the model
m1 = RandomForestRegressor()
m1.fit(X_train, y_train)

# Save the trained model
joblib.dump(m1, "random_forest_aqi_model.pkl")

# Predicting on test set and calculating RMSE for model evaluation
y_pred = m1.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Square Error (RMSE) on Test Data: {rmse:.2f}")
