# Customer Tenure Dashboard

## Overview

This project presents an interactive Tableau dashboard analyzing customer tenure and churn across various demographic and service-based segments. The goal is to provide executive stakeholders with clear, actionable insights into which customers stay longer, and how to better retain those who are likely to leave.

## Business Context

Customer churn is expensive — it costs up to 10x more to acquire a new customer than to retain an existing one. This dashboard was designed for a non-technical executive audience to help identify:

- Which types of customers stay longer
- Where churn is happening most (by age, income, location, race, gender)
- The impact of service bundling on retention

## Tools Used

- **Tableau** – for dashboard creation and visualization
- **WGU Churn Dataset** – core customer data
- **2015 US Census Demographics** – supplemental dataset for state-level insights

## Dashboard Features

- **Average Tenure by Demographics**
  - Filter by gender, age, income, race, and state population
  - Insight: Younger customers tend to churn less than older ones

- **Average Tenure by Service Subscription**
  - View how subscription types affect average tenure
  - Insight: Customers with more subscribed services have longer tenure

- **Churn Rate by Age and Race**
  - Compare churn patterns across demographic groups
  - Insight: Higher churn is seen among older customers

## Accessibility Considerations

- Used **shades of the same color** for better visibility for users with colorblindness
- Clear labels and tooltips on every data point
- No acronyms or jargon — content is understandable by a non-technical audience

## How to View

- Download the file `customer_tenure_dashboard.twbx`
- Open in [Tableau Desktop](https://www.tableau.com/products/desktop)

> Optional: If published to Tableau Public, include the link here:
> [View on Tableau Public](https://public.tableau.com/...)

## Key Takeaways

- More subscribed services = longer customer tenure
- Older customers churn more — explore potential causes (financial strain, lack of fit)
- Dashboards allow filtering by multiple factors to support targeted marketing or retention strategies
