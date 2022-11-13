<p align = "center">
<img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Revenue%20increase%20strategy%20analysis%20for%20Google%20merchandise%20store%20(BI)/Images/Google%20Merchandise%20Store.png">
</p>


# Table of Content
1. [Chapter 1 - Project Overview](#ch1)
2. [Chapter 2 - Web Metrics](#ch2)
3. [Chapter 3 - Persona of customers](#ch3)
4. [Chapter 4 - The performance of products](#ch4)



<a id = "ch1"></a>
## Chapter 1 Project Overview
### Background Information
Google merchandise store is an online platform that sells google-branded products. The Google Analytics platform (a web analytics tool that stores historical marketing data and tracks the customer's real-time status) shows that in December 2017 and April 2018, the sales performance reached the highest peak – $578,246 and $585,960. But after June 2018, the trend showed a considerable decline until the lowest point ($3,269 in November 2018). The significant decrease should be that the European Commission took a hard line on antitrust behaviour and fined Google €2.42 billion in June 2017 and €4.34 billion in July 2018, respectively (European Commission, 2017, 2018). The situation lasted for two years, and the revenue started to increase in December 2020, but the peak value was much lower than before. To help the Google merchandise store recreate its historical prospects, this report uses the google analytics platform to define customers' personas and provide feasible strategies to increase revenue.

### Dataset
Data comes from Demo Account (54516992) – UA – Google Merchandise Store (UA-54516992-1) - 1 Master View (92320289). 

The time range is the first quarter in 2022; the objective of comparison in the first quarter (from January 1 to March 31) in 2021, considering seasonality may influence the performance, although there are still many uncontrollable factors like pandemics (Ehrenthal et al., 2014).

### Detailed questions
1. What is the persona (an overview of customers in marketing) of customers, and what are the characteristics of target customers? 
2. What are the most popular products? How profitable are products?
3. What are customers’ shopping habits?
4. What are the differences between new users and returning users? 
5. What happened during the whole shopping journey? Which stages do most consumers leave before payment?

<a id = "ch2"></a>
## Chapter 2 Web Metrics
### The percentage of conversions
Understanding consumers’ activities are the first step for web analysis. As figure 1 shows, total visitors represent visitors who have entered the website; potential conversions mean visitors are likely to shop for products. Most visitors leave the website without further exploration, which are bounded visits; the left visitors may add items to carts, but only 1 – 3 % of total visitors will pay for products. This small part can be counted as conversions.

<p align = "center">
  <image src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Revenue%20increase%20strategy%20analysis%20for%20Google%20merchandise%20store%20(BI)/Images/1.The_classification_of_web_users.png" width = 400>
</p>   

### Objectives and key results (OKRs)
 To achieve the increasing revenue goal, data analysis focused on five objectives and key results (OKRs) to answer five questions mentioned in the introduction: 
1. Identify what group of customers purchase more and depict the demographic features of customers. 
2. Identify the most popular or profitable products and find the features of top-selling products. 
3. Identify the pattern of activity of customers, such as the length of durations, used devices, and channels. 
4. Explore the different performance patterns between new users and returning users.
5. Identify barriers during online activities, such as the stages where visitors are likely to give up making payments.  
Each OKR needs corresponding key performance indicators (KPIs). Table 1 shows what KPIs are measured and the definitions of KPIs.

 <p align = "center">
   <image src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Revenue%20increase%20strategy%20analysis%20for%20Google%20merchandise%20store%20(BI)/Images/2.OKRs_and_KPIs.png" width = 400>
 </p>
   
### Hypotheses
Five hypotheses are listed below to solve five questions and achieve five OKRs.
1. A specific group (maybe young women in the United States) has shown strong intentions to purchase Google-branded products.
2. Clothes with the Google brand logo attract most consumers considering their practicability.
3. Consumers often use mobile phones to complete a purchase.
4. Returning users contribute more to the revenue.
5. Consumers often leave after they have added products to their carts.
   
<a id = "ch3"></a>
## Chapter 3 Persona of customers
The first analysis depicts the current customer; a persona can form a coherent picture of consumers with better clarity and completeness (Sinha, 2003; Spiliotopoulos et al., 2020). Table 2 indicates that the United States has contributed the most users and revenue; the interesting point is that India has the second most users, but the payment is not high enough. 

Figure 2 below illustrates that the 18-24 and 25-34 groups use google merchandise store more, and the male uses the online store slightly more frequently than females. Men purchase more than women in the store violates the public consensus that women drive most of total purchasing (Nelson, 2020). It may be caused by the attraction of the Google brand for men. The first hypothesis should be changed because young men intend to purchase Google-branded products more. It is worth noting that the demographic data are only available for about half of the total users (the right corner of the graphs has annotated the number). 

<p align = "center">
  <image src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Revenue%20increase%20strategy%20analysis%20for%20Google%20merchandise%20store%20(BI)/Images/3.Country_distribution_for_users_and_revenue.png" width = 400>
    </p>

<a id = "ch4"></a>
## Chapter 4 The performance of products
The product performance reflects customers’ mindsets or insights (Charm, 2020). Table 3 below presents the six most famous products: hoodies, T-shirts, jackets, polo, and backpack. From the data, it is easy to see that 5/6 belongs to clothing and one in the backpack, and the price did not change a lot, but the quantity has added a lot. For example, the sales volumes of Google Black Cloud Zip Hoodie and Google Unisex Eco Tee Black products have over doubled compared to the same quarter last year, and there are two new items which did not come into markets in the first quarter of 2021 have become popular too, they are both jackets. The ranking of popular products shows that consumers may pursue practical fashion and brand satisfaction simultaneously and supports the second hypothesis.

<p align = "center">
  <image src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Revenue%20increase%20strategy%20analysis%20for%20Google%20merchandise%20store%20(BI)/Images/4.The_performance_of_products.png" width = 400>
    </p>

   
   
 
