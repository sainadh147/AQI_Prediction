import pandas as pd
import joblib

# Load the saved model
m1 = joblib.load("random_forest_aqi_model.pkl")

# Load the new dataset
new_data = pd.read_csv("new_data.csv")  # Make sure this file is in the same directory or provide a full path

# Predict AQI values for the new dataset
aqi_predictions = m1.predict(new_data)

# Add predictions to the DataFrame
new_data['Predicted AQI'] = aqi_predictions

# Save or display the results
new_data.to_csv("predicted_aqi_data.csv", index=False)
print(new_data[['Predicted AQI']])
