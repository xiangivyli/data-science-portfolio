<p align = "center">
  <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Data%20Platform%20Design%20for%20Healthcare%20Research%20(Database)/Image/EER%20Diagram%20MySQL.png">
  </p>

# Table of Content
1. [Chapter 1 - Project Overview](#chr1)
2. [Chapter 2 - Design of Schema](#chr2)
3. [Chapter 3 - Data Privacy and Security](#chr3)
4. [Chapter 4 - Extract, Transform, and Load (ETL)](#chr4)
5. [Chapter 5 - Monitor and Maintain](#chr5)
6. [Chapter 6 - Future Work](#chr6)


<a id = "ch1"></a>
## Chapter 1 Project Overview
The project is inspired by a data engineer job description posted by Our Future Health, to identify how diseases begin and progress in people from different backgrounds. They would like to harness genetic and clinical data to create a more detailed picture of people’s health. 

MySQL is a relational database which stores structured data (each row represents one record with different features), it can create several tables with relationships that connect them together, and the purpose of storing data is to reduce duplicate data and retrieve data conveniently.

There are several objectives:
 - integration of genetics and healthcare data
 - easily monitor and maintain in the future work
 - predicted outcome: research-ready, well-curated and well-documentaed data

<a id = "ch2"></a>
## Chapter 2 Design of Schema
Tables in schema are divided into two parts:
 - Clinical data
 - Genetic data
<p align = "center">
  <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Data%20Platform%20Design%20for%20Healthcare%20Research%20(Database)/Image/Schema%20mindmap.png">
            </p>
            
As the mindmap shows, clinical data comes from NHS and genetic data comes genetic detection organisation. The clinical data involves patient general information, and admission and treatment reccords. The genetic data involves detailed mutated genes and frequency and other parameters.
