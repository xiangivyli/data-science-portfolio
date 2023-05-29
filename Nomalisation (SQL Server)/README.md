
# Table of Content
1. [Chapter 1 - Project Overview](#chr1)
2. [Chapter 2 - Import data](#chr2)
3. [Chapter 3 - Create tables and populate them](#ch3)
4. [Chapter 4 - Set constraints and relationship](#ch4)


<a id = "ch1"></a>
## Chapter 1 Project Overview

Normalisation is a process to store data while reducing data redundancy and keeping data consistency at the same time, it follows the common 3 Normal Forms and 2 Strict Normal Forms plus the Boyce-Codd Normal Form. This project shows how to split a complete table into a database with appropriate relationships and constraints in SQL Server.

This project mainly focuses on logic and techniques.

<a id = "ch2"></a>
## Chapter 2 Import data

SQL Server 2019 Import and Export Data Wizard imported Excel table into my SQL Server Database. Then, have a look at the original table.

<p align = "center">
  <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Nomalisation%20(SQL%20Server)/Image/10.%20Original%20table.png">
  </p>
  
 It has 8 attributes:
  - firstname
  - lastname
  - university
  - university_shortname
  - university_city
  - function
  - organization
  - organization_sector

<a id = "ch3"></a>
## Chapter 3 Create tables and populate them

This database mainly records what role professors play in each organisation, a professor can have different functions in an organisation, and professors and organisations have their own dimension tables.

It has 1 fact table and 3 dimension tables
 - affiliations (fact table)
 - professors (dimension table)
 - organisations (dimension table)
 - universities (dimension table)

There are 3 things to consider when create tables
 - datatype 
 - nullable 
 - primary key

### datatype
Most attributes are varchar(), the maximum should be decided by the maximum length of the current role but should leave some space. The column university_shortname should follow the fixed format and use char(3).

### nullable
Most attributes should not be null except function attribute.

### primary key
For affiliations and professors, the primary key can be surrogate keys considering they need to combine at least two columns. For organisations and universities, the names of organisations and universities are good choices to identify each row.


**With CREATE, VARCHAR(), PRIMARY KEY, the four empty tables are created in SQL Server.**
**With INSERT INTO, SELECT DISTINCT columns FROM the original table, they are populated.**
<p align = "center">
  <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Nomalisation%20(SQL%20Server)/Image/3.%20Created%20tables.png">
  </p>













