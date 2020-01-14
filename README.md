# Life Expectancy in the US

## Executive Summary

## Methodology
1. Data Import
2. Data Cleansing
3. Data Exploration  
  3.1 Overview of data via plots  
  3.2 Overview of target (Life expectancy)  
  3.3 Split training and test data
4. Feature Selection (Part 1): Evaluate predictors  
  4.1 Baseline model : calculate k-fold cv with all predictors  
  4.2 Evaluate predictors (Step 1) : Correlation of predictors vs. target (Life expectancy)  
  4.3 Evaluate predictors (Step 2) : Multicollinearity between all predictors  
  4.4 Model 1 : calculate k-fold cv using top predictors  
  4.5 Evaluate predictors (Step 3) : Interaction between top predictors  
  4.6 Evaluate predictors (Step 4): Polynomial terms  
  4.7 Add top interaction terms and top polynomial terms into data frame  
5. Feature Selection (Part 2) : Finalize predictors  
  5.1 Model 2 : use top predictors + top interactions + top polynomial terms  
  5.2 Determine strongest predictor terms (based on correlation  
  5.3 Determine strongest predictor terms (based on standardized coefficient)  
6. Final Model  
  6.1 Prepare final training and test data  
  6.2 Run final model with training and test data  
  6.3 Fine-tune with regularization techniques using Ridge and Lasso  
7. Conclusion
  
  
  

## Key findings & Conclusion
