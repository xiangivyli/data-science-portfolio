<p align = "center">
<img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Lloyds%20Bank%20Customer%20Profiling%20and%20Predictive%20Model%20(BI%20%26%20Logistic%20Regression)/Images/Lloyds_Banking_Group_logo.png">
</p>



# Table of Contents
1. [Chapter 1 - Challenge Overview](#ch1)
2. [Chapter 2 - Data Strategy](#ch2)


<a id = "ch1"></a>
## Chapter 1 Challenge Overview
Lloyds Banking Group is launching a new loans product. Prior to the launch I can use historical customer data to:
 - **Task 1 Data Stategy**: Understand and summarise the different behaviours or attributes between customers who paid back their loan and customers who did not
 - **Task 2 Data Science**: To use the historical data to design a process which predicts the likelihood of a new customer not paying back their loan

### Dataset
The dataset and corresponding dictionary can be found in the Data folder. 
Note: the dataset is based on the American credit risk problem.
The dataset contains 18,324 customers with 31 columns who: 
 - Previously held a loan
 - The status of that loan - did the customer pay back the loan or not:
     - Customers who paid back are categorised as 'Fully Paid'
     - Customers who did not pay back their loan are categorised as 'Charged-off'
 - Other credit and product information that can be used to understand a customer's credit or financial behaviour, like:
     - emp_length: employment length in years
     - home_ownership: RENT, OWN, MORTGAGE, OTHER
     - purpose: a category provided by the borrower for the loan request
     - etc.
 
 
 <a id = "ch2"></a>
 ## Chapter 2 Data Strategy
 ### Methodology
 This chapter use Power BI to depict features of customers, like the geographical features, the current distribution of loan status, the distribution of purposes, then explore the relationship between loan status and employment length, income and home ownership.
 Note: the analysis adds a small dataset including U.S. state and territory two-letter abbreviation corresponding full name.
 
 ### Dashboard
 
 <p align = "center">
<img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Lloyds%20Bank%20Customer%20Profiling%20and%20Predictive%20Model%20(BI%20%26%20Logistic%20Regression)/Images/Lloyds%20Bank%20Customer%20Cover%20Photo.png">
</p>

### Insights
 
 - The total loan is 176 million dollars.
 - 14418 customers have paid back while 3906 have not.
 - The customers who borrow loans mainly live on the east coast of the U.S.
 - Income increases with employee length, and the higher income group is likely to pay back.
 - Customers who rent their home struggle to pay back.
 - More than half of customers apply for a loan to consolidate debt; the 2nd purpose is to support credit cards.
