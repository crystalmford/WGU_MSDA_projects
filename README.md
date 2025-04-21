# Monthly Charge vs. Churn Analysis

This project explores whether there is a statistically significant relationship between a customer's monthly service charge and their likelihood to churn. It was developed as part of an applied analytics assignment using the WGU churn dataset.

## Research Question

Are customers paying a higher monthly charge more likely to churn?

- **Null Hypothesis (H0):** A customer’s monthly charge has no effect on churn rate.
- **Alternative Hypothesis (HA):** Customers with higher monthly charges are more likely to churn.

## Business Impact

Customer churn is costly — acquiring a new customer is up to 10x more expensive than retaining one. This analysis provides insight into how pricing may influence churn behavior, helping stakeholders determine whether pricing adjustments, discounts, or loyalty incentives are needed to retain existing customers.

## Tools & Methods

- **Python (pandas, seaborn, matplotlib, scipy.stats)** for data cleaning, visualization, and statistical testing
- **Two-sample t-test** to compare mean monthly charges between churned vs. non-churned customers
- **Descriptive statistics** and **univariate/bivariate visualizations** for deeper exploration

## Key Variables

- `Churn` (categorical): Whether a customer discontinued service
- `MonthlyCharge` (continuous): Average monthly service charge
- Additional features explored: `Income`, `Gender`, `Marital`, `InternetService`, `Bandwidth_GB_Year`

## Statistical Findings

- The two-sample t-test returned a **p-value below 0.05**, suggesting the null hypothesis can be rejected.
- Customers who churned had **significantly higher average monthly charges** than those who did not.
- Univariate analysis revealed:
  - Most customers reported **incomes under $40,000/year**
  - **Average monthly charge was $172**, which appears high relative to income levels
- Bivariate analysis showed:
  - **No major difference** in income by gender
  - **Unexpected patterns** in bandwidth usage by internet service type

## Visualizations Included

- Histograms of income, gender, and marital status
- Boxplots of monthly charges, income by gender, and bandwidth usage by service type
- Value counts for categorical variables

## Limitations

- Dataset sample size (n=10,000) may not represent a full customer base
- No control for service tier — higher charges may reflect more premium service packages
- Dataset is synthetic and not fully aligned with real-world pricing behavior

## Recommendations

- Investigate the **pricing structure** for high-churn customers
- Consider offering **discounts or loyalty rewards** to retain customers with higher charges
- Conduct follow-up analysis that controls for service type, contract length, and customer tenure

## How to Run

This project is written in Python. To run locally:

```bash
pip install pandas matplotlib seaborn scipy
python monthly_charge_vs_churn_analysis.py

