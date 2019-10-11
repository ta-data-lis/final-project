<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Drug Review Dataset (Drugs.com) 
*[Laura Würz]*

*[Datasquad 21, Lisbon & October 2019]*

## Content
- [Project Description](#project-description)
- [Questions](#hypotheses-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Analysis](#analysis)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
The dataset provides patient reviews on specific drugs along with related conditions and a 10 star patient rating reflecting overall patient satisfaction. The data was obtained by crawling online pharmaceutical review sites. The intention was to study whether ratings depend on the condition the consumer suffered from and to conduct a sentiment analysis to compare whether reviews and ratings differ from each other. 

## Questions
* 1. Do ratings given depend on the condition suffered from?
* 2. Do ratings and reviews differ from another?  


## Dataset
* The dataset was downloaded from UCI Machine Learning Repository via Kaggle. 
* Dataset description:
    * Size: 215063 entries
    * Features: 6
        * Attribute Information:
        1. drugName (categorical): name of drug
        2. condition (categorical): name of condition
        3. review (text): patient review
        4. rating (numerical): 10 star patient rating
        5. date (date): date of review entry
        6. usefulCount (numerical): number of users who found review useful

## Cleaning
* concatenating train and test set
* > 1000 entries did not have information on the condition. Since condition is an important attribute in our analysis, these entries were dropped.
* > 85 420 entries duplicated and had to be removed.
* > 127 000 entries were left for conducting the analysis


## Analysis
* Exploratory Analysis: explore and visualize the data in order to get a general understanding of the data
* ANOVA Analysis to answer Question 1: Between groups (conditions) - do ratings differ significantly?
* Sentiment Analysis: 1. Clean/Process Text using spacy and nlkt, 2. Conduct Sentiment Analysis using TextBlob


## Conclusion
* Question 1: Rating scores depend on the condition the consumer is suffering from
* Question 2: Rating scores and Reviews do not match each other - Ratings subjective


## Future Work
Future Research can access questions such as whether other features such as the price of drugs have an impact on the rating score.

## Workflow
Outline the workflow you used in your project. What were the steps?

* I started by preparing my data for the analysis and then inspected the data during the Exploratory analysis. 
* I then conducted a sentiment analysis and compared ratings and review outcomes of the sentiment analysis. 
* During the process I constantly updated my presentation.


## Organization
The project was organized using TRELLO.

What does your repository look like? Explain your folder and file structure.

## Links
Link UCI: https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29
Link Kaggle Kernel: https://www.kaggle.com/lauriandwu/drug-review/
Link TRELLO: https://trello.com/b/Z1nJfnn5/final-project
Link Github: https://github.com/laurawuerz/final-project


