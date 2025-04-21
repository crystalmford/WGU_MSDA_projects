import pandas as pd
import numpy as np

# Load the cleaned dataset
file_path = r'C:\Users\Crystal\OneDrive\Desktop\d602\task 2\d602-deployment-task-2\data\cleaned_data_v2.csv'
df = pd.read_csv(file_path)

# Ensure SCHEDULED_DEPARTURE is numeric
df['SCHEDULED_DEPARTURE'] = pd.to_numeric(df['SCHEDULED_DEPARTURE'], errors='coerce')

# Filter data to only include departures from ATL
df_atl = df[df['DEST_AIRPORT'] == 'ATL']
# Drop rows with missing departure time
df_atl = df_atl.dropna(subset=['SCHEDULED_DEPARTURE'])

# Remove extreme delays (> 60 minutes) to match the previous analyst's notebook
df_atl['DEPARTURE_DELAY'] = df_atl['DEPARTURE_DELAY'].apply(lambda x: x if x < 60 else np.nan)
df_atl = df_atl.dropna()

# Convert SCHEDULED_DEPARTURE (HHMM) to seconds since midnight
def time_to_seconds(time_value):
    time_str = str(int(time_value)).zfill(4)
    hour, minute = int(time_str[:2]), int(time_str[2:])
    return hour * 3600 + minute * 60

df_atl['SCHEDULED_DEPARTURE'] = df_atl['SCHEDULED_DEPARTURE'].apply(time_to_seconds)

# Save the filtered dataset
filtered_file_path = r'C:\Users\Crystal\OneDrive\Desktop\d602\task 2\d602-deployment-task-2\data\filtered_atl_data_v2.csv'
df_atl.to_csv(filtered_file_path, index=False)

# Print summary
print(f"Filtered ATL data saved to {filtered_file_path}")
print(df_atl.head())
