-- Create a database
CREATE DATABASE enhanceit
-- Location of the database
LOCATION '/enhanceit';    

-- Specify the database to be used
USE enhanceit;

-- Enineers table (External)
CREATE EXTERNAL TABLE IF NOT EXISTS 
engineers ( 
    id INT, 
    firstName STRING, 
    lastName STRING, 
    age INT,
    city STRING,
    country STRING,
    salary INT,
    department INT)
STORED AS ORC
LOCATION '/user/hive/hive_assignment';
-- tblproperties("transactional" = "true");
-- CLUSTERED BY (age) INTO 2 BUCKETS STORED AS ORC;
-- ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'


-- Managers table (External)
CREATE EXTERNAL TABLE IF NOT EXISTS 
managers
LIKE Engineers
LOCATION '/user/maria_dev/enhanceit';


-- Departments table (External)
CREATE EXTERNAL TABLE IF NOT EXISTS 
departments (
    id INT,
    name STRING)
LOCATION '/user/maria_dev/enhanceit';

LOAD DATA LOCAL INPATH '/enhanceit/engineers.csv' OVERWRITE INTO TABLE engineers;


-- Values into Managers table
INSERT INTO managers
  VALUES (001, 'Olson', 'Dimanche', 35, 'Port_Prince', 'Heiti', 65000, 2);


-- Values into Department table
INSERT INTO departments
    VALUES (001, 'Big_Data');


-- Hire and renewal date
ALTER TABLE
engineers
ADD columns (date_of_joining DATE, contract_renewal DATE)
LOCATION '/user/maria_dev/hive_assignment';


--Comment UPDATE engineers 
--Comment SET hire_date = "2019-10-29",
--Comment renewal_date = DATE_ADD(ADD_MONTHS("2019-10-29", 12), 0);