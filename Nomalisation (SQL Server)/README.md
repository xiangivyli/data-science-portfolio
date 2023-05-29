
# Table of Content
1. [Chapter 1 - Project Overview](#chr1)
2. [Chapter 2 - Import data](#chr2)
3. [Chapter 3 - Create tables and populate them](#ch3)
4. [Chapter 4 - Set constraints and relationship](#ch4)
5. [Chapter 5 - Final two tips](#ch5)


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

<a id = "ch4"></a>
## Chapter 4 Set constraints and relationships

The final relationships should be 
 - M:1 relationship from professors to universities with university_shortname column
 - N:M relationship from professors to organisations with affiliations table
   - 1:N relationship from professors to affiliations with professor_id column
   - 1:M relationship from organisations to affiliations with orgnaisation column

The key part of this chapter is to talk about how to achieve the connection between organisations and professors with affiliations. Because a professor can have many functions in an organisation while an organisation can have many professors, there is a many-to-many relationship. A method is to use an intermediate table to become the bridge.

### Step 1 Add a professor_id as the foreign key from professors to affiliations for convenience 
```ruby
ALTER TABLE affiliations
ADD professor_id INT,
    CONSTRAINT fk_affiliations_professors FOREIGN KEY (professor_id)
	REFERENCES professors(id) ON DELETE NO ACTION;
```
<p align = "center">
  <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Nomalisation%20(SQL%20Server)/Image/5.%20Add%20professor%20id.png">
  </p>
  
### Step 2 Populate professor_id using professors table
```ruby
UPDATE affiliations
SET professor_id = professors.id
FROM affiliations
JOIN professors ON affiliations.firstname = professors.firstname
                AND affiliations.lastname = professors.lastname;
```
<p align = "center">
  <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Nomalisation%20(SQL%20Server)/Image/6.%20Populate%20affiliations.png">
  </p>


### Step 3 Drop firstname and lastname 
```ruby
ALTER TABLE affiliations
DROP COLUMN firstname;

ALTER TABLE affiliations
DROP COLUMN lastname;
```
### Step 4 1:M relationship from organisations to affiliations
```ruby
ALTER TABLE affiliations
ADD CONSTRAINT fk_affiliations_organisations FOREIGN KEY (organisation) 
    REFERENCES organisations(organisation) ON DELETE NO ACTION;
```

**The final diagram** shows the complete database
<p align = "center">
  <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Nomalisation%20(SQL%20Server)/Image/9.%20Final%20diagram.png">
  </p>

<a id = "ch5"></a>
## Chapter 5 Final Two tips

### Tip 1 Referential Integrity: ON DELETE NO ACTION
To keep data consistency, there are some options for referenced table when a row is deleted. The project chose NO ACTION, it prevents the deletion of rows if it is referenced.
Test it with 
```ruby
DELETE FROM professors
WHERE firstname = 'Alain';
```
And the error is 
<p align = "center">
  <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Nomalisation%20(SQL%20Server)/Image/8.%20Referential%20Intergrity.png">
  </p>

### Tip 2 INFORMATION_SCHEMA
The INFORMATION_SCHEMA can check tables, columns, constraints and other metadata.
```ruby
SELECT constraint_name, table_name, constraint_type
FROM INFORMATION_SCHEMA.table_constraints;
```
The constraints will be extracted in a table, super convenient, right?
<p align = "center">
  <img src="https://github.com/xiangivyli/Data-Science-Porfolio/blob/main/Nomalisation%20(SQL%20Server)/Image/7.%20Constraints.png">
  </p>






