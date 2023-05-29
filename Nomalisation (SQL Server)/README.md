
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

