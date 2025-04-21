# poly_regressor_Python_1.0.0.py
# Description: Polynomial regression model to predict flight delays using Ridge Regression.
# MLflow is used for experiment tracking.

import datetime
import pandas as pd
import argparse
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures, LabelEncoder, OneHotEncoder
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import mlflow
import mlflow.sklearn
import logging
import pickle

# Set up argument parser
parser = argparse.ArgumentParser(description="Polynomial regression for flight delays")
parser.add_argument("--num_alphas", type=int, default=20, help="Number of Ridge regression alpha values to try")
parser.add_argument("--order", type=int, default=1, help="Degree of polynomial features")
args = parser.parse_args()

num_alphas = args.num_alphas
order = args.order

# Configure logger
logging.basicConfig(
    filename="polynomial_regression.txt",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)
logging.info("Flight Departure Delays Polynomial Regression Model Log")

# Read data file
df = pd.read_csv("data/filtered_cleaned_data.csv")

# Construct full DATE column
df['DATE'] = pd.to_datetime(df[['YEAR', 'MONTH', 'DAY']])

# Convert SCHEDULED_DEPARTURE and SCHEDULED_ARRIVAL to full datetime
df['SCHEDULED_DEPARTURE'] = pd.to_datetime(df['DATE'].astype(str) + ' ' + df['SCHEDULED_DEPARTURE'].astype(str).str.zfill(4), format='%Y-%m-%d %H%M', errors='coerce')
df['SCHEDULED_ARRIVAL'] = pd.to_datetime(df['DATE'].astype(str) + ' ' + df['SCHEDULED_ARRIVAL'].astype(str).str.zfill(4), format='%Y-%m-%d %H%M', errors='coerce')

# Verify the conversion
print(df[['DATE', 'SCHEDULED_DEPARTURE', 'SCHEDULED_ARRIVAL']].head())

# Check for NaT values
if df['SCHEDULED_DEPARTURE'].isna().sum() > 0:
    print("Warning: Some departure times could not be converted:")
    print(df[df['SCHEDULED_DEPARTURE'].isna()].head())
    raise ValueError("Error: SCHEDULED_DEPARTURE conversion failed. Check input data formatting.")


# Prepare dataset
def create_df(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df[["SCHEDULED_DEPARTURE", "SCHEDULED_ARRIVAL", "DEST_AIRPORT", "DEPARTURE_DELAY"]].copy()
    df2.dropna(inplace=True)
    df2["weekday"] = df2["SCHEDULED_DEPARTURE"].apply(lambda x: x.weekday())
    df2["DEPARTURE_DELAY"] = df2["DEPARTURE_DELAY"].apply(lambda x: x if x < 60 else np.nan)
    df2.dropna(inplace=True)
    df2["hour_depart"] = df2["SCHEDULED_DEPARTURE"].apply(lambda x: x.hour * 3600 + x.minute * 60)
    df2["hour_arrive"] = df2["SCHEDULED_ARRIVAL"].apply(lambda x: x.hour * 3600 + x.minute * 60)
    return df2[["hour_depart", "hour_arrive", "DEST_AIRPORT", "DEPARTURE_DELAY", "weekday"]]

# Split data: first 3 weeks for training, last week for testing
df_train = df[df["SCHEDULED_DEPARTURE"].apply(lambda x: x is not np.nan and x.day < 23)]
df_test = df[df["SCHEDULED_DEPARTURE"].apply(lambda x: x is not np.nan and x.day >= 23)]

# Process training data
df3 = create_df(df_train)
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(df3["DEST_AIRPORT"])
onehot_encoder = OneHotEncoder(sparse_output=False)
integer_encoded = integer_encoded.reshape(-1, 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
X = np.hstack((onehot_encoded, df3[["hour_depart", "hour_arrive"]]))
Y = df3["DEPARTURE_DELAY"].values.reshape(-1, 1)

# Train-validation split
X_train, X_validate, Y_train, Y_validate = train_test_split(X, Y, test_size=0.3)

# Set up MLflow experiment
experiment_name = "Airport Departure Delays " + str(datetime.date.today())
mlflow.set_experiment(experiment_name)
run_name = "Run at " + datetime.datetime.now().strftime("%H:%M")

parameters = [0, order]

with mlflow.start_run(run_name=run_name):
    score_min = float("inf")
    for alpha in np.linspace(0, num_alphas * 0.2, num_alphas):
        ridgereg = Ridge(alpha=alpha)
        poly = PolynomialFeatures(degree=order)
        X_ = poly.fit_transform(X_train)
        ridgereg.fit(X_, Y_train)
        result = ridgereg.predict(poly.transform(X_validate))
        score = metrics.mean_squared_error(result, Y_validate)
        with mlflow.start_run(run_name=f"Run {alpha:.1f}", nested=True):
            mlflow.log_param("alpha", alpha)
            mlflow.log_metric("MSE", score)
        if score < score_min:
            score_min = score
            parameters = [alpha, order]
    mlflow.log_param("Best Alpha", parameters[0])
    mlflow.log_param("Polynomial Order", parameters[1])
    mlflow.log_metric("Final MSE", score_min)

# Save final model
pickle.dump(ridgereg, open("finalized_model.pkl", "wb"))
mlflow.log_artifact("finalized_model.pkl")

mlflow.end_run()
print("Script completed successfully!")
