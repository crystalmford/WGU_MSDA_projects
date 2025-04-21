# Customer Churn Prediction Model

This project explores customer churn using supervised machine learning classification. The objective is to predict which customers are likely to leave based on service usage, demographics, and account details.

## Problem Statement
Can we predict whether a customer will churn based on their service usage and demographic features? Identifying at-risk customers enables businesses to take proactive steps to improve retention.

## Technologies Used
- Python (pandas, numpy)
- Scikit-learn (RandomForestClassifier, train_test_split, GridSearchCV, evaluation metrics)
- Matplotlib & Seaborn (visualization)
- Jupyter Notebook

## Data Preparation
- Removed irrelevant features (IDs, location data)
- Converted Yes/No columns to binary
- One-hot encoded all categorical variables (contract type, service level, job titles)
- Final dataset included over 700 features due to expanded one-hot encoding

## Modeling Approach
- Applied Random Forest Classifier to handle high-dimensional feature space
- Used GridSearchCV for hyperparameter tuning
- Evaluated using accuracy, precision, recall, F1 score, and AUC-ROC

## Outcome
The final model successfully identified churn patterns with strong performance on validation data. The project demonstrates advanced feature engineering, model optimization, and practical business application in customer
