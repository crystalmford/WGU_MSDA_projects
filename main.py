# main.py

# ----------------------------------------
# Step 1: Import Libraries
# ----------------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# ----------------------------------------
# Step 2: Load the Dataset
# ----------------------------------------
df = pd.read_csv("churn_clean.csv")

print("Dataset loaded successfully!")
print("Shape:", df.shape)

# ----------------------------------------
# Step 3: Handle Missing Values
# ----------------------------------------
# Fill missing values in 'InternetService' with "None"
df["InternetService"] = df["InternetService"].fillna("None")

# ----------------------------------------
# Step 4: Convert Target Variable to Binary
# ----------------------------------------
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# ----------------------------------------
# Step 5: One-Hot Encode Categorical Columns
# ----------------------------------------
df_encoded = pd.get_dummies(df, drop_first=True)

# ----------------------------------------
# Step 6: Prepare Features and Target
# ----------------------------------------
X = df_encoded.drop("Churn", axis=1)
y = df_encoded["Churn"]

# ----------------------------------------
# Step 7: Split Data into Train/Test Sets
# ----------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ----------------------------------------
# Step 8: Train a Logistic Regression Model
# ----------------------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ----------------------------------------
# Step 9: Predict and Evaluate
# ----------------------------------------
y_pred = model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
