# Monthly Charge Data Cleaning

## Objective

This project focuses on preparing a telecommunications customer dataset for analysis. The goal is to identify and address common data quality issues in preparation for modeling monthly charges based on customer demographics and service usage patterns.

## Research Question

What customer factors influence monthly charge?

## Context

Understanding what drives monthly charges can help with targeted marketing, pricing strategies, and customer segmentation. Before this analysis can take place, it’s critical to ensure the dataset is clean and reliable.

## Tools & Technologies

- **R**
- RStudio
- `dplyr`, `tidyr`, `visdat`, and base R functions

## Cleaning Steps

- Imported raw CSV data into R
- Checked for data type mismatches
- Identified and removed duplicates using `duplicated()`
- Located and handled missing values using `colSums(is.na())` and `vis_miss()`
- Detected outliers using Z-scores via `scale()`
- Assessed categorical variables for potential reclassification

## Outcome

The final cleaned dataset is ready for exploratory analysis or modeling to answer the primary research question.

## How to Run

1. Open the script in RStudio: `monthly_charge_cleaning.R`
2. Ensure required libraries are installed: `dplyr`, `visdat`, `tidyr`
3. Follow the comments in the script to reproduce the cleaning steps

---

This project demonstrates practical skills in data wrangling, exploratory data quality assessment, and preparation of a dataset for downstream analysis in a real-world business context.

