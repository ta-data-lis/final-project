<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Title of My Project
*Ana Horta*

*Data Analytics at Ironhack Bootcmap, Lisbon, January 2020*

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
Sentiment Analysis on Tweets relating to Brexit throughout the year 2019. Identifying if there were more positive tweets refering to Theresa May or Boris Johnson and whether people became more accepting of Brexit throughout the year.

## Hypotheses / Questions
* Which prime minister made people more accepting of the prospect of the UK leaving the European Union? 

## Dataset
Built my own dataset from extracting tweets with GetOldTweets3 Library. All tweets refer to Brexit.

## Cleaning
I first dropped columns which were not relevant for my analysis and then dropped any remaining rows with null values and duplicate entries. I changed the date column type from object to datetime format and then removed all non-english tweets. I also stop checked top users with most frequent tweets and removed this from my dataset as the majority looked like fake & news accounts and did not add any meaningful value to my analysis. Adittionally, all accounts with 'brexit' in the name which displayed troll behaviour were also removed.

I then proceeded to check which tweets referred to Theresa May and Boris Johnson and added this information to a new column named 'PM'. I removed all tweets that did not mention either of the PM's as this was not meaningful to my analysis on what people were saying about the PM's within the context of Brexit. My new shape is 30,143 rows.

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
