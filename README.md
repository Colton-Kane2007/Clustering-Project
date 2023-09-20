--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                                                                                                      #
# **How to Sip Success: Secrets of Premium Wine **                                               
#                                                                                                                                                                      # 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## **Project Description**
###  This project emphasizes the value of data-driven decision-making in the wine industry and highlights the potential of unsupervised learning techniques, such as clustering, to enhance wine quality prediction.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## **Project Goal**
###  The main goals of the project are
  - &#9733; Construct an ML model based on clustering for wine quality prediction
  - &#9733; Identify key drivers of wine quality
  - &#9733; Enhance wine quality accuracy
  - &#9733; Provide insights into wine quality variations
  - &#9733; Deliver a comprehensive report to data science team in charge of winery supply chain marketing
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## **Initial Thoughts**
In the initial phases, our primary objectives revolve around data exploration, identifying key factors affecting wine quality, and constructing clustering-based ML models to enhance the accuracy of wine quality prediction. This foundational stage lays the groundwork for harnessing data effectively in predicting wine quality.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## **The Plan**
- &#9733; Acquire data from https://data.world/food/wine-quality
- &#9733; Prepare data that's acquired:
  -  Feature Selection/Engineering
     - &#9642; Replace spaces with underscores
     - &#9642; Create a column to show whether it is red or white wine
     - &#9642; Rename columns for visibility
     - &#9642; Split our quality category into high quality (6-10) and low quality (0-5) in order to recommend what attributes wine companies should note or change to achieve a high quality score.
- &#9733; Explore data in search of key quality drivers:
  -  Answer important questions
     - &#9642; Why do some properties have higher values than others nearby?
     - &#9642; Why do properties with similar attributes differ in value?
     - &#9642; Relationship between bathrooms, bedrooms, and property value
- &#9733; Model Selection:
  -   Choose classification algorithms
     - &#9642; KNN
     - &#9642; Decision Tree
     - &#9642; Logistic Regression
- &#9733; Data Splitting and Model Training:
  -  Divide the dataset into train and test sets
     - &#9642; Train chosen models on training dataset
- &#9733; Model Evaluation:
  -   Check the performance of models on the test dataset
  - Metrics used
     - &#9642; Accuracy
     - &#9642; R-squared (R2)
     - &#9642; R-squared (RMSE)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## **Data Dictionary**
| #   | Column            | Dtype    | Definition                                      |
| --- | ----------------- | -------  | ----------------------------------------------- |
| 1   | fixed_acidity     | float64 | Fixed acidity level of the wine                |
| 2   | volatile_acidity  | float64 | Volatile acidity level of the wine             |
| 3   | citric_acid       | float64 | Citric acid content in the wine                |
| 4   | residual_sugar    | float64 | Residual sugar content in the wine             |
| 5   | chlorides         | float64 | Chloride content in the wine                   |
| 6   | free_so2          | float64 | Free sulfur dioxide content in the wine        |
| 7   | total_so2         | float64 | Total sulfur dioxide content in the wine       |
| 8   | density           | float64 | Density of the wine                            |
| 9   | ph                | float64 | pH level of the wine                           |
| 10  | sulphates         | float64 | Sulfates content in the wine                   |
| 11  | alcohol           | float64 | Alcohol content of the wine                    |
| 12  | quality           | int64   | Quality rating of the wine (target variable)   |
| 13  | is_red            | int64   | Indicator for red wine (1 for red, 0 for white) |
| 14  | high_quality      | int64   | Indicator for high-quality wine (1 for high quality, 0 otherwise) |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## **Steps to Reproduce**
## Ordered List:
     1. Clone this repo.
     2. Create a wrangle.py and an env
     3. Acquire the data from https://data.world/food/wine-quality.
     4. Run data preprocessing and feature engineering scripts.
     5. Explore data using provided notebooks.
     6. Train and evaluate models using the provided notebook.
     7. Replicate the quality process using the provided instructions.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## **Recommendations**
## Actionable recommendations based on project's insights:
- &#9733; Optimize Alcohol Levels 
- &#9733; Monitor Volatile Acidity 
- &#9733; Refine Blending Strategies
- &#9733; Quality Testing and Validation
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## **Takeaways and Conclusions**
In conclusion, this analysis provides valuable insights into predicting quality of wine. Key drivers such as alcohol, volatile acidity, and density influence quality significantly. By implementing the recommended actions, we can confidently predict quality, and offer insights to companies in order to produce wine with a higher quality score.
It is evident that a data-driven approach to quality, considering wine attributes, will lead to more accurate assessments and ultimately empowere wine companies with data-driven decisions.
