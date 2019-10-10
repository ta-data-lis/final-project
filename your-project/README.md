<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Predict Future Sales
*[Linda Ritter]*

*[Data Squad 21, Lisbon 2019-10-11]*

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
To ensure the future growth of your business you have to make wise decisions - now. One step towards this is predict future sales, because this is the base for your business revenue, this is the base for your profability. For that I create a model to forecast the future sales in a time series.

## Hypotheses / Questions
* How many products are you going to sell in the future?
* How much of each product and of each store do you need to order for the next month?


## Dataset
kaggle | Predict Future Sales (competion, private)
 - items.csv
 - item_categories.csv
 - shops.csv
 - sales_train_v2.csv
 - test.csv

## Cleaning
I translated the shop names into english (data in russian) via googletrans. 
Afterwards I merged the different datasets to one big dataset: 
 - items.csv and item_categories.csv on item_category_id
 - items.csv and sales_train_v2.csv on item_id
 - sales_train_v2.csv and shops.csv on shop_id
 The next step was to transform the date to a Timestamp

## Analysis
* Overview the general steps you went through to analyze your data in order to test your hypothesis.
* Document each step of your data exploration and analysis.
* Include charts to demonstrate the effect of your work.
* If you used Machine Learning in your final project, describe your feature selection process.

## Model Training and Evaluation
*Include this section only if you chose to include ML in your project.*
* Describe how you trained your model, the results you obtained, and how you evaluated those results.

## Conclusion
* Summarize your results. What do they mean?
* What can you say about your hypotheses?
* Interpret your findings in terms of the questions you try to answer.

## Future Work
Address any questions you were unable to answer, or any next steps or future extensions to your project.

## Workflow
Outline the workflow you used in your project. What were the steps?
How did you test the accuracy of your analysis and/or machine learning algorithm?

## Organization
How did you organize your work? Did you use any tools like a trello or kanban board?

What does your repository look like? Explain your folder and file structure.

## Links
Include links to your repository, slides and trello/kanban board. Feel free to include any other links associated with your project.


[Repository](https://github.com/)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/en)  
