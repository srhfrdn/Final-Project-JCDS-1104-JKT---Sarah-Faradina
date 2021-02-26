# **Final Project - Airline Passenger Satisfaction**

## **About The Project:** 

Predicting Airline Passenger Satisfaction Project is a machine learning classification project that will try to predict whether the future passengers would be satisfied or neutral/dissatisfied with service using machine learning based on historical data.

Dataset for this project was taken from Kaggle [US Airline Passenger](https://www.kaggle.com/johndddddd/customer-satisfaction). The data shows whether a passenger is satisfied with the airlines or not after travelling with them. There are several other measurement or to say feedback taken from the customers as well as their demographic data is also recorded.

![Airplane](/Visualization/airplane_gif.gif)

## **Goals:**

**1.** The Goals of this project is Predicts whether the future passengers would be satisfied or neutral/dissatisfied with service. 

**2.** To know on which airline aspect of the services offered by them have to be emphasized more to generate more satisfied passengers.


## **Workflow:**

### **Data Cleaning :** 
  - Imputing missing value with median using median instead of mean here because there are many outliers in the dataset : Arrival Delay in Minutes
  - **Dropping columns** 
    - ID : that don't seem contain any important information for our purpose
    - Flight Distance :  low correlation, many outliers, and its not important based on basic knowledge
      
 ### **Exploratory Data Analysis :** 
  - Feature Engineering 
  - Aggregating Columns
  - Visualization
  - Insight & Conclusion
  
 ### **Machine learning process**
  - Train Test Split
  - Using pipeline for model building 
    - simpleimputer with median for missing values
    - scaling using Robust Scaler for numerical features
    - one hot and ordinal encoder for categorical features
  - Creating base model with few algorithm *(Decision Tree Classifier, K Neighbors Classifier, Random Forest classifier)*
  - Checking evaluation matrix
  - Hyperparameter with Random SearchCV tuning on all algorithm
  - checking evaluation matrix on the tuned model
  - Export the model with the best accuracy score

 ### **Recall Score Before & After Hyperparameter Tuning**

  |           |  Before  | After |
  |:-|:-:|:-:|
  | Decision Tree | 0.881453 | 0.925589 |
  | KNN Classifier | 0.924058 | 0.918360|
  | Random Forest | 0.838507 | 0.874224 |
    

  Based on Recall Score, the best model is Decision Tree Classifier After Tuned.

## **Conclusion:**
- The airline can identify the potential satisfied or dissatisfied passenger by using model (Decision Tree Classifier with hyperparameter Tuning ) if the airline do satisfaction survey and the passenger fill out the survey well.
- After do some analysis, the worst aspect each category are:
  - Service before flight : Ease of Online booking and Online boarding services
  - Service inflight : Food and drink
  - Facilities : Seat comfort
There may be a problem with these services, so these should be considered and improved.



## **Dashboard Building Using Flask:**

- **Home**

![Home](/Dashboard/resultdash/1_dashboard.png)

- **Predict**

![Predict](/Dashboard/resultdash/2_predict.png)

- **Result**

![Result](/Dashboard/resultdash/3_result.png)

- **Visualization**
  - visual 1
![Visualization1](/Dashboard/resultdash/4a_visual.png)

  - visual 2
![Visualization2](/Dashboard/resultdash/4b_visual.png)

  - visual 3
![Visualization3](/Dashboard/resultdash/4c_visual.png)

  - **etc**
  
- **Author**

![Author](/Dashboard/resultdash/5_author.png)

## **Thank you for reading.**



