<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Predict Future Sales
*Linda Ritter*

*Data Squad 21, Lisbon 2019-10-11*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Analysis](#analysis)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
To ensure the future growth of your business you have to make wise decisions - now. One step towards this is predict future sales, because this is the base for your business revenue, this is the base for your profitability. For that I create a model to forecast the future sales in a time series.

## Hypotheses / Questions
* How many products are you going to sell in the future?
* How much of each product and of each store do you need to order for the next month?


## Dataset
kaggle | Predict Future Sales (competition, private)
 - items.csv
 - item_categories.csv
 - shops.csv
 - sales_train_v2.csv
 - test.csv

## Cleaning
* I translated the shop names into english (data in russian) via googletrans. 
* Afterwards I merged the different datasets to one big dataset: 
  - items.csv and item_categories.csv on item_category_id
  - items.csv and sales_train_v2.csv on item_id
  - sales_train_v2.csv and shops.csv on shop_id
* The next step was to transform the date to a Timestamp

## Analysis
* EDA - Exploratory Data Analysis
* Prediction Future Sales
  - Analysing historical data via seasonal decomposition -> seasonality = 12 months
  - Test Stationarity: Augmented Dicky Fuller Test -> p-value < 0.05 -> stationarity
  - Analysing different parameters (season, trend, noise) for SARIMAX to get the best AIC -> lowest AIC (115) at (1,1,1)x(1,1,0,12) for (p,d,q)
  - Diagnostic of the distribution of residuals via comparisson of normal distribution and QQ-plotting -> well distributed
* Prediction Future Sales for different shops

## Model Training and Evaluation
Based on my previous results, I choose SARIMAX for my final forecast, because the historical data shows me a seasonality of one year. The parameters season (p), trend (d) and noise (q) after iterating through all possabilities gave me the best AIC (115) at (1,1,1)x(1,1,0,12). Stationarity was confirmed by the ADF Test.

## Conclusion
The prediction of future sales for all sold products is very good, the distribution is in the beginning very low and increase with more predicted months. But the results for the forecast for one month - which was required - is very good. To predict future sales more correctly for months in one to two years, I need more data. 

## Future Work
Unfortunatley cased by processing power of my laptop, I wasn´t able to predict the order list for future sales for each product and each shop. I already prepared my data with further features e.g. lag_features and tried the LinearRegression model but my accuracy score stopped at 24%. After trying a different model XGBoost with feeding my prepared data my Laptop crashed.

## Workflow
Outline the workflow you used in your project. What were the steps?
How did you test the accuracy of your analysis and/or machine learning algorithm?

## Organization
I used Trello.

* All .csv files are raw data. 
* The .pgn files are plots which I used in my presentation
* Predict Future Sales - Time Series.ipyng is the code for the time series and contains basicly all the steps I mentioned above
* Predict Future Sales - SL ML.ipyng is the attempt to predict the order list, based on supevised machine learning with the regression model

## Links
Include links to your repository, slides and trello/kanban board. Feel free to include any other links associated with your project.


[Repository](https://github.com/)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/en)  
