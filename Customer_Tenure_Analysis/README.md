# Customer Tenure Analysis: Factors Influencing Retention

## Objective

This project explores which customer characteristics have the greatest influence on how long they remain subscribed to a service. The goal is to identify key drivers of customer tenure to help companies increase retention and reduce churn-related costs.

## Research Question

What customer factors influence tenure?

## Business Context

Customer retention is especially important in the telecommunications industry, where it can cost up to ten times more to acquire a new customer than to keep an existing one. Understanding the factors that contribute to longer customer relationships can help reduce churn and improve profitability.

## Dataset

The analysis uses a customer churn dataset containing variables related to demographics, service usage, contract types, and billing information. All data is anonymized and publicly available.

## Methodology

- **Exploratory Data Analysis (EDA)** to understand distributions and relationships
- **Correlation analysis** to identify variables most associated with tenure
- **Linear Regression modeling** to quantify the influence of selected variables
- **Feature selection** and **model refinement** to improve predictive performance

## Tools & Technologies

- Python (pandas, matplotlib, seaborn, scikit-learn)
- Jupyter Notebook

## Key Insights

- Contract type, monthly charges, and payment method showed significant correlation with tenure
- Longer-term contracts were positively associated with higher tenure
- Customers using electronic check were more likely to have shorter tenures

## How to Run This Project

1. Open the notebook `customer_tenure_analysis.ipynb` in Jupyter
2. Run the cells sequentially to see the data analysis and modeling workflow
