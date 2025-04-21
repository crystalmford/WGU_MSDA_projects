# Customer Churn Prediction with Random Forest

This project builds a supervised machine learning model to predict customer churn based on service usage and demographic features. The goal is to identify customers at risk of leaving so that the business can proactively engage them and reduce attrition.

## Project Overview

- Classification problem using historical customer data
- Trained and tuned a Random Forest model
- Engineered over 700 features using binary encoding and one-hot encoding
- Evaluated with precision, recall, F1 score, and AUC-ROC

## Technologies Used

- Python
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
- Jupyter Notebook

## Data Preprocessing

- Removed irrelevant identifiers and geographic features
- Converted Yes/No fields to binary
- One-hot encoded categorical variables (e.g., contract type, job title)
- Split into training, validation, and test datasets

## Modeling Approach

- Random Forest Classifier
- GridSearchCV for hyperparameter tuning
- Performance measured using accuracy, precision, recall, F1 score, and AUC-ROC

## Results

The final model performed well in predicting churn on the test set, identifying high-risk customers with balanced precision and recall. This model supports business decision-making in customer retention strategy.

