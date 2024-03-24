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

Potential audience:
 - Researchers (bioinformatics scientists, surgeon, oncologists, etc)
 - Managers in NHS
 - Public
 - Funding Organisations
 - Government Health Sectors

Potential stakeholders
 - IT (database establishment and maintenance)
 - Public (disease trend)
 - Researchers (needed data)

<a id = "ch2"></a>
## Chapter 2 Design of Schema
### Step 1: Initial mindmap 
Tables in schema are divided into two parts:
 - Clinical data
 - Genetic data
<p align = "center">
  <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Data%20Platform%20Design%20for%20Healthcare%20Research%20(Database)/Image/Schema%20mindmap.png">
            </p>
            
As the mindmap shows, clinical data comes from NHS and genetic data comes from genetic detection organisation. The clinical data involves patient general information, and admission and treatment reccords. The genetic data involves detailed mutated genes and frequency and other parameters.

### Step 2: Use [drawSQL](https://drawsql.app/) to map it
8 Tables for clinical data:
 - Patient
 - Primary care
 - City
 - Country
 - Admission record
 - Treatment
 - Medication
 - Surgery

4 Tables for genetic data:
 - Sample
 - Detection Organisation
 - Genetic Info
 - Gene

<p align = "center">
  <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Data%20Platform%20Design%20for%20Healthcare%20Research%20(Database)/Image/Schema%20design.png">
  </p>

### Step 3: Import SQL into MySQL
I use drawSQL to generate [SQL queries](https://github.com/xiangivyli/data-science-portfolio/blob/main/part_a_database_design_healthcare_research/dataplatform_for_healthcare_research.sql), and then use MySQL to run it.

<a id = "ch3"></a>
## Chapter 3 Data Privacy and Security
The preparation of the database has finished, before populating the database, it is essential to talk about etical considerations as the data is connected to patient privacy. Patients may suffer potential harm when their data is used for research purposes like revealing sensitive information. NHS currently has [information governance](https://www.england.nhs.uk/ig/about/) which protects patients. "Secondary use" must only use data that will not identify individuals.

The pre-requisite includes:
 - Obtain the appropriate consent from patients
 - de-indentify the data to protect patient privacy
 - ensure data is only used for approved purposes

Relevant technology includes:
 - Data anonymisation
 - Data encryption
 - Data access control
 - Data masking
 - so on

<a id = "ch4"></a>
## Chapter 4 Extract, Transform, and Load (ETL)
The data comes from two sources: Electronic Health Records (EHRs) and genetic detection organisations. 
There are several steps to do it:
 - obtain **permission** from administrators and patients
 - establish the **relationships** between EHR and the database (needed data)
 - **extract** data from EHRs (APIs, SQL)
 - **transform**: revise the message formats and map coding systems (Apache Spark)
 - **load**: import data and ensure the data is complete and accurate 

<a id = "ch5"></a>
## Chapter 5 Monitor and Maintain
When data is generated with time and simulated in the database, the ETL process should be implemented periodically.
**Set up scheduled ingestion of data from the EHR databases to an analytical database (Airflow)**
 - at the correct time
 - with a specific interval
 - in the right order

<a id = "ch6"></a>
## Chapter 6 Future Work
Coming back to the original purposes, the database is for healthcare researchers, considering the security and management of the database, maybe it is a good idea to set a separate database for data analysis or views in MySQL for researchers.

Last but not least, the update for the database is an iterated process. Getting feedback from researchers or NHS managers, adding or deleting columns will be followed in the future.

The slides I presented [here](https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Data%20Platform%20Design%20for%20Healthcare%20Research%20(Database)/0317Data%20Platform%20Design%20for%20healthcare%20research.pptx). Feel free to comment it. 

