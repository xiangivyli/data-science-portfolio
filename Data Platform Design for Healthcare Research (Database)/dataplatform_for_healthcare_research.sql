CREATE TABLE `Gene`(
    `gene_id` SMALLINT NOT NULL,
    `chromosome` VARCHAR(20) NOT NULL,
    `last_update` TIMESTAMP NOT NULL
);
ALTER TABLE
    `Gene` ADD PRIMARY KEY `gene_gene_id_primary`(`gene_id`);
CREATE TABLE `Treatment`(
    `treatment_id` VARCHAR(20) NOT NULL,
    `admission_id` VARCHAR(20) NOT NULL,
    `treatment_datetime` DATETIME NOT NULL,
    `ICD_10` VARCHAR(20) NOT NULL,
    `SNOMED` VARCHAR(20) NOT NULL,
    `outcome` VARCHAR(20) NOT NULL
);
ALTER TABLE
    `Treatment` ADD PRIMARY KEY `treatment_treatment_id_primary`(`treatment_id`);
CREATE TABLE `Admission_record`(
    `admission_id` VARCHAR(20) NOT NULL,
    `admission_date` DATE NOT NULL,
    `gp_id` VARCHAR(20) NOT NULL,
    `patient_id` VARCHAR(20) NOT NULL,
    `discharge_date` DATE NOT NULL
);
ALTER TABLE
    `Admission_record` ADD PRIMARY KEY `admission_record_admission_id_primary`(`admission_id`);
CREATE TABLE `Detection_Organisation`(
    `organisation_id` VARCHAR(20) NOT NULL,
    `name` VARCHAR(40) NOT NULL,
    `postal_code` VARCHAR(20) NOT NULL,
    `address` VARCHAR(40) NOT NULL,
    `city_id` SMALLINT NOT NULL,
    `phone` VARCHAR(20) NOT NULL,
    `last_update` TIMESTAMP NOT NULL
);
ALTER TABLE
    `Detection_Organisation` ADD PRIMARY KEY `detection_organisation_organisation_id_primary`(`organisation_id`);
CREATE TABLE `Patient`(
    `patient_id` VARCHAR(20) NOT NULL,
    `first_name` VARCHAR(40) NOT NULL,
    `middle_name` VARCHAR(40) NULL,
    `last_name` VARCHAR(40) NOT NULL,
    `age` SMALLINT NOT NULL,
    `gender` ENUM('') NOT NULL,
    `date_of_birth` DATE NOT NULL,
    `ethnicity` ENUM('') NOT NULL,
    `country_of_origin` ENUM('') NOT NULL,
    `consent_given` TINYINT(1) NOT NULL,
    `smoking_history` VARCHAR(40) NOT NULL,
    `drinking_history` VARCHAR(40) NOT NULL,
    `family_history` VARCHAR(40) NOT NULL,
    `drug_food_allergy` VARCHAR(40) NOT NULL,
    `marital_history` VARCHAR(40) NOT NULL,
    `menstrual_history` VARCHAR(40) NOT NULL
);
ALTER TABLE
    `Patient` ADD PRIMARY KEY `patient_patient_id_primary`(`patient_id`);
CREATE TABLE `Genetic_Info`(
    `gene_id` SMALLINT NOT NULL,
    `sample_id` VARCHAR(20) NOT NULL,
    `mutation_type` ENUM('') NOT NULL,
    `mutation_location` VARCHAR(100) NOT NULL,
    `mutation_frequency` DOUBLE(8, 2) NOT NULL
);
ALTER TABLE
    `Genetic_Info` ADD PRIMARY KEY `genetic_info_gene_id_primary`(`gene_id`);
CREATE TABLE `Medication`(
    `medication_id` VARCHAR(20) NOT NULL,
    `treatment_id` VARCHAR(20) NOT NULL,
    `medication_name` VARCHAR(255) NOT NULL,
    `dosage` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `Medication` ADD PRIMARY KEY `medication_medication_id_primary`(`medication_id`);
CREATE TABLE `Country`(
    `country_id` SMALLINT NOT NULL,
    `country` VARCHAR(40) NOT NULL,
    `last_update` TIMESTAMP NOT NULL
);
ALTER TABLE
    `Country` ADD PRIMARY KEY `country_country_id_primary`(`country_id`);
CREATE TABLE `Primary_Care`(
    `gp_id` VARCHAR(20) NOT NULL,
    `postal_code` VARCHAR(20) NOT NULL,
    `address` VARCHAR(40) NOT NULL,
    `city_id` SMALLINT NOT NULL,
    `phone` VARCHAR(20) NOT NULL,
    `last_update` TIMESTAMP NOT NULL
);
ALTER TABLE
    `Primary_Care` ADD PRIMARY KEY `primary_care_gp_id_primary`(`gp_id`);
CREATE TABLE `Sample`(
    `sample_id` VARCHAR(20) NOT NULL,
    `treatment_id` VARCHAR(20) NOT NULL,
    `organisation_id` VARCHAR(20) NOT NULL,
    `detection_method` ENUM('') NOT NULL,
    `sampling_site` VARCHAR(40) NOT NULL,
    `sampling_type` ENUM('') NOT NULL,
    `datetime_of_detection` DATETIME NOT NULL,
    `Informed_consent` TINYINT(1) NOT NULL
);
ALTER TABLE
    `Sample` ADD PRIMARY KEY `sample_sample_id_primary`(`sample_id`);
CREATE TABLE `City`(
    `city_id` SMALLINT NOT NULL,
    `city` VARCHAR(40) NOT NULL,
    `country_id` SMALLINT NOT NULL,
    `last_update` TIMESTAMP NOT NULL
);
ALTER TABLE
    `City` ADD PRIMARY KEY `city_city_id_primary`(`city_id`);
CREATE TABLE `Surgery`(
    `surgery_id` VARCHAR(20) NOT NULL,
    `surgeon_id` VARCHAR(20) NOT NULL,
    `surgery_datetime` DATETIME NOT NULL,
    `procedure` VARCHAR(200) NOT NULL,
    `anesthesia` VARCHAR(200) NULL,
    `duration` SMALLINT NOT NULL,
    `complication` VARCHAR(200) NOT NULL,
    `follow_up_care` VARCHAR(200) NOT NULL
);
ALTER TABLE
    `Surgery` ADD PRIMARY KEY `surgery_surgery_id_primary`(`surgery_id`);
ALTER TABLE
    `Medication` ADD CONSTRAINT `medication_treatment_id_foreign` FOREIGN KEY(`treatment_id`) REFERENCES `Treatment`(`treatment_id`);
ALTER TABLE
    `Admission_record` ADD CONSTRAINT `admission_record_gp_id_foreign` FOREIGN KEY(`gp_id`) REFERENCES `Primary_Care`(`gp_id`);
ALTER TABLE
    `Genetic_Info` ADD CONSTRAINT `genetic_info_gene_id_foreign` FOREIGN KEY(`gene_id`) REFERENCES `Gene`(`gene_id`);
ALTER TABLE
    `Admission_record` ADD CONSTRAINT `admission_record_patient_id_foreign` FOREIGN KEY(`patient_id`) REFERENCES `Patient`(`patient_id`);
ALTER TABLE
    `Sample` ADD CONSTRAINT `sample_treatment_id_foreign` FOREIGN KEY(`treatment_id`) REFERENCES `Treatment`(`treatment_id`);
ALTER TABLE
    `Primary_Care` ADD CONSTRAINT `primary_care_city_id_foreign` FOREIGN KEY(`city_id`) REFERENCES `City`(`city_id`);
ALTER TABLE
    `Sample` ADD CONSTRAINT `sample_organisation_id_foreign` FOREIGN KEY(`organisation_id`) REFERENCES `Detection_Organisation`(`organisation_id`);
ALTER TABLE
    `Treatment` ADD CONSTRAINT `treatment_treatment_id_foreign` FOREIGN KEY(`treatment_id`) REFERENCES `Surgery`(`surgery_id`);
ALTER TABLE
    `Genetic_Info` ADD CONSTRAINT `genetic_info_sample_id_foreign` FOREIGN KEY(`sample_id`) REFERENCES `Sample`(`sample_id`);
ALTER TABLE
    `City` ADD CONSTRAINT `city_country_id_foreign` FOREIGN KEY(`country_id`) REFERENCES `Country`(`country_id`);
ALTER TABLE
    `Treatment` ADD CONSTRAINT `treatment_admission_id_foreign` FOREIGN KEY(`admission_id`) REFERENCES `Admission_record`(`admission_id`);
ALTER TABLE
    `Detection_Organisation` ADD CONSTRAINT `detection_organisation_city_id_foreign` FOREIGN KEY(`city_id`) REFERENCES `City`(`city_id`);