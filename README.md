# Life Expectancy in the US

## Executive Summary
We are taking the position of a consultancy company hired by the government to study the relationship between life expectancy in the US versus various factors related to health and lifestyle. The study's objective is to support the government in formulate healthcare policy based on the life expectancy model that we build.

Latest data indicates that there are large differences in life expectancy (over 20 years) between some counties: our model will be particularly useful in addressing healthcare issues in vulnerable counties to bring them at par to the rest of the country.

## Key files
1. <a href="https://docs.google.com/presentation/d/1lvWhw1TjPNJF9uzwCESKHKAFMNPAXIG8evZ8uMbkQ2M/edit?usp=sharing">Link here</a> : Presentation in Google Slides format
2. Life_Expectancy_USA.pdf : Presentation in PDF format
3. Life_Expectancy_USA.ipynb : Jupyter notebook file with Python codes + commentaries
4. Life_Analysis.py : local Python functions source file for Jupyter notebook
5. analytic_data2019.csv : Raw data source file in CSV format

## Methodology
1. **Data Import**
2. **Data Cleansing**  
  2.1 Clean-up columns and data  
  2.2 Remove outliers  
3. **Data Exploration**  
  3.1 Overview of all data via plots  
  3.2 Overview of target (Life expectancy)  
  3.3 Split and transform training and test data
4. **Feature Selection (Part 1): Evaluate predictors**  
  4.1 Baseline model : calculate k-fold cv with all predictors  
  4.2 Baseline model : investigate regularization using Lasso  
  4.3 Evaluate predictors (Step 1) : P-value of baseline predictors vs. target  
  4.4 Evaluate predictors (Step 2) : Correlation of predictors vs. target  
  4.5 Evaluate predictors (Step 3) : Multicollinearity between all predictors  
  4.6 Model 1 : using Top predictors  
  4.7 Evaluate predictors (Step 4) : Interaction between top predictors  
  4.8 Evaluate predictors (Step 5): Polynomial terms  
  4.9 Add top interaction terms and top polynomial terms into data frame  
5. **Feature Selection (Part 2) : Finalize predictors**  
  5.1 Model 2 : use Top predictors + interactions + polynomial terms  
  5.2 Determine strongest predictor terms (based on correlation)  
  5.3 Determine strongest predictor terms (based on standardized coefficient)  
  5.4 Evaluate linear regression model assumptions via residual analysis  
6. **Final Model**  
  6.1 Prepare final training and test data  
  6.2 Final model : run with training and test data

## Key findings

The first baseline model using all available predictors in the dataset gives a very high accuracy, but similar results would not be achieved in production due to overfitting of sample data. We employed several techniques to reduce the predictors based on the principles of correlation, multicollinearity, interaction between predictors, transforming predictors into polynomial terms, and regularization techniques using Ridge and Lasso.

Our final model generates an r-squared value of 71% for training data. R-squared value is defined as the proportion of the variance (difference between actual observed data and modelized output) of life expectancy that can be explained by the model's predictor variables.

For test data, we obtained an R-squared value of 66%, which suggests that our model does not fall into overfitting trap. In other words, the model is able adapt to unknown data and generates the same level of accuracy as during the development stage.

Here are the strongest contributing factors to predict life expectancy value in our model. The figures in parenthesis denote the model's absolute coefficient, which measures the relative weight of each predictor to the model's output.
1. [0.58] Teen births
2. [0.56] Adult smoking
3. [0.39] Diabetes prevalence
4. [0.32] Food insecurity
5. [0.29] Median household income
6. [0.26] Mental health providers
7. [0.25] Physical inactivity
8. [0.25] Mammography screening

## Conclusions
From the study and models conducted on the impact of various health and lifestyle factors to life expectancy in the US, we came up with following key conclusions:
- **Teen births, smoking** and **diabetes prevalence** are identified as top contributors to lower life expectancy.
- There is a **trade-off** that we needed to take between the model’s accuracy and the ability to predict using unseen data input.
- The **accuracy** of our model remains fairly unchanged when applied to new data set. We can conclude that it is a **reliable model** although more refinement can be done to improve its accuracy further.

## Recommendations
Here are the top 3 action plans that we propose to US federal and state agencies to improve life expectancy and to reduce this inequality between states and counties:
- **Sex education in school**: improvement in the quality of sex education curriculum in schools to be prioritized in order to reduce teen pregnancy, which came out as top factor in lowering life expectancy.
- **Food stamps programme**: food stamps programme to be extended to other vulnerable segments of the population to combat food insecurities via affordable access to food, and to combat diabetes via healthier food options.
- **Southern states** are in need the most: states in the south of the US, particularly Mississippi, Alabama and Louisiana are the key areas of focus where life expectancy is the lowest in order to bring the level in par with other parts of the country.


