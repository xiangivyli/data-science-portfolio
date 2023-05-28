/*Step 1, Create empty tables*/

-- 1a Table professor: create a table for the professors entity type, U means User Table
IF OBJECT_ID('professors', 'U') IS NULL
BEGIN
   CREATE TABLE professors(
     firstname VARCHAR(68) NOT NULL,
     lastname VARCHAR(68) NOT NULL,
	 university_shortname CHAR(3) NOT NULL
);
END

--	1b Table universities: create a table for the universities entity type
IF OBJECT_ID('universities', 'U') IS NULL
BEGIN
    CREATE TABLE universities (
         university_shortname CHAR(3) NOT NULL,
         university VARCHAR(20) NOT NULL,
         university_city VARCHAR(20) NOT NULL
);
END

-- 1c Table affiliations: create a table for the relationship between professors and organisations
IF OBJECT_ID('affiliations', 'U') IS NULL
BEGIN
    CREATE TABLE affiliations (
	     firstname VARCHAR(68) NOT NULL,
		 lastname VARCHAR(68) NOT NULL,
		 organisation VARCHAR(256) NOT NULL,
		 [function] VARCHAR(256) NOT NULL
);
END

-- 1d Table organisations: create a table for the organisation entity type
IF OBJECT_ID('organisations', 'U') IS NULL
BEGIN
   CREATE TABLE organisations (
         organisation VARCHAR(256) NOT NULL,
		 organisation_sector VARCHAR(128) NOT NULL
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