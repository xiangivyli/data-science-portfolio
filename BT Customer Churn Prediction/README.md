<p align = "center">
<img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/BT%20Customer%20Churn%20Prediction/Image/BT%20Logo.jpg">
</p>


# Table of Contents
1. [Chapter 1 - Project Overview](#ch1)
2. [Chapter 2 - Data Validation](#ch2)
3. [Chapter 3 - Logistic Regression](#ch3)
4. [Chapter 4 - Feature Importance](#ch4)

<a id = "ch1"></a>
## Chapter 1 Project Overview
The event is that Dig Data cooperated with BT Group to provide an opportunity to experience the "real world" business problem. Logistic regression is popular in business environment as there are many binary values (is spam email or not, cancel contract or not, promotion or not and so on). In this project, I am going to use logistic regression model to predict customer churn and identify the key features.

### Background Information
BT group is investigating why some customers stop using BT services (churn), including:
- Build a model that predicts which customers are highly likely to leave 
- Interpret the model to understand what influences the customers' decision to leave
- Make recommendations to the business:
  - How to engage the customers to stay with BT?
  - How to retain more customers?


<a id = "ch2"></a>
## Chapter 2 Data Validation
BT provided 7,043 rows (customers) and 21 columns (features). The "Churn" columns is the target, showing whether the customer left the company (Churn = 'Yes') or not (Churn = 'No').
<p align = "center">
<img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/BT%20Customer%20Churn%20Prediction/Image/Data%20Snapshot.jpg">
</p>
The dataset includes information about:

- Customers who left within the last month - the column is called Churn
- Services that each customer has signed up for - phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
- Customer account information - how long they've been a customer, contract, payment method, paperless billing, monthly charges, and total charges
- Demographic info about customers - gender, if they have partners and dependents

You can find the dataset and dictionary on my [GitHub](https://github.com/xiangivyli/Data-Science-Porfolio/tree/main/BT%20Customer%20Churn%20Prediction/Data)

Steps to adjust dataset:

- delete customerID, the feature is unuseful
- delete null values, TotalCharges column has missing values
- adjust datatype, TotalCharges should be numeric rather than object
- merge some categories, InternetService has 'No' and 'No internet service', they should be merged together, others do the same

Steps to adjust dataset for preparing model:

- convert 'yes' to 1, 'no' to 0
- convert 'Female' to 1, 'male' to 0
- generate dummy variables for categorical feature ('InternetService', 'Contract', 'PaymentMethod')
- scaling continuous values to avoid bias ('tenure', 'MonthlyCharges', 'TotalCharges')

After the data validation and preparation, the dataset contains **7,032 rows and 27 columns** without missing data.

<a id = "ch3"></a>
## Chapter 3 Logistic Regression

Step 1 split data: split dataset into training dataset and test dataset, I use 8:2 ratio to split it.
Step 2 modelling: define a function in which generate the model and calculate confusion matrix, accuracy, f1-score, coefficients and corresponding probability.

The result is AUC=0.85

<p align = "center">
<img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/BT%20Customer%20Churn%20Prediction/Image/ROC.png">
</p>

### SMOTE Optimisation

As the number of 0 value is much less than 1 value in our dataset (imbalanced), the accuracy is not able to reflect if the model is good. Therefore, I used Synthetic Minority Over-sampling Technique (SMOTE) to oversampling the 0 value to make the number of 0 value equal to another one.

The optimised result is AUC=0.86
<p align = "center">
<img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/BT%20Customer%20Churn%20Prediction/Image/ROC-SMOTE.png">
</p>


<a id = "ch4"></a>
## Chapter 4 Feature Importance

The purpose of this project is to identify key features, I extracted coefficients for each feature and mapped them in a bar plot.

<p aligh = "center'>
            <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/BT%20Customer%20Churn%20Prediction/Image/Coefficients.png">
                                                                                                                                              </p>
