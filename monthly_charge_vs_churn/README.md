# Monthly Charges and Customer Churn

## Research Question

Are customers who pay higher monthly charges more likely to churn (cancel their service)?

- **Null Hypothesis (H₀):** A customer's monthly charge has no effect on the churn rate.
- **Alternative Hypothesis (H₁):** Customers with higher monthly charges are more likely to churn.

## Business Context

This analysis explores whether high monthly charges are associated with increased customer churn. Retaining customers is critical — it can cost 10x more to acquire a new customer than to retain an existing one. If monthly charges are driving customers away, pricing strategies may need to be reconsidered.

## Dataset Variables Used

- **Churn**: Indicates whether the customer has canceled their subscription (Yes/No)
- **MonthlyCharge**: The customer's average monthly billing amount
- Additional variables used in exploratory analysis include:
  - `Income` (continuous)
  - `Gender`, `Marital` (categorical)
  - `InternetService`, `Bandwidth_GB_Year`

---

## Analysis Methodology

### Hypothesis Test

A two-sample t-test was conducted to compare the average monthly charges of customers who churned vs. those who did not. Monthly charges were grouped by churn status and tested to determine if a significant difference exists.

### Justification

A two-sample t-test is appropriate when comparing the means of two independent groups (Churn: Yes vs. No) for a continuous variable (MonthlyCharge). The results showed a statistically significant difference, suggesting customers who churn tend to pay higher monthly charges.

---

## Exploratory Data Analysis

### Univariate Analysis

#### Income
- Majority of reported incomes are below $100,000
- Mean income is under $40,000, which is lower than the U.S. average (~$74,000 in 2023)

#### Monthly Charges
- Mean monthly charge is approximately $172
- High relative to income — could indicate pricing pressure

#### Gender & Marital Status
- Gender distribution is relatively even
- Marital status is unexpectedly balanced — may reflect the artificial nature of the dataset

### Visualizations
- Histograms and boxplots for `Income`, `MonthlyCharge`, `Gender`, and `Marital`
- Summary statistics using `.describe()` and `.value_counts()`

---

## Bivariate Analysis

### 1. Income vs. Gender
- Boxplot visualization
- Very little visible difference in reported income between genders
- Real-world data typically shows income inequality — this is likely a limitation of the dataset

### 2. Bandwidth Usage vs. Internet Service
- Compared data usage across different service types (e.g., DSL vs. Fiber Optic)
- Unexpected results (e.g., lower usage on fiber) may reflect sample imbalance or data quality issues

---

## Statistical Results

- The two-sample t-test returned a **p-value well below 0.05**
- This suggests that customers who churn tend to pay significantly higher monthly charges
- Therefore, we reject the null hypothesis

---

## Limitations

- **Sample Size**: Dataset has ~10,000 rows, which may not represent the full customer base
- **Service Breakdown**: MonthlyCharge variable doesn't account for differences in subscribed services
- **Synthetic Data**: The dataset is not real, which may affect the generalizability of results

---

## Recommendations

- Investigate pricing structure and customer retention strategies
- Consider discounts or loyalty programs to retain customers with high bills
- Explore additional factors influencing churn beyond monthly charges

---

## References

- Internal course resources:
  - DataCamp
  - Webinar Series
