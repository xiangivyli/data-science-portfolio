/*Step 1, Create empty tables*/

-- 1a Table professor: create a table for the professors entity type, U means User Table
-- 1a1.Every column is not null
-- 1a2.Add surrogate key as primary key
IF OBJECT_ID('professors', 'U') IS NULL
BEGIN
   CREATE TABLE professors(
     id INT IDENTITY(1,1) CONSTRAINT PK_professors PRIMARY KEY,
     firstname VARCHAR(68) NOT NULL,
     lastname VARCHAR(68) NOT NULL,
	 university_shortname CHAR(3) NOT NULL    	 
);
END

-- 1b Table universities: create a table for the universities entity type
-- 1b1.Every column is not null
-- 1b2.Set university_shortname as primary key
IF OBJECT_ID('universities', 'U') IS NULL
BEGIN
    CREATE TABLE universities (
         university_shortname CHAR(3) NOT NULL,
         university VARCHAR(20) NOT NULL,
         university_city VARCHAR(20) NOT NULL
		 CONSTRAINT PK_universities PRIMARY KEY (university_shortname)
);
END

-- 1c Table organisations: create a table for the organisation entity type
-- 1c1.Every column is not null
-- 1c2.Set organisation as primary key
IF OBJECT_ID('organisations', 'U') IS NULL
BEGIN
   CREATE TABLE organisations (
         organisation VARCHAR(256) NOT NULL,
		 organisation_sector VARCHAR(128) NOT NULL,
		 CONSTRAINT PK_organisations PRIMARY KEY (organisation)
);
END

-- 1d Table affiliations: create a table for the relationship between professors and organisations
-- 1d1. Every column is not null
IF OBJECT_ID('affiliations', 'U') IS NULL
BEGIN
    CREATE TABLE affiliations (
	     firstname VARCHAR(68) NOT NULL,
		 lastname VARCHAR(68) NOT NULL,
		 organisation VARCHAR(256) NOT NULL,
		 [function] VARCHAR(256) NOT NULL
);
END

/*Step 2, Migrate data from old table*/

-- Insert selected data (distinct)
INSERT INTO professors
SELECT DISTINCT firstname, 
                lastname, 
				university_shortname 
FROM university_professors;


INSERT INTO universities
SELECT DISTINCT university_shortname,
                university,
	            university_city
FROM university_professors;

INSERT INTO organisations
SELECT DISTINCT organization,
                organization_sector
FROM university_professors; 

INSERT INTO affiliations
SELECT DISTINCT firstname,
                lastname,
				organization,
				[function]
FROM university_professors; 

/*Step 3, Drop the old table */
--DROP TABLE university_professors;


/*Step 4, foreign key, build relationship */

-- 4a M:1 from professors to universities with university_shortname
ALTER TABLE professors
ADD CONSTRAINT fk_professors_universities FOREIGN KEY (university_shortname) 
    REFERENCES universities (university_shortname) ON DELETE NO ACTION;

-- 4b N:M relationship from professors to organisations with affiliations table

-- 4b1.Add professor_id in affiliations table
-- 4b2.1:N from professors to affiliations with professor_id
ALTER TABLE affiliations
ADD professor_id INT,
    CONSTRAINT fk_affiliations_professors FOREIGN KEY (professor_id)
	REFERENCES professors(id) ON DELETE NO ACTION;

-- 4b3.populate professor_id in affiliations
UPDATE affiliations
SET professor_id = professors.id
FROM affiliations
JOIN professors ON affiliations.firstname = professors.firstname
                AND affiliations.familyname = professors.familyname;

-- 4b4.Drop firstname and family name because there has been ids
ALTER TABLE affiliations
DROP COLUMN firstname;

ALTER TABLE affiliations
DROP COLUMN familyname;

-- 4b4.1:N from organisations to affiliations (ON DELETE NO ACTION)
ALTER TABLE affiliations
ADD CONSTRAINT fk_affiliations_orgaisations FOREIGN KEY (organisation) 
    REFERENCES organisations(organisation_id) ON DELETE NO ACTION;


/*Step 5, Check constraints with metadata (INFORMATION_SCHEMA*/

-- Identify the correct constraint name
SELECT constraint_name, table_name, constraint_type
FROM INFORMATION_SCHEMA.table_constraints
WHERE constraint_type = 'FOREIGN KEY';

-- Check the referential integrity 
DELETE FROM professors
WHERE firstname = 'Alain';
