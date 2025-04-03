# Tech Inclination Prediction: Modeling Customer Self-Identification as "Techie"

## Objective

This project explores which customer characteristics are most strongly associated with a customer self-identifying as "Techie" — someone who considers themselves technically inclined. Understanding this relationship may help identify opportunities to tailor services, provide targeted training, or develop new features that appeal to more or less technically inclined users.

## Research Question

Which factors most significantly contribute to a customer self-identifying as "Techie"?

## Business Context

Customers who identify as technically inclined may be more likely to adopt additional, higher-tier, or technical services. Conversely, those who are less confident with technology might benefit from support or simplified offerings. By modeling this relationship, businesses can tailor communication and service packages accordingly.

## Dataset

This project uses the same customer churn dataset as other projects in this repository. It includes customer demographics, subscription behavior, and self-reported characteristics (including the "Techie" label).

## Methodology

- **Data Preprocessing**
  - Cleaned and prepared categorical and numeric variables
  - Checked for multicollinearity among explanatory variables
- **Modeling**
  - Built a logistic regression model to predict the binary outcome ("Techie" or not)
- **Evaluation**
  - Used standard classification metrics (accuracy, precision, recall)
  - Interpreted coefficients to understand feature impact

## Tools & Technologies

- Python
- pandas, numpy
- seaborn, matplotlib
- statsmodels, sklearn

## Key Insights

- Certain service subscription patterns were correlated with self-identified techie status
- Features like streaming usage and contract types showed measurable influence
- Understanding these factors could inform both upsell strategies and training programs

## How to Run This Project

1. Open the notebook `techie_prediction_model.ipynb` in Jupyter or VS Code.
2. Run the cells in order to reproduce the analysis and model.
3. Ensure required packages are installed (`pandas`, `sklearn`, etc.).

## Next Steps

Future work could expand this analysis by:
- Testing more complex models (e.g., decision trees or random forests)
- Performing deeper feature engineering
- Segmenting customers by tech confidence levels for targeted outreach
