# Customer Revenue Forecasting with ARIMA

This project applies time series forecasting techniques to predict future customer revenue. Using monthly revenue data, the model analyzes historical patterns to estimate future trends and inform business planning decisions.

## Project Overview
- Goal: Forecast customer revenue over time
- Method: ARIMA modeling with differencing to handle trend and seasonality
- Validation: Actual vs. predicted plots and confidence intervals

## Technologies Used
- Python (pandas, numpy, statsmodels)
- Jupyter Notebook
- Matplotlib (visualization)

## Key Steps
- Performed stationarity checks and visualized ACF/PACF plots
- Applied differencing to stabilize the time series
- Tuned ARIMA parameters using AIC/BIC scores
- Forecasted future revenue with confidence intervals
- Evaluated model with visual inspection and performance metrics

## Outcome
The model successfully forecasted future customer revenue based on historical trends. Insights from this model can help inform resource planning, budgeting, and performance evaluation.

This PDF report outlines the methodology, forecasting results, and key takeaways for revenue prediction using ARIMA.

> Note: While the file is named `churn_clean.csv` for consistency across projects, in this analysis it is used for modeling and forecasting monthly revenue trends.
