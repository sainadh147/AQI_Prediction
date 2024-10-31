import pandas as pd

# Create a DataFrame
data = {
    'CO AQI Value': [1, 1, 1, 1, 1, 1, 1, 1],
    'Ozone AQI Value': [36, 5, 5, 39, 34, 14, 14, 29],
    'NO2 AQI Value': [0, 1, 1, 2, 0, 11, 11, 7],
    'PM2.5 AQI Value': [51, 41, 41, 66, 20, 54, 54, 64],
    'lat': [44.7444, -5.2900, -11.2958, 37.1667, 53.0167, 16.1005, 26.8941, 51.0761],
    'lng': [44.2031, -44.4900, -41.9869, 15.1833, 20.8833, -88.8074, -82.0513, 4.2803]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("new_aqi_data.csv", index=False)
