import pandas as pd
import numpy as np

# Load the raw dataset
file_path = r"C:\Users\Crystal\OneDrive\Desktop\d602\task 2\d602-deployment-task-2\data\T_ONTIME_REPORTING.csv"
df = pd.read_csv(file_path)

# Rename columns to match the previous analyst’s format
df = df.rename(columns={
    'CRS_DEP_TIME': 'SCHEDULED_DEPARTURE',
    'CRS_ARR_TIME': 'SCHEDULED_ARRIVAL',
    'DEST': 'DEST_AIRPORT',
    'DEP_DELAY': 'DEPARTURE_DELAY'
})

# Select only the required columns
df = df[['SCHEDULED_DEPARTURE', 'SCHEDULED_ARRIVAL', 'DEST_AIRPORT', 'DEPARTURE_DELAY']]

# Drop missing values
df = df.dropna()

# Remove extreme delays (> 60 minutes)
df['DEPARTURE_DELAY'] = df['DEPARTURE_DELAY'].apply(lambda x: x if x < 60 else np.nan)
df = df.dropna()

# Convert SCHEDULED_DEPARTURE (HHMM format) to seconds since midnight
def time_to_seconds(time_value):
    # Ensure time_value is treated as a string, then extract hour and minute
    time_str = str(int(time_value)).zfill(4)  # Convert to string and pad with zeros if needed
    hour, minute = int(time_str[:2]), int(time_str[2:])
    return hour * 3600 + minute * 60  # Convert to total seconds

df['SCHEDULED_DEPARTURE'] = df['SCHEDULED_DEPARTURE'].apply(time_to_seconds)

# Save the cleaned data
cleaned_file_path = r"C:\Users\Crystal\OneDrive\Desktop\d602\task 2\d602-deployment-task-2\data\cleaned_T_ONTIME_REPORTING.csv"
df.to_csv(cleaned_file_path, index=False)

# Print summary
print(f"Cleaned data saved to {cleaned_file_path}")
print(df.head())
