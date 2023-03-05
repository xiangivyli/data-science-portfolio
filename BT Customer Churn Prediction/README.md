<p align = "center">
<img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/BT%20Customer%20Churn%20Prediction/Image/BT%20Logo.jpg">
</p>


# Table of Contents
1. [Chapter 1 - Project Overview](#ch1)
2. [Chapter 2 - Data Validation](#ch2)

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


